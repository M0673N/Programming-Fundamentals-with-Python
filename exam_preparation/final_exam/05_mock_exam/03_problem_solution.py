command = input()
map_of_the_seas = {}
while not command == "Sail":
    city, population, gold = command.split("||")
    if city not in map_of_the_seas:
        map_of_the_seas[city] = [int(population), int(gold)]
    else:
        map_of_the_seas[city][0] += int(population)
        map_of_the_seas[city][1] += int(gold)
    command = input()

command_2 = input()
while not command_2 == "End":
    command_2 = command_2.split("=>")
    if command_2[0] == "Plunder":
        city = command_2[1]
        people = int(command_2[2])
        gold = int(command_2[3])
        map_of_the_seas[city][0] -= people
        map_of_the_seas[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if map_of_the_seas[city][0] <= 0 or map_of_the_seas[city][1] <= 0:
            print(f"{city} has been wiped off the map!")
            map_of_the_seas.pop(city)
    elif command_2[0] == "Prosper":
        city = command_2[1]
        gold = int(command_2[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            map_of_the_seas[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {map_of_the_seas[city][1]} gold.")
    command_2 = input()

if len(map_of_the_seas) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    map_of_the_seas = dict(sorted(map_of_the_seas.items(), key=lambda x: (-x[1][1], x[0])))
    print(f"Ahoy, Captain! There are {len(map_of_the_seas)} wealthy settlements to go to:")
    for city in map_of_the_seas:
        print(f"{city} -> Population: {map_of_the_seas[city][0]} citizens, Gold: {map_of_the_seas[city][1]} kg")
