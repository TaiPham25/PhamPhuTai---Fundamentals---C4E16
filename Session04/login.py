print('Hi there, this is a superuser gateway')
count = 0
while True:
    write = input('Username: ')

    if write != 'c4e':
        print('Not')
    else:
        password = input('password: ')
        if password != 'c4e16':
            print('incorrect')
        else:
            print('welcome', write)
            break
    count += 1
    if count == 3:
        print('failed 3 time')
        break
