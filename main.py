import re

mystr = "hello yo"

pattern = re.compile(r"hello")

matches = re.finditer(pattern, mystr)

for match in matches:
    print(match)
