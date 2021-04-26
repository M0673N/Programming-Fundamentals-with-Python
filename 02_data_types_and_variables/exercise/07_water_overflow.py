n = int(input())
capacity = 0
for i in range(n):
    litres = int(input())
    if capacity + litres > 255:
        print("Insufficient capacity!")
    else:
        capacity += litres
print(capacity)
