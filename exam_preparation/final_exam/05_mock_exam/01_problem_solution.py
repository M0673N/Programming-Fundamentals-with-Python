key = input()
command = input()
while not command == "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        action = command[1]
        start = int(command[2])
        end = int(command[3])
        if action == "Upper":
            key = key[:start] + key[start:end].upper() + key[end:]
        elif action == "Lower":
            key = key[:start] + key[start:end].lower() + key[end:]
        print(key)
    elif command[0] == "Slice":
        start = int(command[1])
        end = int(command[2])
        key = key[:start] + key[end:]
        print(key)
    command = input()

print(f"Your activation key is: {key}")
