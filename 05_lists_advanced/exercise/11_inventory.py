data = input().split(", ")
command = input()
while not command == "Craft!":
    command = command.split(" - ")
    if command[0] == "Collect":
        if not command[1] in data:
            data.append(command[1])
    elif command[0] == "Drop":
        if command[1] in data:
            data.remove(command[1])
    elif command[0] == "Combine Items":
        command_2 = command[1].split(":")
        if command_2[0] in data:
            data.insert(data.index(command_2[0]) + 1, command_2[1])
    elif command[0] == "Renew":
        if command[1] in data:
            data.append(command[1])
            data.remove(command[1])
    command = input()
print(", ".join(data))
