data = input().split()
totals = 0
for item in data:
    temp = 0
    if 65 <= ord(item[0]) <= 90:
        temp = int(item[1:-1]) / (ord(item[0]) - 64)
    elif 97 <= ord(item[0]) <= 122:
        temp = int(item[1:-1]) * (ord(item[0]) - 96)

    if 65 <= ord(item[-1]) <= 90:
        temp -= ord(item[-1]) - 64
    elif 97 <= ord(item[-1]) <= 122:
        temp += ord(item[-1]) - 96

    totals += temp

print(f"{totals:.2f}")
