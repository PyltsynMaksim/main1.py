import random
number = 'abcdefghijklmnopqrstuvwz1234567890'
question = int(input('pass length'))


password = ''

for i in range(question):
    password += random.choice(number)


print(password)
