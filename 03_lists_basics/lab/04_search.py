n = int(input())
word = input()
data = []
for i in range(n):
    data.append(input())
print(data)
data_2 = []
for item in data:
    if word in item:
        data_2.append(item)
print(data_2)
