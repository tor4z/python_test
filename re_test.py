import re

string = b"how do you turn this on."

pat = re.compile(b'do')

s = pat.search(string)

start, end = s.span()
print(string[start:end])
