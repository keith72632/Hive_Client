import socket
import sys
from time import sleep

HOST = '192.168.0.183'
PORT = 666

def create_sock(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created\n')

    s.bind((host, port))
    print(f'Socket for {host} bound on port {port}\n')

    s.listen(5)
    print('Listening...\n')

    while True:
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            data = conn.recv(1024)
            if data:
                print(data.decode())


if __name__ == '__main__':
    create_sock(HOST, PORT)        
