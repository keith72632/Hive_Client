from threading import *
import socket

SERVER = '192.168.0.183'
PORT = 666


def new1():
    data = f'From {current_thread().getName()}'
    data1 = data.encode()

    print(f'Thread: {current_thread().getName()}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect((SERVER, PORT))
        print('Connected to server')

        s.send(data1)
        print(f'Data sent: {data1}')
        s.close()

def new2():
    data = f'From {current_thread().getName()}'
    data1 = data.encode()

    print(f'Thread: {current_thread().getName()}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect((SERVER, PORT))
        print('Connected to server')

        s.send(data1)
        print(f'Data sent: {data1}')
        s.close()


#main thread always exectutes
t1 = Thread(target=new1)
t2 = Thread(target=new2)
t1.start()
t2.start()

#join the child back with main
t1.join()
t2.join()

print("Bye", current_thread().getName())
