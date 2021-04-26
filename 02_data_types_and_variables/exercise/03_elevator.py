people = int(input())
capacity = int(input())
if people <= capacity:
    print(1)
elif people > capacity and people % capacity == 0:
    print(int(people / capacity))
else:
    print(int(people / capacity + 1))
