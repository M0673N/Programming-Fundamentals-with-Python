word = input()
for char in range(len(word) - 1, -1, -1):
    print(f"{word[char]}", end="")
