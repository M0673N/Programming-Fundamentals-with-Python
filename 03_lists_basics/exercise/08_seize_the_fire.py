data = input().split("#")
water = int(input())
effort = 0
fire = 0
for item in range(len(data)):
    data[item] = data[item].split(" = ")
print("Cells:")
for item in range(len(data)):
    cell_put_out = False
    if data[item][0] == "High" and 81 <= int(data[item][1]) <= 125 and water >= int(data[item][1]):
        cell_put_out = True
    elif data[item][0] == "Medium" and 51 <= int(data[item][1]) <= 80 and water >= int(data[item][1]):
        cell_put_out = True
    elif data[item][0] == "Low" and 1 <= int(data[item][1]) <= 50 and water >= int(data[item][1]):
        cell_put_out = True
    if cell_put_out:
        water -= int(data[item][1])
        effort += int(data[item][1]) * 0.25
        fire += int(data[item][1])
        print(f"- {data[item][1]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")
