import re

pattern = r">>([A-Za-z]+)<<(\d+\.\d+|\d+)!(\d+)"

list_of_bought_things = []
totals = 0
command = input()
while not command == "Purchase":
    result = re.findall(pattern, command)
    if result:
        item = result[0][0]
        price = float(result[0][1])
        quantity = int(result[0][2])
        list_of_bought_things.append(item)
        totals += price * quantity
    command = input()

print("Bought furniture:")
for item in list_of_bought_things:
    print(item)
print(f"Total money spend: {totals:.2f}")
