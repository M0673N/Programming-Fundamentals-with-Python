def perfect_number_check(num):
    total = 0
    for i in range(2, num):
        if num % i == 0:
            total += i
    if total + 1 == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())

perfect_number_check(num)
