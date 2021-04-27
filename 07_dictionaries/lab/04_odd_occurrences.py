words = input().split(" ")
dictionary = {}
for word in words:
    word_l = word.lower()
    if word_l not in dictionary:
        dictionary[word_l] = 0
    dictionary[word_l] += 1
for key, value in dictionary.items():
    if value % 2 == 1:
        print(key, end=" ")
