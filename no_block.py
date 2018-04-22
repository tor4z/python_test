import threading
import time

class Future:
    def __init__(self):
        self._res = None
        self._done = False
        self._e = threading.Event()
        
    def wait(self):
        self._e.wait()
        
    def set_result(self, res):
        self._res = res
        self._done = True
        self._e.set()
        
    def get_result(self):
        while True:
            if self._done:
                return self._res
            else:
                self.wait()
    
    def __str__(self):
        return str(self.get_result())

def go(func):
    fu = Future()
    def _exec():
        t=threading.Thread(target=wrapper, args=(func, fu))
        t.setDaemon(True)
        t.start()
        return fu
    return _exec
    
def wrapper(func, fu):
    fu.set_result(func())
    
@go
def f():
    print("run f")
    time.sleep(2)
    return 2

@go
def ff():
    print("run ff")
    time.sleep(1)
    return 1
    
r=f()
rr=ff()
print("==")
print(rr)
print(r)