import socket
import sys

# The initial variables. Feel free to alter these.
host=''
port = 80
# Make a socket object, set some options
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind a port to our socket, so folks can connect to it
conn.bind(host, port)

conn.listen(1)

print(f'Your server is now running on host {host} and listening on port {port}')

