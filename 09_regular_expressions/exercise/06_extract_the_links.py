import re

pattern = r"(www\.)([A-Za-z0-9-]+)(\.[a-z]+)+"

command = input()
while command:
    result = re.search(pattern, command)
    if result:
        print(result.group())
    command = input()
