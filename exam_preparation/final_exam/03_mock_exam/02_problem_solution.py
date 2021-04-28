import re

text = input()
pattern = r"(@|#)(?P<word_1>[A-Za-z]{2}[A-Za-z]+)\1\1(?P<word_2>[A-Za-z]{2}[A-Za-z]+)\1"

hidden_words = re.findall(pattern, text)
mirror_words = []
for item in hidden_words:
    if item[1] == "".join(reversed(item[2])):
        mirror_words.append(item[1])
        mirror_words.append(item[2])

if not hidden_words:
    print("No word pairs found!")
else:
    print(f"{len(hidden_words)} word pairs found!")
result = []
if not mirror_words:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    for i in range(len(mirror_words)):
        if i % 2 == 0:
            if i + 1 < len(mirror_words):
                result.append(f"{mirror_words[i]} <=> {mirror_words[i + 1]}")
    print(", ".join(result))
