array = [int(i) for i in input().split()]
command = input()
while not command == "end":
    command = command.split()
    if command[0] == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]
    elif command[0] == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        array[index_1] = array[index_1] * array[index_2]
    elif command[0] == "decrease":
        array = [i - 1 for i in array]
    command = input()

array = [str(i) for i in array]
print(", ".join(array))
