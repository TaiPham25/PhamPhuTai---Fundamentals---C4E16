shopping = True
while shopping:
    choice = input('Welcome to our shop, what do you want (C, R, U, D)?  ')
    choice = choice.upper()
    if choice == 'R':
        shop = ['T-shirt' ,'Sweater']
        print('Our items:',*shop, sep=', ')
        break
    elif choice == 'C':
        shop = ['T-shirt' ,'Sweater']
        add = input('Enter new item: ')
        shop.append(add)
        print('Our items:', *shop, sep=', ')
        break
    elif choice == 'U':
        shop = ['T-shirt' ,'Sweater']
        print('Our items: ', *shop, sep=',')
        position = int(input('position u want update: '))
        new = input('New item: ')
        shop[position - 1] = new
        add = ('Jeans')
        shop.append(add)
        print('Our items: ', *shop, sep=',')
        break
    elif choice == 'D':
        shop = ['T-shirt' ,'Skirt' , 'Sweater']

        print('Our items: ', *shop, sep=',')
        delete = int(input('position u want delete: '))
        delete = len(shop)
        del shop[delete - 1]
        print('Our items: ', *shop, sep=',')
        break
    else:
        print('Wrong choice,again!')
