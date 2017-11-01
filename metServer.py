#Importing socket to be able to communicate with server
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Defining the IP adress and port of the device
server = '37.26.220.85'
port = 4002

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
#Requesting a connection to the server
s.connect((server, port))
#Sending commands to recieve measurements in ohm
s.send(request.encode())
result = s.recv(4096)

#print(result)

#Requires the result to have content to be printed
while(len(result) > 0):
    print(result)
    result = s.recv(4096)
