from turtle import *

shape('turtle')
color('gray')
speed(-1)
length = 5

for i in range(80):
        forward(length)
        left(90)

        length += 5

mainloop()
