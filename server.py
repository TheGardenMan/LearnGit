import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello D')


httpd = socketserver.TCPServer(('', 1998), Handler)
print("Server will run")
httpd.serve_forever()
