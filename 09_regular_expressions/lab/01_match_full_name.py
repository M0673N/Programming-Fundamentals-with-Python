import re

data = input()
regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
result = re.findall(regex, data)
print(" ".join(result))
