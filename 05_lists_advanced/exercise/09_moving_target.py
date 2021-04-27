data = input().split()
data = [int(i) for i in data]
command = input()
while not command == "End":
    command = command.split()
    if command[0] == "Shoot":
        if 0 <= int(command[1]) < len(data):
            data[int(command[1])] -= int(command[2])
            if data[int(command[1])] <= 0:
                data.pop(int(command[1]))
    elif command[0] == "Add":
        if len(data) > int(command[1]) >= 0:
            data.insert(int(command[1]), int(command[2]))
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        if int(command[1]) >= int(command[2]) and int(command[1]) + int(command[2]) - 1 <= len(data) and int(
                command[1]) >= 0:
            data.pop(int(command[1]))
            data1 = data[:int(command[1])]
            for i in range(1, int(command[2]) + 1):
                data1.pop(-i)
            data2 = data[int(command[1]):]
            for i in range(int(command[2])):
                data2.pop(i)
            data = data1 + data2
        else:
            print("Strike missed!")
    command = input()
data = [str(i) for i in data]
print("|".join(data))
