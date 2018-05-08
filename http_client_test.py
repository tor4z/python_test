import urllib.request

with urllib.request.urlopen('http://www.acfun.cn/') as f:
    print(f.read(300))
