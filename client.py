import socket
import sys
from time import sleep
from pprint import pprint

data = 666
HOST = sys.argv[1]
PORT = int(sys.argv[2])
KNRM = "\x1B[0m"
KRED = "\x1B[31m"

def sendData(host, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect((host, port))
        print('Connected to Server')
        #data = s.recv(69)
        #print(data)
        str_i = str(data)
        s.send(str_i.encode())
        print(data)
        s.close()

def getServerInfo(host, port):
    addrinfo = socket.getaddrinfo(host, port)
    print(KRED)
    print('Server Info')
    pprint(addrinfo)
    print(KNRM)
    print('Host Name:',socket.gethostname())

if __name__ == '__main__':
    sendData(HOST, PORT, data)
