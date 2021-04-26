data = input().split(" ")
command = input()
while command != "No Money":
    command = command.split(" ")
    if command[0] == "OutOfStock":
        for item in range(len(data)):
            if data[item] == command[1]:
                data[item] = None
    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(data):
            data[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        data[-1] = command[1]
    command = input()
while None in data:
    data.remove(None)
print(" ".join(data))
