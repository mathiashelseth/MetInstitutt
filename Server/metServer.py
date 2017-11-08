import socket
import sys
import time

def space():
    print()
    print()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip = "***REMOVED***"
port = 4002

print("Connecting...")
sock.connect((ip, port))
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

    dataRes = float(dChar[2] + dChar[3] + dChar[4] + dChar[5] + dChar[6] + dChar[7])
    print(dataRes)


    R = float(input("R = %s" + str(chr(13))) % dataRes)
    t = ((((-R_0)*a) + math.sqrt((R_0 ** 2) * (a ** 2) - 4 * R_0 * b * (R_0 - R))) / (2 * R_0 * b))
    space()
    if(t == -0.0):
        print("t = 0 C")
    else:
        print("t =",t,"C")


finally:
    print('Closing Socket...')
    sock.close()
    print('Socket closed!')
