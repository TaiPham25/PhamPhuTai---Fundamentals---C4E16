#tach cau thanh tung chu
# print('champion'.split(''))

#tach chu
# character = list("champion")
# print(character)

#random lay ra 1 ki tu
from random import choice
character = list("champion")
print(character)
random_char = choice(character)
print(random_char)

answer = input('Your answer: ')
if answer == champion:
    print('good job')
else:
    print('lame')
