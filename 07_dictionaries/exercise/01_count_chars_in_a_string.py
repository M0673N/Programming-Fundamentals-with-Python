data = input().split()
new_data = []
for word in data:
    for char in word:
        new_data.append(char)

info = {}
for char in new_data:
    if char not in info:
        info[char] = 1
    else:
        info[char] += 1

for char in info:
    print(f"{char} -> {info[char]}")
