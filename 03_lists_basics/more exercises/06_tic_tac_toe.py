def check_who_won(player):
    if first_line.count(player) == 3:
        return True
    elif second_line.count(player) == 3:
        return True
    elif third_line.count(player) == 3:
        return True
    elif col_1.count(player) == 3:
        return True
    elif col_2.count(player) == 3:
        return True
    elif col_3.count(player) == 3:
        return True
    elif diag_1.count(player) == 3:
        return True
    elif diag_2.count(player) == 3:
        return True
    else:
        return False


first_line = [int(i) for i in input().split()]
second_line = [int(i) for i in input().split()]
third_line = [int(i) for i in input().split()]
col_1 = [first_line[0], second_line[0], third_line[0]]
col_2 = [first_line[1], second_line[1], third_line[1]]
col_3 = [first_line[2], second_line[2], third_line[2]]
diag_1 = [first_line[0], second_line[1], third_line[2]]
diag_2 = [first_line[2], second_line[1], third_line[0]]
pl_1_won = check_who_won(1)
pl_2_won = check_who_won(2)
if pl_1_won:
    print("First player won")
elif pl_2_won:
    print("Second player won")
else:
    print("Draw!")
