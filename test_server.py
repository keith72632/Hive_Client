import socket
import sys
from time import sleep
from datetime import datetime

HOST = '192.168.0.183'
PORT = 666

def create_sock(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created\n')

    s.bind((host, port))
    print(f'Socket for {host} bound on port {PORT}\n')

    s.listen(5)
    print('Listening...\n')

    try:
        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Connected by {addr} at {datetime.now()}')
                data = conn.recv(1024)
                if data:
                    print(data.decode())
    except KeyboardInterrupt:
        print(f'\nKeyboard Interrupt. Closing socket host {HOST}:{PORT}')
        s.close()

if __name__ == '__main__':
    create_sock(HOST, PORT)        
