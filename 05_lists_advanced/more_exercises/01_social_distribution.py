people = [int(i) for i in input().split(", ")]
min_wealth = int(input())
if sum(people) < min_wealth * len(people):
    print("No equal distribution possible")
    exit(0)
else:
    while people[people.index(min(people))] < min_wealth:
        people[people.index(max(people))] -= min_wealth - people[people.index(min(people))]
        people[people.index(min(people))] += min_wealth - people[people.index(min(people))]

print(people)
