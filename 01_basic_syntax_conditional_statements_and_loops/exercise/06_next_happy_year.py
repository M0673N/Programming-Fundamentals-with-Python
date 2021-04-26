year = int(input())
year += 1
while True:
    year = str(year)
    if len(year) == len(set(year)):
        print(year)
        break
    year = int(year) + 1
