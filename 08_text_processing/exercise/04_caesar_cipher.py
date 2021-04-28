data = input()
result = ""
for letter in data:
    new_letter = chr(ord(letter) + 3)
    result += new_letter
print(result)
