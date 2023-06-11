from django.http import HttpResponseForbidden

class RestrictIPMiddleware:
    allowed_ips = ['127.0.0.1','121.196.164.199','47.98.43.127']  # Replace with your allowed IPs
    restricted_path = '/api/v1/check'  # The path you want to restrict

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META['REMOTE_ADDR']
        # Check if the path is the restricted one and if the client's IP is not in the allowed list
        if request.path == self.restricted_path and client_ip not in self.allowed_ips:
            return HttpResponseForbidden()  # Return 403 Forbidden response
        response = self.get_response(request)
        return response
