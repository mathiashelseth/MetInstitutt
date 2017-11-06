import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip = "***REMOVED***"
port = 4002

server_address = (ip, port)
print("Connecting...")
sock.connect(server_address)
print("Connected to", ip, "with port", port)

try:

    # Send data
    message = "#04" + str(chr(13))
    print('Sending "%s"' % message)
    sock.sendall(message.encode('utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message.encode('utf-8'))

    while amount_received < amount_expected:
        data = sock.recv(4096)
        # Compensate for data delay
        time.sleep(0.5)
        amount_received += len(data)
        print('Recieved "%s"' % data)

finally:
    print('Closing Socket...')
    sock.close()
    print('Socket closed!')
