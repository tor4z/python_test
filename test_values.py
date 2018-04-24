s={}
 
def update_s(s):
    s.update({"a":1})
    
print(s)
update_s(s)
print(s)

class A:
    def __init__(self):
        self.test()

    @property
    def val(self):
        print("call val")
        return 1
        
    def test(self):
        self.val
       
       
a=A()