import re

pattern_title = r"<title>(.+)</title>"
pattern_content = r"<body>.+</body>"
split_tags = r"<[A-Za-z -=]+>"
split_ns = r"\\n"

text = input()

title = re.findall(pattern_title, text)
content = re.findall(pattern_content, text)
content = re.split(split_tags, content[0])
content = "".join(content)
content = re.split(split_ns, content)
content = "".join(content)
content = content.split()
content = " ".join(content)

print(f"Title: {title[0]}")
print(f"Content: {content}")
