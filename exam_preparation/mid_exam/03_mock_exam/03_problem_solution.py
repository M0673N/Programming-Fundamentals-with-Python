targets = [int(target) for target in input().split()]
command = input()
while not command == "End":
    command = command.split()
    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        if 0 <= index - radius < len(targets) and 0 <= index + radius < len(targets):
            first_half = targets[:index - radius]
            second_half = targets[index + radius + 1:]
            targets = first_half + second_half
        else:
            print("Strike missed!")

    command = input()

targets = [str(target) for target in targets]
print("|".join(targets))
