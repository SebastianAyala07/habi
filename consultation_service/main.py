from http.server import BaseHTTPRequestHandler, HTTPServer
from controllers.property_controller import PropertyController
from controllers.status_history_controller import StatusHistoryController
import json



class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        response = None
        if not self.path or self.path == "/":
            response, error = json.dumps(
                {
                    "title": "Habi Test Project: consultation_service",
                    "author": "Sebastian Ayala Gonzalez",
                    "year": 2022,
                    "linkedin_profile": "https://www.linkedin.com/in/sebastianayala7/"
                }
            ), None
        elif self.path.split("?")[0] == "/property":
            # filters = self.path.split("?")
            # filters.pop(0)
            response, error = PropertyController.get_properties()
        self._set_headers()
        self.wfile.write(
            bytes(
                response if response else "", 'utf-8'
            )
        )


def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...'%port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()