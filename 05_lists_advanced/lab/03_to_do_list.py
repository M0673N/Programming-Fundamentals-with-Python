command = input()
result = [0] * 11
while not command == "End":
    command = command.split("-")
    result.insert(int(command[0]), command[1])
    result.pop(int(command[0]) + 1)
    command = input()
result = [i for i in result if not i == 0]
print(result)
