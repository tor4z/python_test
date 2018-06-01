import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', default="a.out")
    parser.add_argument('input', type=argparse.FileType("r"))

    result = parser.parse_args()

    print(result.o)