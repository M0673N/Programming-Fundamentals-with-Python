def transform(string, repetitions):
    result = ""
    for i in range(repetitions):
        result += string
    return result


string = input()
repetitions = int(input())

print(transform(string, repetitions))
