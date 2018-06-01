if __name__ == "__main__":
    filename = "file_test.txt"
    fp = open(filename, "r")

    while True:
        line = fp.readline()
        if line is '':
            break
        if line == '\n':
            continue
        print(line)

    fp.close()