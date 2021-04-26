data = [int(i) for i in input().split()]
route_1 = data[:len(data) // 2]
route_2 = data[len(data) // 2 + 1:]
route_2.reverse()
total_time_route_1 = 0
total_time_route_2 = 0
for i in route_1:
    if i == 0:
        total_time_route_1 *= 0.8
    else:
        total_time_route_1 += i
for i in route_2:
    if i == 0:
        total_time_route_2 *= 0.8
    else:
        total_time_route_2 += i
if total_time_route_1 < total_time_route_2:
    print(f"The winner is left with total time: {total_time_route_1:.1f}")
else:
    print(f"The winner is right with total time: {total_time_route_2:.1f}")
