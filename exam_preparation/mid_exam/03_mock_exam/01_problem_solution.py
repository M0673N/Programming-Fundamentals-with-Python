energy = int(input())
distance = input()
count = 0
lost = False
while not distance == "End of battle":
    distance = int(distance)
    energy -= distance
    if energy >= 0:
        count += 1
        if count % 3 == 0:
            energy += count

    else:
        energy += distance
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        lost = True
        break

    distance = input()

if not lost:
    print(f"Won battles: {count}. Energy left: {energy}")
