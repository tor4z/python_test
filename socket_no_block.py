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
timeout = 10

def send(sock, end):
    now = time.time()
    if now > end:
        print("exit timeout.")
        LOOP.stop()
    try:
        # time.sleep(1)
        print(">>")
        sock.sendall(b'Raised when an operation would block on an object (e.g. socket)')
    except BlockingIOError as e:
        LOOP.remove_writer(sock.fileno())
        
def recv(sock):
    try:
        body = sock.recv(1024)
        if not body:
            LOOP.remove_reader(sock.fileno())
            print("exit")
            LOOP.stop()
        else:
            print(body)
    except BlockingIOError:
        if not body:
            LOOP.remove_reader(sock.fileno())
            print("exit")
            LOOP.stop()



LOOP.add_writer(sock.fileno(), functools.partial(send, sock, time.time()+timeout))
LOOP.add_reader(sock.fileno(), functools.partial(recv, sock))

LOOP.run_forever()
