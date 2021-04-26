factor = int(input())
count = int(input())
result = []
previous = 0
for num in range(count):
    result.append(factor + previous)
    previous += factor
print(result)
