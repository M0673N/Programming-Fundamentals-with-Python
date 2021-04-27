def loading_bar(num):
    result = "[..........]"
    result_list = list(result)
    for percent in range(1, int(num / 10 + 1)):
        result_list[percent] = "%"
    result_list = "".join(result_list)
    if num == 100:
        print(f"100% Complete!")
        print(f"{result_list}")
    else:
        print(f"{num}% {result_list}")
        print(f"Still loading...")


num = int(input())

loading_bar(num)
