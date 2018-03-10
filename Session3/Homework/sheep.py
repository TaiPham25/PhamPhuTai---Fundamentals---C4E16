size = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Tai and these are my ship sizes',':', *size, sep=' ')
max_size = max(size)
print('Now my biggest sheep has size', max_size,"let's shear it")
for index, item in enumerate(size):
    if item == max_size:
        size[index] = 8
print('After shearing, here in my flock', *size, sep=' ')

month = 1
while month < 4:
    for index, item in enumerate(size):
        item += 50
        size[index] = item
    print('MONTH', month)
    print('One month has passed, now here is my flock', *size, sep=' ')
    max_size = max(size)
    print('Now my biggest sheep has size', max_size,"let's shear it")
    for index, item in enumerate(size):
        if item == max_size:
            size[index] = 8
    print('After shearing, here in my flock', *size, sep=' ')
    month +=1
    print
    if month == 4:
        break
