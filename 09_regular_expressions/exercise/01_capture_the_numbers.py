import re

line = input()
pattern = r"\d+"
while line:
    result = re.findall(pattern, line)
    if result:
        print(*result, end=" ")
    line = input()
