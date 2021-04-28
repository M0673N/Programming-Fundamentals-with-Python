list_of_items = input().split("!")
command = input()
while not command == "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent":
        if command[1] not in list_of_items:
            list_of_items.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in list_of_items:
            list_of_items.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in list_of_items:
            list_of_items = [command[2] if i == command[1] else i for i in list_of_items]
    elif command[0] == "Rearrange":
        if command[1] in list_of_items:
            list_of_items.remove(command[1])
            list_of_items.append(command[1])
    command = input()
print(", ".join(list_of_items))
