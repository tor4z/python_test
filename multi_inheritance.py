class A:
    @classmethod
    def m(cls):
        pass

class A1:
    def __init__(self):
        print("init A1")

class B:
    def __init__(self, *args, **kwargs):
        print('Init B ')

class C(A, A1, B):
    def __init__(self):
        super().__init__()

# ==========================================

class First:
    def __init__(self):
        print("first")

class Second(First):
    def __init__(self):
        super().__init__()
        print("second")

class Third(First):
    def __init__(self):
        super().__init__()
        print("third")

class Fourth(Second, Third):
    def __init__(self):
        super().__init__()
        print("that's it")

if __name__ == "__main__":
    c = C()

    # ============
    print("====")

    f = Fourth()

    """
    Result:

    init A1
    ====
    first
    third
    second
    that's it
    """