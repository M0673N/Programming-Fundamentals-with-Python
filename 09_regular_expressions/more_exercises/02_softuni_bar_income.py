import re

pattern = r"%([A-Z][a-z]+)%([^\|\$\.]+)?<(\w+)>([^\|\$\.]+)?\|([0-9]+)\|([^\|\$\.0-9]+)?(\d+(\.\d+)?)\$"

command = input()
info = {}
total_income = 0
while not command == "end of shift":
    command = re.findall(pattern, command)
    if command:
        name = command[0][0]
        product = command[0][2]
        quantity = int(command[0][4])
        price = float(command[0][6])
        info[name] = [product, quantity * price]
        total_income += quantity*price
        print(f"{name}: {product} - {quantity * price:.2f}")
    command = input()

print(f"Total income: {total_income:.2f}")
