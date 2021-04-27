data = input()
digits = [int(i) for i in data if i.isdigit()]
data = [i for i in data if not i.isdigit()]
take = []
skip = []
result = ""
for i in range(len(digits)):
    if i % 2 == 1:
        skip.append(digits[i])
        continue
    take.append(digits[i])
counter = 0
while len(skip) > 0:
    for i in range(take[0]):
        if counter >= len(data):
            break
        result += data[counter]
        counter += 1
    for i in range(skip[0]):
        counter += 1
    take.pop(0)
    skip.pop(0)
print(result)
