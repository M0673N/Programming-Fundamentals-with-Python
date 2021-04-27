data = input().split(", ")
data = [int(el) for el in data]
x = 10
result = []
while len(data) > 0:
    for i in range(len(data)):
        if 0 <= data[i] <= x:
            result.append(data[i])
            data[i] = -1
    print(f"Group of {x}'s: {result}")
    data = [el for el in data if not el == -1]
    result.clear()
    x += 10
