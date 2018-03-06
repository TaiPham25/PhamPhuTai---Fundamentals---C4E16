

# for i in range(3):
#     # print('*' * 4)
#     for k in range(4):
#         print('* ' , end='')
#     print()
for i in range(6):
    for j in range(6):
        if j >= 5 - i:
            print('x ', end='')
        else:
            print('  ', end='')
    print()
