targets = [int(target) for target in input().split()]
command = input()
shot = 0
while not command == "End":
    command = int(command)
    if 0 <= command < len(targets):
        value = targets[command]
        targets[command] = -1
        shot += 1
        for i in range(len(targets)):
            if targets[i] > value and not targets[i] == -1:
                targets[i] -= value
            elif targets[i] <= value and not targets[i] == -1:
                targets[i] += value
    command = input()

targets = [str(target) for target in targets]
print(f"Shot targets: {shot} -> {' '.join(targets)}")
