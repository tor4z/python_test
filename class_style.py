import sys

class C:
    def __init__(self):
        pass
        
    if sys.platform == "win32":
        def run(self):
            print("run win 32")
    else:
        def run(self):
            print("run other")

# ----------------
 
class A1:
    def __init__(self):
        print("init class a1")

class A2:
    def __init__(self):
        print("init class a2")

class B:
    A_CLS = None
    def __init__(self):
        self.a = self.A_CLS()

class B1(B):
    A_CLS = A1
    def __init__(self):
        super().__init__()

class B2(B):
    A_CLS = A2
    def __init__(self):
        super().__init__()

B1()
B2()

def test_clean_up():
    try:
        return 1
    finally:
        print("Clean up.")

test_clean_up()