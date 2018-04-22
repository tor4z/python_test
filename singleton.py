import threading
import time

class Single:
    _INSTANCE = None
    _LOCK = threading.RLock()
    
    def __init__(self, _new=False):
        if not _new:
            raise Exception("Don't instancing it direct")
        
    @classmethod
    def instance(cls):
        if cls._INSTANCE is None:
            with cls._LOCK:
                if cls._INSTANCE is None:
                    cls._INSTANCE = cls(True)
        return cls._INSTANCE

class A:
    pass
        
def _worker():
    s  = Single.instance()
    a  = A()
    print(s, "s")
    print(a, "a")
        
def new_thread(n):
    tp=[]
    for i in range(n):
        t=threading.Thread(target=_worker)
        t.start()
        tp.append(t)
    for t in tp:
        t.join()
    
if __name__ == "__main__":
    new_thread(5)
    