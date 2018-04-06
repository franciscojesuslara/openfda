import http.server
import socketserver

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8007

# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open("search.html","r") as f:
            if self.path == "/":
                message = f.read()
            elif search in self.path:
                message =
            else:
                message =


        self.wfile.write(bytes(message, "utf8"))
        print("File served")
        return


# Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
        pass

httpd.server_close()
print("")
print("Server stopped!")


# https://github.com/joshmaker/simple-python-webserver/blob/master/server.py