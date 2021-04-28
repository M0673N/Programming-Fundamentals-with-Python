health = 100
bitcoins = 0
dungeon_rooms = input().split("|")
failed = False
room_counter = 0
for room in dungeon_rooms:
    command, number = room.split()
    if command == "potion":
        health += int(number)
        if health > 100:
            to_subtract = health - 100
            health = 100
            n2 = int(number) - to_subtract
            print(f"You healed for {n2} hp.")
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {int(number)} hp.")
            print(f"Current health: {health} hp.")
        room_counter += 1
    elif command == "chest":
        print(f"You found {int(number)} bitcoins.")
        bitcoins += int(number)
        room_counter += 1
    else:
        health -= int(number)
        if health > 0:
            print(f"You slayed {command}.")
            room_counter += 1
        else:
            room_counter += 1
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            failed = True
            break
if not failed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
