budget = float(input())
flour_price = float(input())
eggs = flour_price * 0.75
milk = flour_price * 1.25
cozonac = eggs + flour_price + milk * 0.25
cozonac_count = 0
count_eggs = 0
while budget - cozonac > 0:
    budget -= cozonac
    cozonac_count += 1
    count_eggs += 3
    if cozonac_count % 3 == 0:
        count_eggs -= cozonac_count - 2
print(f"You made {cozonac_count} cozonacs! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")
