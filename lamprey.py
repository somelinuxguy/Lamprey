# total rework for python 3 and its lovely http library
# deal with raw sockets another time
from http.server import BaseHTTPRequestHandler, HTTPServer

class webServerHandler(BaseHTTPRequestHandler):
    # method handlers (from BaseHTTPRequestHandler)
    # GET
 
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type','text/html')
        self.end_headers()

        replyMessage = "moo"
        self.wfile.write(bytes(replyMessage, "utf8"))
        return

# A function to run the httpd server using our handler class.
def startHttpd(addy,port):
    print(f"Starting fake http server on address {addy} and port {port}")
    server_address = (addy, port)
    httpd = HTTPServer(server_address, webServerHandler)
    httpd.serve_forever()


# Main
print("Starting up...")
startHttpd('127.0.0.1', 8000)
