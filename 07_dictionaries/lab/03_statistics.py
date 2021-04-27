to_be_dict = input().split(": ")
dictionary = {}
for i in range(0, len(to_be_dict), 2):
    key = to_be_dict[i]
    value = to_be_dict[i + 1]
    dictionary[key] = int(value)

command = input()
while not command == "statistics":
    new_key, new_value = command.split(": ")
    if new_key not in dictionary:
        dictionary[new_key] = 0
    dictionary[new_key] += int(new_value)
    command = input()
print("Products in stock:")
for i in dictionary:
    print(f"- {i}: {dictionary[i]}")
print(f"Total Products: {len(dictionary)}")
print(f"Total Quantity: {sum(dictionary.values())}")
