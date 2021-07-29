import socket
import sys
from time import sleep
from pprint import pprint
from sensors import setup, gpio_read, gpio_write

data = 'hey\n'
gpio_channel1 = 11
gpio_channel2 = 13
HOST = sys.argv[1]
PORT = int(sys.argv[2])
KNRM = "\x1B[0m"
KRED = "\x1B[31m"

def sendData(host, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect((host, port))
        print('Connected to Server')
        string_data = str(data)
        byte_data = string_data.encode()
        s.send(byte_data)
        print(f'Data sent {data}')
        s.close()

def getServerInfo(host, port):
    addrinfo = socket.getaddrinfo(host, port)
    print(KRED)
    print('Server Info')
    pprint(addrinfo)
    print(KNRM)
    print('Host Name:',socket.gethostname())

if __name__ == '__main__':
    setup(gpio_channel1, gpio_channel2)
    while True:
        gpio_write(gpio_channel2, 1)
        new_data = gpio_read(gpio_channel1)
        sendData(HOST, PORT, new_data)
        sleep(5)
        gpio_write(gpio_channel2, 0)
        sleep(5)
