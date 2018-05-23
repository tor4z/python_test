import time


def g():
    i = 0
    while i < 10:
        yield i
        i += 1


class AA:
    def __next__(self):
        print("AA next")
        return 0


class A:
    def __init__(self):
        pass

    def __iter__(self):
        print("iter")
        return AA()
        # return g()

    def __next__(self):
        print("next")
        return 2

if __name__ == "__main__":
    a = A()
    print(dir(g()))
    for i in a:
        print(i)
        time.sleep(0.1)