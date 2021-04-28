data = {}
while True:
    command = input()
    if command == "buy":
        break

    item, price, quantity = command.split()

    if item not in data:
        data[item] = [float(price), int(quantity)]
    else:
        data[item][0] = float(price)
        data[item][1] += int(quantity)

for item in data:
    print(f"{item} -> {data[item][0] * data[item][1]:.2f}")
