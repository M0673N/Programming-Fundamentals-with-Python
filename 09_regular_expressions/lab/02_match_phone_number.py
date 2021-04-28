import re

data = input()
regex = r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
result = re.finditer(regex, data)
result = [i.group(0) for i in result]
print(", ".join(result))
