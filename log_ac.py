import socket
import datetime


HOST = 'www.acfun.cn'    # The remote host
PORT = 80              # The same port as used by the server
data = f"""
POST /login.aspx HTTP/1.1\r\n\
Date: {datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")}\r\n\
Accept: */*\r\n\
Accept-Encoding: deflate\r\n\
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\n\
Cache-Control: no-cache\r\n\
Connection: keep-alive\r\n\
Content-Length: 42\r\n\
Content-Type: application/x-www-form-urlencoded; charset=UTF-8\r\n\
DNT: 1\r\n\
Host: {HOST}\r\n\
\r\n\
password=your_password&username=your_phone_number\
"""
print(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data.encode())
    while True:
        body = s.recv(1024)
        print(body.decode("utf-8"))
        if not body:
            break

