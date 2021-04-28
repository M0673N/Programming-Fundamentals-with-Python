data = input().split(", ")
command = input()
while not command == "Craft!":
    command = command.split(" - ")
    if command[0] == "Collect":
        if command[1] not in data:
            data.append(command[1])
    elif command[0] == "Drop":
        if command[1] in data:
            data.remove(command[1])
    elif command[0] == "Combine Items":
        old_item, new_item = command[1].split(":")
        if old_item in data:
            data.insert(data.index(old_item) + 1, new_item)
    elif command[0] == "Renew":
        if command[1] in data:
            data.remove(command[1])
            data.append(command[1])

    command = input()

print(", ".join(data))
