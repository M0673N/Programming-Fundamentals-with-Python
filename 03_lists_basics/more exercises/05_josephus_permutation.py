circle = [int(i) for i in input().split()]
step = int(input())
result = []
index = -1
counter = 0
while circle.count("x") < len(circle):
    index += 1
    if index == len(circle):
        index = 0
    if circle[index] == "x":
        continue
    counter += 1
    if counter % step == 0 and not counter == 0:
        result.append(circle[index])
        circle[index] = "x"
result = [str(i) for i in result]
print("[" + ",".join(result) + "]")
