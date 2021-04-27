stock_list = input().split()
dict_stock = {}
for i in range(0, len(stock_list), 2):
    key = stock_list[i]
    value = int(stock_list[i + 1])
    dict_stock[key] = value
print(dict_stock)
