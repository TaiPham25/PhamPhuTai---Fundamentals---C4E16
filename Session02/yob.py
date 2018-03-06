yob = int(input(' Your year of bith? '))

age =  2018 - yob

print('age:' , age)

if age < 10:
    print('baby')

elif age <= 18:
    print('teenager')

elif age == 24:
    print('lay chong thoi')

else:
    print('not baby')


print('bye')
