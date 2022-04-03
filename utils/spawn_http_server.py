"""
Spawns an http server in the directory
it is executed for easy access to files.
"""

import http.server
import socketserver
import sys

def main():
    PORT = int(sys.argv[1])
    run_server(PORT)

def run_server(port):
    
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(('', port), Handler) as httpd:
        httpd.serve_forever()

if __name__ == '__main__':
    main()