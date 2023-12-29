from http.server import HTTPServer,BaseHTTPRequestHandler

HOST="localhost"
PORT=9000

class karthikHTTP(BaseHTTPRequestHandler):

    def do_Get(Self):
        Self.send_response(200)
        Self.send_header("Content-type","text/html")
        Self.end_headers()

        Self.wfile.write(bytes("<html><body><h1>My First Heading</h1></body></html>","utf-8"))



server=HTTPServer((HOST,PORT),karthikHTTP)
print("Now the server is running")
server.serve_forever()
server.server_close()
print("Server Stopped")
