command = input()
total = 0
while not command == "special" and not command == "regular":
    if float(command) >= 0:
        total += float(command)
    else:
        print("Invalid price!")
    command = input()
total_plus_tax = total * 1.2
tax = total * 0.2
if total_plus_tax == 0:
    print("Invalid order!")
else:
    if command == "special":
        total_plus_tax *= 0.9
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {tax:.2f}$")
        print(f"-----------")
        print(f"Total price: {total_plus_tax:.2f}$")
    elif command == "regular":
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {tax:.2f}$")
        print(f"-----------")
        print(f"Total price: {total_plus_tax:.2f}$")
