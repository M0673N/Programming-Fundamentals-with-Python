employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students = int(input())
hours = 0
counter = 0
while students > 0:
    if counter % 3 == 0 and not counter == 0:
        hours += 1
    students -= employee_1 + employee_3 + employee_2
    hours += 1
    counter += 1
print(f"Time needed: {hours}h.")
