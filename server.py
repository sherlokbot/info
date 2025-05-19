#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        if self.path.endswith('.html') or self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    port = 8000
    print(f"Starting server at http://localhost:{port}")
    server = HTTPServer(('localhost', port), CustomHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()
        sys.exit(0) 