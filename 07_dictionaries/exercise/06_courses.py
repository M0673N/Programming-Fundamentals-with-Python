courses = {}
while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)

courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for course in courses:
    print(f"{course}: {len(courses[course])}")
    courses[course] = sorted(courses[course])
    for student in courses[course]:
        print(f"-- {student}")
