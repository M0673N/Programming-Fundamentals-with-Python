data = {}
while True:
    command = input()
    if command == "End":
        break
    company, employee = command.split(" -> ")
    if company not in data:
        data[company] = [employee]
    else:
        if employee not in data[company]:
            data[company].append(employee)

data = dict(sorted(data.items()))

for company in data:
    print(company)
    for employee in data[company]:
        print(f"-- {employee}")
