from django.http import HttpResponseForbidden

class RestrictIPMiddleware:
    allowed_ips = ['127.0.0.1','121.196.164.199']  # Replace with your allowed IPs

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META['REMOTE_ADDR']
        if client_ip not in self.allowed_ips:
            return HttpResponseForbidden()  # Return 403 Forbidden response
        response = self.get_response(request)
        return response
