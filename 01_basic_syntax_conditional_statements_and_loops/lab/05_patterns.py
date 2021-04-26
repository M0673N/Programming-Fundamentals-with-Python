num = int(input())
for i in range(num):
    for j in range(i + 1):
        print("*", end="")
    print()
for k in range(num - 1, -1, -1):
    for l in range(k - 1, -1, -1):
        print("*", end="")
    print()
