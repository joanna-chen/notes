import socket

# the variables
username = str.encode("joanna-chen")
message = "hello!"
timestamp = 1014

# create socket
s = socket.socket()

# connect to machine 'localhost' on port 5000
host = 'localhost'
port = 5000
s.connect((host, port))
print('connected to server')

# send stuff to server
s.send(username)
s.send(message)
s.send(str(timestamp))

s.close
