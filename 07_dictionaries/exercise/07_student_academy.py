n = int(input())
data = {}
for _ in range(n):
    student = input()
    grade = float(input())
    if student not in data:
        data[student] = [grade]
    else:
        data[student].append(grade)

good_students = {}
for student in data:
    data[student] = sum(data[student]) / len(data[student])
    if data[student] >= 4.5:
        good_students[student] = data[student]

good_students = dict(sorted(good_students.items(), key=lambda x: -x[1]))
for name, grade in good_students.items():
    print(f"{name} -> {grade:.2f}")
