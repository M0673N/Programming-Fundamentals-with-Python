string = [int(i) for i in input().split(", ")]
counter = 0
for i in range(len(string)):
    if string[i] == 0:
        counter += 1
result = [i for i in string if i != 0]
for i in range(counter):
    result.append(0)
print(result)
