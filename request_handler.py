import json
from urllib.parse import urlparse, parse_qs
from repository import all, single, create, delete, update, get_all_or_single, query_get
from http.server import BaseHTTPRequestHandler, HTTPServer

class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  
        resource = path_params[1]
        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)
        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def do_GET(self):
        response = {}
        parsed = self.parse_url(self.path)
        # If the path does not include a query parameter, continue with the original if block
        if '?' not in self.path:
            ( resource, id ) = parsed
            response = get_all_or_single(self, resource, id)
            if response == '':
                self._set_headers(404)
            elif response == {}:
                self._set_headers(405)
            else:
                self._set_headers(200)
        else: # There is a ? in the path, run the query param functions
            (resource, query) = parsed
            response = query_get(query, resource)
            if response == '':
                self._set_headers(404)
            else:
                self._set_headers(200)
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        new_post = create(resource, post_body)
        if 'id' in new_post:
            self._set_headers(201)
        elif 'message' in new_post:
            self._set_headers(400)
        else:
            self._set_headers(404)
        self.wfile.write(json.dumps(new_post).encode())

    def do_PUT(self):
        response = ""
        self._set_headers(404)
        self.wfile.write(json.dumps(response).encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response
        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        (resource, id) = self.parse_url(self.path)
        response = delete(resource, id)
        if resource in ('species', 'owners', 'snakes'):
            self._set_headers(405)
        else:
            self._set_headers(404)
        self.wfile.write(json.dumps(response).encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
