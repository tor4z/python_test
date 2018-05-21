class A:
    def __init__(self, val):
        self._val = val
    
    def __setattr__(self, key, val):
        if not key[0] == '_':
            print("A:", key, val)
        else:
            super().__setattr__(key, val)


class B:
    def __init__(self, val):
        self._val = val
    
    def __setattribute__(self, key, val):
        print("B:", key, val)

class C:
    def __init__(self, val):
        self._val = val
    
    def __set__(self, key, val):
        print("C:", key, val)

if __name__ == "__main__":
    a = A(1)
    b = B(1)
    c = C(1)

    a.a = 2
    b.a = 2
    c.a = 2

    b._val = 2

    print(a._val)