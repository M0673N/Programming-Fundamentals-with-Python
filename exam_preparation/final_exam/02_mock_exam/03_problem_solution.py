n = int(input())
plants = {}
for i in range(n):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])
    plants[plant] = [rarity, []]

command = input()
while not command == "Exhibition":
    command = command.split()
    if command[0] == "Rate:":
        plant = command[1]
        if plant not in plants:
            print("error")
        else:
            rating = int(command[3])
            plants[plant][1].append(rating)
    elif command[0] == "Update:":
        plant = command[1]
        if plant not in plants:
            print("error")
        else:
            rarity = int(command[3])
            plants[plant][0] = rarity
    elif command[0] == "Reset:":
        plant = command[1]
        if plant not in plants:
            print("error")
        else:
            plants[plant][1].clear()
    else:
        print("error")
    command = input()

plants = dict(sorted(plants.items(), key=lambda x: (-x[1][0], -sum(x[1][1]))))
print("Plants for the exhibition:")
for plant in plants:
    if len(plants[plant][1]) == 0:
        print(f"- {plant}; Rarity: {plants[plant][0]}; Rating: 0.00")
    else:
        print(f"- {plant}; Rarity: {plants[plant][0]}; Rating: {sum(plants[plant][1]) / len(plants[plant][1]):.2f}")
