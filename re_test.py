import re

string = "How do you turn this on?"

pat = re.compile(r'.*?(?P<do>do).*?[(?P<you>you)|(?P<me>me)]+.*')

m = pat.match(string)

print(m.group("do"))

print(m.groupdict())
'''
print(m.group("you"))
print(m.group("me"))
'''

################

string = "How do you 10086 turn this on?"

pat = re.compile(r'.*?(?P<do>do)\s*?\w+\s*(?P<you_d>[\w+|\d+]+).*')

m = pat.match(string)

print(m.groups())
print(m.groupdict())
