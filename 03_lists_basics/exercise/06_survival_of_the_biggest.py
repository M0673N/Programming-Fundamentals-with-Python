data = input().split(" ")
n = int(input())
for item in range(len(data)):
    data[item] = int(data[item])
for i in range(n):
    data.remove(min(data))
print(data)
