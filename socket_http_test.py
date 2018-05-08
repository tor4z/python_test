import socket
import datetime
import gzip
import io

HOST = 'www.163.com'    # The remote host
PORT = 80              # The same port as used by the server
data = f"""
GET / HTTP/1.1\r\n\
Date: {datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")}\r\n\
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\
Accept-Encoding: identity,deflate\r\n\
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\n\
Cache-Control: no-cache\r\n\
Connection: keep-alive\r\n\
DNT: 1\r\n\
Host: www.163.com\r\n\
Pragma: no-cache\r\n\
Upgrade-Insecure-Requests: 1\r\n\
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0\r\n\
\r\n\
"""
print(data)
body = b''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data.encode())
    while True:
        data = s.recv(1024)
        print(data.decode("gbk"))
        if not data:
            break
