data = input().split("@")
data = [int(i) for i in data]
command = input()
position = 0
while not command == "Love!":
    command = command.split()
    position += int(command[1])
    if position >= len(data):
        position = 0
    if data[position] <= 0:
        print(f"Place {position} already had Valentine's day.")
    elif data[position] - 2 <= 0:
        print(f"Place {position} has Valentine's day.")
    data[position] -= 2
    command = input()
success_check = [i for i in data if not i <= 0]

print(f"Cupid's last position was {position}.")
if len(success_check) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(success_check)} places.")
