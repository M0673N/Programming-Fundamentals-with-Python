lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
shield_counter = 0
cost = 0
for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        cost += helmet
    if fight % 3 == 0:
        cost += sword
        if fight % 2 == 0:
            cost += shield
            shield_counter += 1
            if shield_counter % 2 == 0:
                cost += armor
print(f"Gladiator expenses: {cost:.2f} aureus")
