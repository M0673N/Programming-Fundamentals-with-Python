n = int(input())
cars = {}
for i in range(n):
    info = input().split("|")
    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])
    cars[car] = [mileage, fuel]

command = input()
while not command == "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][1] -= fuel
            cars[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                cars.pop(car)
    elif command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if cars[car][1] + fuel <= 75:
            cars[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            print(f"{car} refueled with {75 - cars[car][1]} liters")
            cars[car][1] = 75
    elif command[0] == "Revert":
        car = command[1]
        km = int(command[2])
        if cars[car][0] - km >= 10000:
            cars[car][0] -= km
            print(f"{car} mileage decreased by {km} kilometers")
        else:
            cars[car][0] = 10000
    command = input()
cars = dict(sorted(cars.items(), key=lambda x: (-x[1][0], x[0])))
for car in cars:
    print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")
