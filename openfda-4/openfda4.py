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
        if self.path == "/":
            with open("search.html", "r") as f:
                f=f.read()
                self.wfile.write(bytes(f, "utf8"))
        elif self.path =="search":
            params=self.path.split("?")[1]
            limit = params.split("&")[1].split("=")[1]
            drug=params.split("&")[0].split("=")[1]

            self.wfile.write(bytes(drug + limit, "utf8"))
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