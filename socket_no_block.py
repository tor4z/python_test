import socket
import asyncio
import functools
import time


HOST = '127.0.0.1'
PORT = 8080
LOOP = asyncio.get_event_loop()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.setblocking(False)

def send(sock):
    time.sleep(1)
    try:
        print("start send data.")
        sock.sendall(b'data,')
    except BlockingIOError:
        LOOP.remove_writer(sock.fileno())
        LOOP.add_writer(sock.fileno(), functools.partial(send, sock))
    except:
        LOOP.remove_writer(sock.fileno())
        LOOP.stop()

def recv(sock):
    try:
        print("start recv data.")
        print(sock.recv(1024))
    except BlockingIOError:
        LOOP.remove_reader(sock.fileno())
        LOOP.add_reader(sock.fileno(), functools.partial(recv, sock))
    except:
        LOOP.remove_reader(sock.fileno())
        LOOP.stop()

LOOP.add_writer(sock.fileno(), functools.partial(send, sock))
LOOP.add_reader(sock.fileno(), functools.partial(recv, sock))

sock.sendall(b'start')


LOOP.run_forever()