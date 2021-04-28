import re

text = input()
pattern = r"(#|\|)([A-Za-z ]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]+)\1"

food = re.findall(pattern, text)
names = [x[1] for x in food]
date = [x[2] for x in food]
calories = [int(x[3]) for x in food]

print(f"You have food to last you for: {sum(calories) // 2000} days!")
for i in range(len(names)):
    print(f"Item: {names[i]}, Best before: {date[i]}, Nutrition: {calories[i]}")
