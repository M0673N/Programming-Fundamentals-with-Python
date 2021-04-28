neighbourhood = [int(i) for i in input().split("@")]
command = input()
position = 0
while not command == "Love!":
    command = command.split()
    command[1] = int(command[1])
    position += command[1]
    if position >= len(neighbourhood):
        position = 0
    if neighbourhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighbourhood[position] -= 2
        if neighbourhood[position] == 0:
            print(f"Place {position} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {position}.")
neighbourhood = [i for i in neighbourhood if i != 0]
if len(neighbourhood) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighbourhood)} places.")
