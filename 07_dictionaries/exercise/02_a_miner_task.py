data = {}
while True:
    recourse = input()
    if recourse == "stop":
        break
    amount = int(input())
    if recourse not in data:
        data[recourse] = amount
    else:
        data[recourse] += amount

for rec, am in data.items():
    print(f"{rec} -> {am}")
