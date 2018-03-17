inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
#add pocket and value of pocket
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

#remove dagger
inventory['backpack'].remove('dagger')

# Add 50 to the number stored under the 'gold' key.
inventory['gold'] += 50
print(inventory)
