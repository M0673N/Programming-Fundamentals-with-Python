from sys import maxsize


def exchange(index):
    array = data[index + 1:] + data[:index + 1]
    return array


def max_even():
    max_num = -maxsize
    max_num_index = -1
    for index in range(len(data)):
        if data[index] >= max_num and data[index] % 2 == 0:
            max_num = data[index]
            max_num_index = index
    return max_num_index


def max_odd():
    max_num = -maxsize
    max_num_index = -1
    for index in range(len(data)):
        if data[index] >= max_num and data[index] % 2 == 1:
            max_num = data[index]
            max_num_index = index
    return max_num_index


def min_even():
    min_num = maxsize
    min_num_index = -1
    for index in range(len(data)):
        if data[index] <= min_num and data[index] % 2 == 0:
            min_num = data[index]
            min_num_index = index
    return min_num_index


def min_odd():
    min_num = maxsize
    min_num_index = -1
    for index in range(len(data)):
        if data[index] <= min_num and data[index] % 2 == 1:
            min_num = data[index]
            min_num_index = index
    return min_num_index


def first(count, kind):
    temp_list = []
    counter = 0
    if kind == "even":
        for num in data:
            if count == counter:
                break
            if num % 2 == 0:
                temp_list.append(num)
                counter += 1
    else:
        for num in data:
            if count == counter:
                break
            if num % 2 == 1:
                temp_list.append(num)
                counter += 1
    return temp_list


def last(count, kind):
    temp_list = []
    counter = 0
    if kind == "even":
        for num in reversed(data):
            if count == counter:
                break
            if num % 2 == 0:
                temp_list.append(num)
                counter += 1
    else:
        for num in reversed(data):
            if count == counter:
                break
            if num % 2 == 1:
                temp_list.append(num)
                counter += 1
    temp_list.reverse()
    return temp_list


data = list(map(int, input().split()))
command = input()
while not command == "end":
    command_as_list = command.split()
    if command_as_list[0] == "exchange":
        if 0 <= int(command_as_list[1]) < len(data):
            data = exchange(int(command_as_list[1]))
        else:
            print("Invalid index")
    elif command_as_list[0] == "max":
        if command_as_list[1] == "even" and max_even() != -1:
            print(max_even())
        elif command_as_list[1] == "odd" and max_odd() != -1:
            print(max_odd())
        else:
            print("No matches")
    elif command_as_list[0] == "min":
        if command_as_list[1] == "even" and min_even() != -1:
            print(min_even())
        elif command_as_list[1] == "odd" and min_odd() != -1:
            print(min_odd())
        else:
            print("No matches")
    elif command_as_list[0] == "first":
        if int(command_as_list[1]) > len(data):
            print("Invalid count")
        else:
            print(first(int(command_as_list[1]), command_as_list[2]))
    elif command_as_list[0] == "last":
        if int(command_as_list[1]) > len(data):
            print("Invalid count")
        else:
            print(last(int(command_as_list[1]), command_as_list[2]))
    command = input()

print(data)
