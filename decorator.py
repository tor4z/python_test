def direct(a):
    def _exec(func):
        print(func.__name__)
        func(a)
    return _exec


@direct(1)
def run(a):
    print("run ..")
