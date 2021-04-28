data = input()
result = []
for index in range(len(data)):
    if data[index] == ":":
        result.append(data[index] + data[index + 1])

for item in result:
    print(item)
