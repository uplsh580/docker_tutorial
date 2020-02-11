import http.server
import socketserver
import numpy as np


a = np.arange(15).reshape(3, 5)
print(a)


handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', 8080), handler) as httpd:
    print('Server listening on port 8080...')
    httpd.serve_forever()
