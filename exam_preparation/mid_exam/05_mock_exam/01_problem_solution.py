from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())
max_bonus = 0
max_attendances = 0
for student in range(students):
    attendances = int(input())
    total_bonus = attendances / lectures * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendances = attendances
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")
