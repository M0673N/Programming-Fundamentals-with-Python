data = input()
result = ""
previous_letter = ""
for letter in data:
    if letter == previous_letter:
        continue
    previous_letter = letter
    result += letter
print(result)
