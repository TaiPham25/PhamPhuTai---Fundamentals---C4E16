Favorite = [ 'death note', 'netflix', 'teaching']

# print(*Favorite, sep=', ') #pythonic
#
# them = input('something else: ')
# Favorite.append(them)
#
# print(*Favorite, sep=', ') #pythonic

# #length
# print(len(Favorite))
# print(Favorite[1])


# for i in range(len(Favorite)):
#     print(i + 1, '. ',  Favorite[i], sep='')


# print('*' *20)
# for index, item in enumerate(Favorite):
#     print(index + 1, '. ',  item, sep='')
# print('*' *20)



# for item in Favorite:
#     print(item)
# print('*' *20)


for index, fav in enumerate(Favorite):
    print(index + 1,', ', fav, sep='')

position =int(input('Vi tri ban muon thay doi: '))

Favorite[n] = input('thay la gi: ')
print(*Favorite, sep=', ')

for index, favin enumerate(Favorite):
    print(index + 1, ' ')
