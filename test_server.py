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

    return s

def receive_data(sock):
    conn, addr = sock.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            if data:
                print(data.decode())


if __name__ == '__main__':
    s = create_sock(HOST, PORT)

    receive_data(s)
