import re

data = input()
regex = r"\d{2}([\./-])[A-Z][a-z]{2}\1\d{4}"
result = re.finditer(regex, data)
for i in result:
    day = i.group(0)[0:2]
    month = i.group(0)[3:6]
    year = i.group(0)[7:11]
    print(f"Day: {day}, Month: {month}, Year: {year}")
