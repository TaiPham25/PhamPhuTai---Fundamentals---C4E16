
print ('Guess your number game')
print ('Now think of a number from 0 to 100, then press " Enter"')
input()
print("""
All you have to do is to asnwer to my guess
'c' if my guess is 'C'orrect
'l' if my guess is 'L'arge than your number
's' if my guess is 'S'mall than your number
""")

#string formatting
from random import randint
# n = randint(0,100)

high = 100
low = 0
while True:
    mid = (low + high) // 2
    answer = input("Is {0} your number? ".format(mid)).lower()

    if answer == 'c':
        print("'C'orrect")
        break
    elif answer == 's':
        low = mid
        print("'S'maller than your number")
    elif answer == 'l':
        high = mid
        print("'L'arge than you number")
    else:
        print('zzzz')
