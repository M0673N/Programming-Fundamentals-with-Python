text = input()
raw_pass = ""
command = input()
while not command == "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        for i in range(len(text)):
            if i % 2 == 1:
                raw_pass += text[i]
        print(raw_pass)
        text = raw_pass
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        half1 = text[:index]
        half2 = text[index + length:]
        text = half1 + half2
        print(text)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {text}")
