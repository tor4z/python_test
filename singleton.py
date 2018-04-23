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

class Single2:   
    _S_LOCK = threading.RLock()
    def __init__(self, _new=False):
        if not _new:
            raise Exception("Don't instancing it direct")
        
    @classmethod
    def instance(cls):
        if not hasattr(cls, "_LOCK"):
            with cls._S_LOCK:
                if not hasattr(cls, "_LOCK"):
                    cls._LOCK = threading.RLock()
                
        if not hasattr(cls, "_INSTANCE"):
            with cls._LOCK:
                if not hasattr(cls, "_INSTANCE"):
                    cls._INSTANCE = cls(True)
        return cls._INSTANCE
        
class UseSingle(Single):
    def __init__(self):
        pass
        
class A:
    pass
        
def _worker():
    s  = Single.instance()
    s2  = Single2.instance()
    a  = A()
    u = UseSingle()
    print(s, "s")
    print(s2, "s2")
    print(a, "a")
    print(u, "u")
        
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
    