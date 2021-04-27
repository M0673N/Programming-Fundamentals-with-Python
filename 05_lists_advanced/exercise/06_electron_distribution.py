electrons = int(input())
counter = 1
result = []
while electrons > 0:
    if electrons - 2 * counter ** 2 >= 0:
        result.append(2 * counter ** 2)
        electrons -= 2 * counter ** 2
        counter += 1
    else:
        result.append(electrons)
        break
print(result)
