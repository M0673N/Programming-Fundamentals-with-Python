import re

string = input()
pattern = r"(=|/)([A-Z][A-Za-z][A-Za-z]+)\1"

destinations = re.findall(pattern, string)
destinations_ready = [i[1] for i in destinations]
score = 0
for destination in destinations_ready:
    score += len(destination)
print(f"Destinations: {', '.join(destinations_ready)}")
print(f"Travel Points: {score}")
