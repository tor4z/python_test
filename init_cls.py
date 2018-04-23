class A:
    def __init__(self, v=1):
        self.v = v
        
class B:
    def __init__(self):
        pass
        
    def init(self):
        pass
        
class C(A, B):
    def init(self, v):
        A.__init__(self, v)

c=C()
c.init(2)
print(c.v)