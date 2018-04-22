import threading
import time

class A:
    def __init__(self):
        self.v=0
        
    def set_v(self, v):
        self.v=v
        
def _worker(a):
    time.sleep(1)
    print(a.v)
    

def new_thread():
    a=A()
    t=threading.Thread(target=_worker, args=(a,))
    t.start()
    return a
    
if __name__ == "__main__":
    a=new_thread()
    a.set_v(100)
    