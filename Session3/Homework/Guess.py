# #3a
# from random import choice
# from random import shuffle

playing = True
while playing:
    fun = list('champion')
    shuffle(fun)
    print(*fun, sep=', ')
    write = input('Your answer: ')
    if write == 'champion':
        print('Hura')
        break
    else:
        print('Your aswer: ', write)
        print(':(')

#3b
# from random import choice
# from random import shuffle
# collect =['meticulous', 'champion', 'hexagon']
# count = 0
# while True:
#     word = choice(collect)
#     fun = word
#     character = list(fun)
#     # shuffle(fun)
#     print(*fun, sep=', ')
#     write = input('Your answer: ')
#     if write == fun:
#         print('Hura')
#         break
#     else:
#         count +=1
#         print('Wrong')
#         if count == 3:
#             break
