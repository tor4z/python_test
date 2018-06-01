def write_bin(filename):
    fp = open(filename, "wb")
    fp.write(bytes(int_to_chars(258)))
    # fp.write(bytes([1, 1]))
    fp.close()

def read_bin(filename):
    fp = open(filename, "rb")
    while True:
        data = fp.read(2)
        if not data:
            break
        print(data.decode())
    fp.close()


def int_to_chars(i):
    result = []
    while True:
        if(i <= 255):
            result.insert(0, i)
            break
        else:
            result.append(i % 256)
            i //= 256
    return result

if __name__ == "__main__":
    filename = "test.bin"
    write_bin(filename)
    print(int_to_chars(257))
    # read_bin(filename)