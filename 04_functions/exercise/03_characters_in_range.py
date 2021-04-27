def weird_function(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


char1 = input()
char2 = input()
weird_function(char1, char2)
