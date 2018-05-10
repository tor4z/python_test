class C:
    def __init__(self):
        print("init")

    def __del__(self):
        print("del object")

if __name__ == "__main__":
    c = C()
    del c
