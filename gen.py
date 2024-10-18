import random

print("Beginner level password generator")

Sparrow = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?0123456789'

number = int(input("How many passwords do you need? "))

length = int(input("What length of password do you need? "))

print('Here are your passwords! ')

for oraimo in range(number):
    password=''
    for dan in range(length):
        password+=random.choice(Sparrow)
        pass
    print(password)