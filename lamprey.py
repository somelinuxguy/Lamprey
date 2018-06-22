import random
import linecache
from http.server import BaseHTTPRequestHandler, HTTPServer

class webServerHandler(BaseHTTPRequestHandler):
    # method handlers (from BaseHTTPRequestHandler)
    server_version = "Zeus"
    sys_version = "(httpd/0.0.b5)"
    # GET
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # todo: reply with poisonPen instead
        replyMessage = "moo"
        self.wfile.write(bytes(replyMessage, "utf8"))
        return

    # PUT
    def do_PUT(self):
        self.send_response(201)
        self.send_header('Content-location',"/command.com")
        self.end_headers()
        # todo: Nothing. I think this is awful enough.
        replyMessage = "INFO: WARN - SUCCESS: ERROR"
        self.wfile.write(bytes(replyMessage, "utf8"))
        return

class poisonPen(object):
    def __init__(self):
        self.junk = []
    
    def FormatParagraph(self, junk):
        #get a junk list, and format it to look like a paragraph: add <p> and <br> and some junk styles.
        pass

    def FormatHeader(self, junk):
        #get a junk list, and format it to look like a Header.
        pass


# A function to run the httpd server using our handler class.
def startHttpd(addy,port):
    print(f"Starting fake http server on address {addy} and port {port}")
    server_address = (addy, port)
    httpd = HTTPServer(server_address, webServerHandler)
    
    httpd.serve_forever()

def getJunk(junklist):
    # from 25 to 100 junk words: in file, read a random line , insert result in a list
    # return that list
    howmanywords = random.randint(25, 100)
    for _ in range(howmanywords):
        junklist.append( linecache.getline(wordsFilename, random.randint(5, wordsFileLen)).rstrip() )
    return junklist

# Main
wordsFilename = "/usr/share/dict/words"
print("Waking up the Lamprey...")

# The length of your words file is important, and variable.
# Let's count it, and then make this a global value.
with open(wordsFilename) as wordfile:
    wordsFileLen = sum(1 for line in wordfile)

# Debugging cruft I left here - make an instance of the poisonPen
#fakepage = poisonPen()
#fakepage.junk = getJunk(fakepage.junk)
#print(fakepage.junk)

startHttpd('127.0.0.1', 8000)