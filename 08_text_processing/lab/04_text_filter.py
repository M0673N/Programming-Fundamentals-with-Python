to_ban = input().split(", ")
text = input()
for word in to_ban:
    text = text.replace(word, "*" * len(word))
print(text)
