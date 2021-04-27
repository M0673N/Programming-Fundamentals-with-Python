message = input().split()
result_list = []
for i in message:
    digit = ""
    word = []
    for j in i:
        if j.isdigit():
            digit += j
        else:
            word.append(j)
    word[0], word[-1] = word[-1], word[0]
    word = "".join(word)
    result = chr(int(digit)) + word
    result_list.append(result)
print(" ".join(result_list))
