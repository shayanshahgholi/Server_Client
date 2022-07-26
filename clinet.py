from http.server import BaseHTTPRequestHandler, HTTPServer
from concurrent.futures import ThreadPoolExecutor
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        num1, num2 = self.path[1:].split('+')
        result = int(num1) + int(num2)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes('<br> result: {} </br>'.format(result) , "utf8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8080), handler) as server:
    server.serve_forever()
