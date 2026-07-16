import http.server
import socketserver
import json

class MyAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Ana səhifə yoxlaması
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        # 2. /data səhifəsi yoxlaması
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(sample_data).encode())

        # 3. /status səhifəsi yoxlaması
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode())

        # 4. Tapılmayan səhifə (404)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())

PORT = 8000
with socketserver.TCPServer(("", PORT), MyAPIHandler) as httpd:
    httpd.serve_forever()
