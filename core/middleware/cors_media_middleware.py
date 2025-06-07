from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class MediaCORSMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.startswith('/media/'):
            origin = request.headers.get('Origin')

            if settings.CORS_ALLOW_ALL_ORIGINS:
                response["Access-Control-Allow-Origin"] = "*"  # для all
            elif origin and origin in settings.CORS_ALLOWED_ORIGINS:
                response["Access-Control-Allow-Origin"] = origin  # разрешенные

            if "Access-Control-Allow-Origin" in response:
                response["Access-Control-Allow-Credentials"] = "true"
                response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
                response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

        return response
