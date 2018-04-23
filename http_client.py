import requests
import threading
import time

s = requests.Session()

def get(url, i):
    #print(i,"starting...")
    start = time.time()
    req = requests.Request("GET", url)
    resp = s.send(req.prepare())
    #print(resp.status_code, round(time.time()-start, 3), "sec.")
    
def mt_get(url, n):
    start = time.time()
    pool = []
    for i in range(n):
        t = threading.Thread(target = get, args=(url, i))
        t.start()
        pool.append(t)
        
    for t in pool:
        t.join()
    return time.time() - start
        
def st_get(url, n):
    start = time.time()
    for i in range(n):
        get(url, i)
    return time.time() - start
    
if __name__ == "__main__":
    
    url = "https://www.microsoft.com"
    n = 20
    t = 10
    print("get %s %d times" % (url, n))
    mt_time = 0
    st_time = 0
    for i in range(t):
        mt_time += mt_get(url, n)
        st_time += st_get(url, n)
    print("Multi thread average", round(mt_time/t, 3), "sec.")
    print("Single thread average", round(st_time/t, 3), "sec.")

    """
    Result:
    get https://www.microsoft.com 20 times
    Multi thread average 0.319 sec.
    Single thread average 2.533 sec.
    """