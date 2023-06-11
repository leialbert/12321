from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PhoneNumber, RequestLog

class CheckPhoneNumberView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

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
            request_ip=request.META['REMOTE_ADDR']
        )

        # Prepare the response
        response_data = {"callId": call_id}
        if exists:
            response_data["forbid"] = 1

        return Response(response_data)