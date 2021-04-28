sequence = input().split()
command = input()
moves = 0
won = False
while not command == "end":
    command = command.split()
    moves += 1
    if int(command[0]) != int(command[1]) and int(command[0]) >= 0 and int(command[1]) >= 0 and int(command[0]) < len(
            sequence) and int(command[1]) < len(sequence):
        if sequence[int(command[0])] == sequence[int(command[1])]:
            to_be_removed = sequence[int(command[0])]
            sequence.remove(to_be_removed)
            sequence.remove(to_be_removed)
            print(f"Congrats! You have found matching elements - {to_be_removed}!")
            if len(sequence) == 0:
                print(f"You have won in {moves} turns!")
                won = True
                break
        elif sequence[int(command[0])] != sequence[int(command[1])]:
            print("Try again!")
    else:
        sequence1 = sequence[:(len(sequence) // 2)]
        sequence2 = sequence[(len(sequence) // 2):]
        sequence1.append("-" + str(moves) + "a")
        sequence1.append("-" + str(moves) + "a")
        sequence = sequence1 + sequence2
        print("Invalid input! Adding additional elements to the board")
    command = input()
if len(sequence) != 0 and not won:
    print("Sorry you lose :(")
    print(f"{' '.join(sequence)}")
