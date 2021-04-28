import re

data = input()
regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
result = re.finditer(regex, data)
result = [i.group() for i in result]
print(*result)
