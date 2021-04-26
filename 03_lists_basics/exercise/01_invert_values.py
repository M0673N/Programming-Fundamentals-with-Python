string = input()
data = string.split(" ")
result = []
for item in data:
    if int(item) < 0:
        result.append(abs(int(item)))
    else:
        result.append(int(item) - int(item) * 2)
print(result)
