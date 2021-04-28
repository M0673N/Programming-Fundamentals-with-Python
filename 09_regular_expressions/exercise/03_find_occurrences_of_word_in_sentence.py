import re

sentence = input().lower()
word = input().lower()
pattern = r"\b" + word + r"\b"
result = re.findall(pattern, sentence)
print(len(result))
