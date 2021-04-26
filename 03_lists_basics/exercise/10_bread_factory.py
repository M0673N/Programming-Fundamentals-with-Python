data = input().split("|")
energy = 100
coins = 100

for i in range(len(data)):
    data[i] = data[i].split("-")

for i in range(len(data)):

    if data[i][0] == "rest":
        if energy + float(data[i][1]) <= 100:
            energy += float(data[i][1])
            print(f"You gained {float(data[i][1]):.0f} energy.")
            print(f"Current energy: {energy:.0f}.")
        else:
            energy += float(data[i][1]) - 100
            jump = energy
            energy = 100
            print(f"You gained {float(data[i][1]) - jump:.0f} energy.")
            print(f"Current energy: {energy:.0f}.")

    elif data[i][0] == "order":
        if energy >= 30:
            coins += float(data[i][1])
            energy -= 30
            print(f"You earned {data[i][1]} coins.")
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if coins > float(data[i][1]):
            coins -= float(data[i][1])
            print(f"You bought {data[i][0]}.")
        else:
            print(f"Closed! Cannot afford {data[i][0]}.")
            break
else:
    print(f"Day completed!")
    print(f"Coins: {coins:.0f}")
    print(f"Energy: {energy:.0f}")
