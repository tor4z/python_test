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


'''
The socket is non-blocking so recv() will raise an exception
if there is no data to read. Note that errno.EWOULDBLOCK =
errno.EAGAIN = 11. This is Python's (well the OS really)
way of telling you to try the recv() again later.

exception BlockingIOError
Raised when an operation would block on an object (e.g. socket)
set for non-blocking operation. Corresponds to errno
EAGAIN, EALREADY, EWOULDBLOCK and EINPROGRESS.
'''

def send(sock):
    try:
        time.sleep(1)
        print("start send data.")
        sock.sendall(b'data,')
    except BlockingIOError:
        LOOP.remove_writer(sock.fileno())
        LOOP.add_writer(sock.fileno(), functools.partial(send, sock))
    except:
        print("exit.")
        LOOP.remove_writer(sock.fileno())
        LOOP.stop()

def recv(sock):
    try:
        time.sleep(1)
        print("start recv data.")
        print(sock.recv(1024))
    except BlockingIOError:
        LOOP.remove_reader(sock.fileno())
        LOOP.add_reader(sock.fileno(), functools.partial(recv, sock))
    except:
        print("exit")
        LOOP.remove_reader(sock.fileno())
        LOOP.stop()

LOOP.add_writer(sock.fileno(), functools.partial(send, sock))
LOOP.add_reader(sock.fileno(), functools.partial(recv, sock))

sock.sendall(b'start')


LOOP.run_forever()