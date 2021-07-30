from threading import *
from datetime import datetime
import socket
import sys

HOST = '192.168.0.183'
PORT1 = 666
PORT2 = 888
def recieving_thread():
    global DATA
    print(f'Thread: {current_thread().getName()}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.bind((HOST, PORT1))
        print(f'Listening on address: {HOST} port: {PORT1}')

        s.listen(5)

        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024)
                    data = data.decode()
                    if data:
                        print(f'Data: {data} recieved from {conn.getsockname()} at {datetime.now()}')
                        DATA = data
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            s.close()
            sys.exit()

def sending_thread():
    print(f'Thread: {current_thread().getName()}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.bind((HOST, PORT2))
        print(f'Listening on address: {HOST} port: {PORT2}')

        s.listen(5)

        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    data = str(DATA)
                    data = data.encode()
                    conn.send(data)
                    print(f'Data: {data} sent to {conn.getsockname()}')
        except KeyboardInterrupt:
            print('Keyboard interrupt')
            s.close()
            sys.exit()

#main thread always exectutes
t1 = Thread(target=recieving_thread)
t2 = Thread(target=sending_thread)
t1.start()
t2.start()

#join the child back with main
t1.join()
t2.join()

print("Bye", current_thread().getName())
