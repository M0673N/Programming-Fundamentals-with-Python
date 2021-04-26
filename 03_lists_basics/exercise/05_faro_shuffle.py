data = input().split(" ")
times = int(input())
for shuffle in range(times):
    data1 = data[:int(len(data) / 2)]
    data2 = data[int(len(data) / 2):]
    data.clear()
    while len(data2) > 0:
        data.append(data1[0])
        data1.pop(0)
        data.append(data2[0])
        data2.pop(0)
print(data)
