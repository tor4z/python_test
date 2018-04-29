from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])

if __name__ == "__main__":
    tor = Person("tor", 10)
    print(tor)
    print(f"NAME:{tor.name}; AGE:{tor.age}")