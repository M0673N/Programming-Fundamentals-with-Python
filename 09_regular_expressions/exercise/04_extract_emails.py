import re

pattern = r"(^|(?<= ))([a-z0-9][a-z0-9._-]+[a-z0-9]\b@[a-z0-9-]+(\.[a-z0-9-]+)+)"

command = input()
result = re.findall(pattern, command)
for mail in result:
    print(mail[1])
