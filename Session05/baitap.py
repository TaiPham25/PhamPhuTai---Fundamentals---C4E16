code = {
'hc' : 'hoc',
'ng': 'nguoi',
'pt' : 'phat trien',
'eny': 'em nguoi yeu',
'any': 'anh nguoi yeu'}
while True:
    print(*code, sep='         ')
    key = input('Your code?')


    if key in code:
        print('Translation',':', code[key])
    else:
        print('Not found')
        choice = input('Them(Y/N)').lower()
        if choice == 'y':
            Translation = input('Translation?')
            code[key] = Translation
            print('Update',*code, sep='         ')
            break
        else:
            break



print('* '*20)
