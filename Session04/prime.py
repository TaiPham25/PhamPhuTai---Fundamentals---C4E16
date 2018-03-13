#so nguyen to

n = int(input(' Enter a number: '))

is_prime = True
# C1
# for i in range (2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# C2
i = 2
while i <= (n ** 0.5): # n**0.5 la can so n
    if n % i == 0:
        is_prime = False
        break
    i += 1

if is_prime == True:
    print(n, 'is a prime number')
else:
    print(n,'is not a prime number')
