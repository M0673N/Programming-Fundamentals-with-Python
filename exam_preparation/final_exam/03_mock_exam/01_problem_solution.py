message = input()
command = input()
while not command == "Reveal":
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        half1 = message[:index]
        half2 = message[index:]
        message = half1 + " " + half2
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += "".join(list(reversed(substring)))
        else:
            print("error")
            command = input()
            continue
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in message:
            message = message.replace(substring, replacement)
    print(message)
    command = input()
print(f"You have a new text message: {message}")
