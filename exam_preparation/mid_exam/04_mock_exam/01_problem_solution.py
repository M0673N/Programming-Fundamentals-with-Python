people_per_hour_employee1 = int(input())
people_per_hour_employee2 = int(input())
people_per_hour_employee3 = int(input())
people_count = int(input())
hour_counter = 0
while people_count > 0:
    if (hour_counter + 1) % 4 == 0 and hour_counter != 0:
        hour_counter += 1
        continue
    people_count -= people_per_hour_employee3 + people_per_hour_employee2 + people_per_hour_employee1
    hour_counter += 1
print(f"Time needed: {hour_counter}h.")
