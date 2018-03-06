socanh = int(input("Ban muon hinh may canh"))
from turtle import *
shape('turtle')
# color('green')
speed(-1)
fillcolor('yellow')

begin_fill()
for i in range(socanh):
    forward(100)
    left(360/socanh)
end_fill()


mainloop()
