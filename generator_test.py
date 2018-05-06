def gen():
    n = 0
    print("gen start")
    while n < 5:
        print("before yield")
        yield (n, n+1)
        print("after yield")
        n += 1

def gen2():
    k = gen()
    while True:
        result = next(k)
        yield result[1]

if __name__ == "__main__":
    for i in gen():
        print("get", i)

    print("========")

    for i in gen2():
        print("get", i)