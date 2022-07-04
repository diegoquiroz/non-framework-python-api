import socketserver
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler
from urllib.parse import urlsplit, parse_qs
from urls import urlpatterns

import sys

sys.path.append('./')


class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlsplit(self.path)
        query = parse_qs(parsed_path.query)
        for (path, callback) in urlpatterns:
            if parsed_path.path == path:
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(callback.get(query))


if __name__ == "__main__":
    PORT = 8000
    server = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
    print(f"Server started at 0.0.0.0:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
