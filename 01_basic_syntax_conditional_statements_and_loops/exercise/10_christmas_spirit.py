quantity = int(input())
days_left = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
spirit = 0
price = 0
if days_left % 10 == 0:
    spirit -= 30
for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        price += quantity * ornament_set
        spirit += 5
    if day % 3 == 0:
        price += quantity * tree_skirt + quantity * tree_garlands
        spirit += 13
    if day % 5 == 0:
        price += tree_lights * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        price += tree_skirt + tree_lights + tree_garlands
print(f"Total cost: {price}")
print(f"Total spirit: {spirit}")
