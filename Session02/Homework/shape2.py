from turtle import *
shape('arrow')
speed(-1)
n = 6
for i in range(n):
    if n == 3 and n == 5:
        color('blue')
    else:
        color('red')
        for i in range(n):
            forward(100)
            left(360/n)
    n = n - 1

mainloop()
