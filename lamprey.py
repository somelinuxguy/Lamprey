import socket
import sys

# To Do: 
# 1. Read a JSON or YAML config file  
# 2. Loop for every port/listener you want the program to make. 
# 3. Serve back the response as defined in the config file when somebody connects
#    This sort of "defines" what kind of server a client thinks it is talking to.
#    Reply with an SMTP header on any port, and that's what you are telling the client you are.
#    There is no need to write config for specific daemon types, unless their responses
#    are gross encrypted binary (ssh https et al.)

# The initial variables. Feel free to alter these.
host=''
port = 80
# Make a socket object, set some options
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind a port to our socket, so folks can connect to it
conn.bind(host, port)

conn.listen(5)
print(f'Your server is now running on host {host} and listening on port {port}')

while 1:
    (clientsocket, address) = conn.accept()
    
