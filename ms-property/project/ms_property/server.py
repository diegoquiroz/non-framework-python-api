import sys

sys.path.append('./')
from http import HTTPStatus
from urls import urlpatterns
from webob import Request, Response


class API:
    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        response = Response()
        for (path, handler) in urlpatterns:
            if request.path == path:
                handler(request, response)
                return response
        response.status_code = HTTPStatus.NOT_FOUND
        response.text = "Page not found"
        return response


app = API()
