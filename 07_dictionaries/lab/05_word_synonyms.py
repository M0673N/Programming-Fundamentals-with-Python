words_count = int(input())
dictionary = {}
words = []
for i in range(words_count * 2):
    words.append(input())
for i in range(0, len(words), 2):
    key = words[i]
    value = words[i + 1]
    if key not in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] += f", {value}"

for key, value in dictionary.items():
    print(f"{key} - {value}")
