import random

while True:
    symbols =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password_len = int(input("Введите количество символов в пароле: "))
    password = ""

    for i in range(password_len):
        password += random.choice(symbols)
    print(password)
    
