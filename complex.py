import random
import string

print("Beginner level password generator")


number = int(input("How many passwords do you need? "))

length = int(input("What length of password do you need? "))

print('Here are your passwords! ')

for oraimo in range(number):
    password=''
    for dan in range(length):
        password+=random.choice(string.ascii_letters + string.digits + string.punctuation)
        pass
    print(password)