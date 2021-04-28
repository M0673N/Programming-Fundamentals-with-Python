n = int(input())
heroes = {}
for i in range(n):
    command = input().split()
    name = command[0]
    hp = int(command[1])
    mp = int(command[2])
    heroes[name] = [hp, mp]

command = input()
while not command == "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        name = command[1]
        mp = int(command[2])
        spell = command[3]
        if mp <= heroes[name][1]:
            heroes[name][1] -= mp
            print(f"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")
    elif command[0] == "TakeDamage":
        name = command[1]
        dmg = int(command[2])
        attacker = command[3]
        if heroes[name][0] > dmg:
            heroes[name][0] -= dmg
            print(f"{name} was hit for {dmg} HP by {attacker} and now has {heroes[name][0]} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            heroes.pop(name)
    elif command[0] == "Recharge":
        name = command[1]
        amount = int(command[2])
        if heroes[name][1] + amount <= 200:
            print(f"{name} recharged for {amount} MP!")
            heroes[name][1] += amount
        else:
            print(f"{name} recharged for {200 - heroes[name][1]} MP!")
            heroes[name][1] = 200
    elif command[0] == "Heal":
        name = command[1]
        amount = int(command[2])
        if heroes[name][0] + amount <= 100:
            print(f"{name} healed for {amount} HP!")
            heroes[name][0] += amount
        else:
            print(f"{name} healed for {100 - heroes[name][0]} HP!")
            heroes[name][0] = 100

    command = input()

heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))

for hero in heroes:
    print(hero)
    print(f"  HP: {heroes[hero][0]}")
    print(f"  MP: {heroes[hero][1]}")
