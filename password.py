import random

characters = 'abcdefghijklmnoprstuwvxyz'
numbers = '1234567890'
special = "._"

characters += numbers + special

length = int(input("Password length"))
password = ''

for _ in range(length):
    password += random.choice(characters)
print(password)