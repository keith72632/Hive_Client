import socket
import sys
from time import sleep
from pprint import pprint

HOST = sys.argv[1]
PORT = int(sys.argv[2])
KNRM = "\x1B[0m"
KRED = "\x1B[31m"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
    s.connect((HOST, PORT))
    print('Connected to Server')
    #data = s.recv(69)
    #print(data)
    i = 0
    while 1:
        print(i)
        str_i = str(i)
        s.send(str_i.encode())
        sleep(10)
        i += 1
    s.close()

addrinfo = socket.getaddrinfo(HOST, PORT)

print(KRED)
print('Server Info')
pprint(addrinfo)
print(KNRM)

print('Host Name:',socket.gethostname())

