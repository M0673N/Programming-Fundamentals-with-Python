names = input().split(", ")
wrong = False
passed = []
for name in names:
    wrong = False
    if not (3 <= len(name) <= 16):
        wrong = True
        continue
    for letter in name:
        if not letter.isalpha() and not letter.isdigit() and not ord(letter) == 95 and not ord(letter) == 45:
            wrong = True
            break
    if wrong:
        continue

    if not len(name) == len(name.strip()):
        wrong = True

    if not wrong:
        passed.append(name)

for name in passed:
    print(name)
