from turtle import *
shape('arrow')
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(-1)

for k in range(1):
    fillcolor(colors[0])
    begin_fill()
    for i in range(2):
        pencolor(colors[0])
        forward(50)
        right(90)
        forward(80)
        right(90)
    end_fill()
    forward(50)

    fillcolor(colors[1])
    begin_fill()
    for i in range(2):
        pencolor(colors[1])
        forward(50)
        right(90)
        forward(80)
        right(90)
    end_fill()
    forward(50)

    fillcolor(colors[2])
    begin_fill()
    for i in range(2):
        pencolor(colors[2])
        forward(50)
        right(90)
        forward(80)
        right(90)
    end_fill()
    forward(50)

    fillcolor(colors[3])
    begin_fill()
    for i in range(2):
        pencolor(colors[3])
        forward(50)
        right(90)
        forward(80)
        right(90)
    end_fill()
    forward(50)

    fillcolor(colors[4])
    begin_fill()
    for i in range(2):
        pencolor(colors[4])
        forward(50)
        right(90)
        forward(80)
        right(90)
    end_fill()
    forward(50)

mainloop()
