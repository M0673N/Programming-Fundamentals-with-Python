n = int(input())
data = {}
for i in range(n):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        plate = command[2]
        if username not in data:
            data[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command[0] == "unregister":
        username = command[1]
        if username in data:
            print(f"{username} unregistered successfully")
            data.pop(username)
        else:
            print(f"ERROR: user {username} not found")

for user, plate in data.items():
    print(f"{user} => {plate}")
