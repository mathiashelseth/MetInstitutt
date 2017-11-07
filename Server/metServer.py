import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip = "37.26.220.85"
port = 4002

server_address = (ip, port)
print("Connecting...")
sock.connect(server_address)
print("Connected to", ip, "with port", port)

try:

    # Send data
    message = "#04" + str(chr(13))
    print('Sending "%s"' % message)
    sock.send(message.encode('utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = 9

    dChar = []
    while amount_received < amount_expected:
        data = sock.recv(1)
        amount_received += len(data)
        dataFull = str(data,'utf-8')

        dVal = dataFull
        dChar.append(dVal)

    dataRes = dChar[2] + dChar[3] + dChar[4] + dChar[5] + dChar[6] + dChar[7]
    print(dataRes)


finally:
    print('Closing Socket...')
    sock.close()
    print('Socket closed!')
