def password_validator(password):
    length = 0
    digits = 0
    flag = False
    x = True
    for char in password:
        length += 1
        if ord(char) in range(48, 58):
            digits += 1
        if not ord(char) in range(97, 123) and not ord(char) in range(65, 91) and not ord(char) in range(48, 58):
            flag = True
    if not 6 <= length <= 10:
        print("Password must be between 6 and 10 characters")
        x = False
    if flag:
        print("Password must consist only of letters and digits")
        x = False
    if digits < 2:
        print("Password must have at least 2 digits")
        x = False
    if x:
        print("Password is valid")


password = input()

password_validator(password)
