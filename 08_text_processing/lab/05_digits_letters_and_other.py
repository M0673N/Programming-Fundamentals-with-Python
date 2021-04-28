data = input()
digits = ""
letters = ""
for d in data:
    if d.isdigit():
        digits += d
for digit in digits:
    data = data.replace(digit, "")

for l in data:
    if l.isalpha():
        letters += l
for letter in letters:
    data = data.replace(letter, "")

print(digits)
print(letters)
print(data)
