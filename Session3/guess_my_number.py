# from random import randint
#
# # n = randint(0,100)
# n= 71
# count = 0
#
# playing = True
# while playing:
#     a = int(input('Guess a number(0-100)? '))
#
#     if a < n:
#         print('too small')
#     elif a == n:
#         print('bingo')
#         break
#     else:
#         print('to large')
#
#
#     count += 1
#     if count == 7:
#         print('U lose :(')
#         break


n = int(input('Enter a number: '))
count = 0

while True:
    n = n // 10
    count +=1
    if n == 0:
        break

print(count)
