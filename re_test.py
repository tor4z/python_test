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

string = "How do you 1s0086 turn this on?"

pat = re.compile(r'.*?(?P<do>do)\s+\w+\s+(?P<you_d>[a-zA-Z_]\w+|\d+).*')

m = pat.match(string)

print(m.groups())
print(m.groupdict())


######################

string = "ADD R1 R2"
string2 = "ADD R1 1"

pat = re.compile(r'\s*(?P<ins>[a-zA-Z_]\w*)\s+(?P<arg1>[a-zA-Z_]\w*)\s+(?P<arg2>[a-zA-Z_]\w*|\d+)\s*')
# pat = re.compile(r'\s*(?P<ins>[a-zA-Z_]\w*)\s+(?P<arg1>[a-zA-Z_]\w*)\s*')

m = pat.match(string)
print(m.groupdict())

m = pat.match(string2)
print(m.groupdict())


######################

string = " // ADD R1 R2"

pat = re.compile(r'\s*//.*')

m = pat.match(string)
print(m)


######################
string = "\n"

pat = re.compile(r'\s*\n')

m = pat.match(string)
print(m)
