data = input().split(", ")
beggars = int(input())
result = []
for beggar in range(beggars):
    result.append(0)
while len(data) > 0:
    for beggar in range(beggars):
        if len(data) > 0:
            result[beggar] += int(data[0])
            data.pop(0)
print(result)
