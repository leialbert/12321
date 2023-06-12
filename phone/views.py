from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PhoneNumber, RequestLog
import json
from rest_framework.exceptions import ParseError


class CheckPhoneNumberView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            raise ParseError("Malformed JSON")
        # Extract the callId, caller and callee from the request data
        call_id = data.get('callId')
        caller = data.get('caller')
        callee = data.get('callee')[-11:]

        # Check if the callee number is in the PhoneNumber database
        exists = PhoneNumber.objects.filter(number=callee).exists()

        # Log the request
        RequestLog.objects.create(
            caller=caller,
            callee=callee,
            block=exists,
            # request_ip=request.META['REMOTE_ADDR'],
            request_ip = request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0] or request.META.get('REMOTE_ADDR'),

            callId=call_id
        )

        # Prepare the response
        response_data = {"callId": call_id}
        if exists:
            response_data["forbid"] = 1
            response_data["transactionId"] = '12321'


        return Response(response_data)
