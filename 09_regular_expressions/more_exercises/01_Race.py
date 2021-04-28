import re

pattern_name = r"[A-Za-z]"
pattern_nums = r"[0-9]"
racers = input().split(", ")
racers_dict = {}
for racer in racers:
    racers_dict[racer] = 0

command = input()
while not command == "end of race":
    name_list = re.findall(pattern_name, command)
    name = "".join(name_list)
    nums = re.findall(pattern_nums, command)
    nums = [int(i) for i in nums]
    nums = sum(nums)
    if name in racers_dict:
        racers_dict[name] += nums
    command = input()

racers_dict = dict(sorted(racers_dict.items(), key=lambda x: -x[1]))
place = 0
for racer in racers_dict:
    place += 1
    if place == 4:
        break
    if place == 1:
        print(f"{place}st place: {racer}")
    elif place == 2:
        print(f"{place}nd place: {racer}")
    else:
        print(f"{place}rd place: {racer}")
