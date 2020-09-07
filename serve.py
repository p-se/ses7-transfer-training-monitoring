#!/usr/bin/env python3

import http.server
import socketserver

port = 8080

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', port), handler) as httpd:
    httpd.serve_forever()
