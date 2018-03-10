#delete
favs = ['death note', 'netflix', 'teaching']
print('hi,list: ')

for index, fav in enumerate(favs):
    print(index + 1, '. ',  fav, sep='')
position =int(input('Vi tri ban muon xoa: '))
del favs[position - 1]
# favs.pop(position - 1)
for index, fav in enumerate(favs):
    print(index + 1, '. ',  fav, sep='')

# if fav_name_to_delete in favs:
#     fav.remove(fav_name_to_delete)
