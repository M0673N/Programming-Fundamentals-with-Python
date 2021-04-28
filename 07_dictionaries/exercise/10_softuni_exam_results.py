students = {}
subjects = {}
while True:
    command = input()
    if command == "exam finished":
        break
    command = command.split("-")

    if command[1] == "banned":
        if command[0] in students:
            students.pop(command[0])
            continue

    if command[0] not in students:
        students[command[0]] = int(command[2])
        if command[1] not in subjects:
            subjects[command[1]] = 1
        else:
            subjects[command[1]] += 1
    else:
        subjects[command[1]] += 1
        if int(command[2]) > students[command[0]]:
            students[command[0]] = int(command[2])

students = dict(sorted(students.items(), key=lambda x: (-x[1], x[0])))
print("Results:")
for user, score in students.items():
    print(f"{user} | {score}")

subjects = dict(sorted(subjects.items(), key=lambda x: (-x[1], x[0])))
print("Submissions:")
for lang, submissions in subjects.items():
    print(f"{lang} - {submissions}")
