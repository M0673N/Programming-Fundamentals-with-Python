stock_list = input().split()
dict_stock = {}
for i in range(0, len(stock_list), 2):
    key = stock_list[i]
    value = int(stock_list[i + 1])
    dict_stock[key] = value
to_be_searched = input().split()
for i in to_be_searched:
    if i in dict_stock:
        print(f"We have {dict_stock[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")
