s = input('Enter a sequence of number, separated by space: ')
#strip cut spaces at start/end of string

words = s.strip().split(' ')
numbers =[]

for word in words:
    numbers.append(int(word))

print(numbers)

is_sorted = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print('you sequence is already sorted')
else:
    print('you sequence is not already sorted')

    sort =[]
    while True:
        min_numbers = min(numbers)
        sort.append(min_numbers)
        numb.remove(min_number)

        if len(numbers) == 0:
            break
    print(*sort)
