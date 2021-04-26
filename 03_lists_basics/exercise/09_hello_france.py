data = input().split("|")
budget = float(input())
temp_budget = 0
temp_budget += budget
inventory = []
for item in range(len(data)):
    data[item] = data[item].split("->")

for item in range(len(data)):

    if data[item][0] == "Clothes":
        if float(data[item][1]) <= 50:
            if budget >= float(data[item][1]):
                budget -= float(data[item][1])
                inventory.append(data[item])
    elif data[item][0] == "Shoes":
        if float(data[item][1]) <= 35:
            if budget >= float(data[item][1]):
                budget -= float(data[item][1])
                inventory.append(data[item])
    elif data[item][0] == "Accessories":
        if float(data[item][1]) <= 20.50:
            if budget >= float(data[item][1]):
                budget -= float(data[item][1])
                inventory.append(data[item])

for item in range(len(inventory)):
    inventory[item][1] = float(inventory[item][1]) * 1.4
profit = 0
for item in range(len(inventory)):
    profit += inventory[item][1]
    print(f"{inventory[item][1]:.2f}", end=" ")
print()
print(f"Profit: {profit + budget - temp_budget:.2f}")
if profit + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
