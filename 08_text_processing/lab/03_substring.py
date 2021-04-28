data1 = input()
data2 = input()
while data1 in data2:
    data2 = data2.replace(data1, "")
print(data2)
