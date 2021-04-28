def check_matches(symbol, ticket):
    symbol = symbol
    ticket = ticket
    result = ""
    for char in ticket:
        if char == symbol:
            result += symbol
        else:
            result += "X"
    result = sorted(result.split("X"), reverse=True)
    matches = len(result[0])
    return matches


def check_symbols(symbol, first_half, second_half):
    symbol = symbol
    first_half = first_half
    second_half = second_half
    first_matches = check_matches(symbol, first_half)
    second_matches = check_matches(symbol, second_half)
    if first_matches == second_matches and 10 > first_matches >= 6:
        print(f'ticket "{ticket}" - {first_matches}{symbol}')
        return True
    elif first_matches > second_matches and 10 > second_matches >= 6:
        print(f'ticket "{ticket}" - {second_matches}{symbol}')
        return True
    elif first_matches < second_matches and 10 > first_matches >= 6:
        print(f'ticket "{ticket}" - {first_matches}{symbol}')
        return True

    elif first_matches == second_matches == 10:
        print(f'ticket "{ticket}" - {first_matches}{symbol} Jackpot!')
        return True

    else:
        global no_matches
        no_matches = True
        return False


data = input()
data = data.replace(" ", "")
data = data.split(",")
valid = False
no_matches = False
won = False
for ticket in data:
    if len(ticket) == 20:
        valid = True
    else:
        print("invalid ticket")
        continue

    if valid:
        first_half = ticket[:int(len(ticket) / 2)]
        second_half = ticket[int(len(ticket) / 2):]
        if "@" in ticket:
            won = check_symbols("@", first_half, second_half)
        if "#" in ticket:
            won = check_symbols("#", first_half, second_half)
        if "$" in ticket:
            won = check_symbols("$", first_half, second_half)
        if "^" in ticket:
            won = check_symbols("^", first_half, second_half)
        if "@" not in ticket and "#" not in ticket and "$" not in ticket and "^" not in ticket:
            print(f'ticket "{ticket}" - no match')
        if no_matches and not won:
            print(f'ticket "{ticket}" - no match')
            no_matches = False
