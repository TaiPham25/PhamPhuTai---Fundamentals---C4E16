from turtle import *
shape('turtle')
color('blue')
speed(-1)

for i in range(48):
    for k in range(4):
        forward(i + 18)
        left(90)
    left(10)
    
mainloop()
