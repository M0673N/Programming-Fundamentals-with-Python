people = int(input())
lift = [int(i) for i in input().split()]
wagon_number = 0
while True:
    if lift[wagon_number] == 4:
        wagon_number += 1
        if wagon_number == len(lift) and people != 0:
            print(f"There isn't enough space! {people} people in a queue!")
            lift = [str(i) for i in lift]
            print(f"{' '.join(lift)}")
            break
        elif wagon_number == len(lift) and people == 0:
            lift = [str(i) for i in lift]
            print(f"{' '.join(lift)}")
            break
        continue
    if people > 0:
        lift[wagon_number] += 1
        people -= 1
    elif people == 0:
        print("The lift has empty spots!")
        lift = [str(i) for i in lift]
        print(f"{' '.join(lift)}")
        break
