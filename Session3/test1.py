# food1 = 'rau muong'
# food2 = 'ca vien chien'
# food3 = 'pho'
# food4 = 'suon xao chua ngot'
# food5 = 'rau'

menu = ['rau muong',
        'ca vien chien',
        'pho',
        'suon xao chua ngot',
        'rau'
        ]
# separator ngan cach
print(*menu, sep=', ') #pythonic

menu.append('bun cha, ')

print(*menu, sep=', ') #pythonics
