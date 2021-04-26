n = int(input())
data = []
result = []
for i in range(n):
    data.append(int(input()))
command = input()
if command == "even":
    for item in data:
        if item % 2 == 0:
            result.append(item)
elif command == "odd":
    for item in data:
        if item % 2 == 1:
            result.append(item)
elif command == "positive":
    for item in data:
        if item >= 0:
            result.append(item)
elif command == "negative":
    for item in data:
        if item < 0:
            result.append(item)
print(result)
