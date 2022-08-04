from turtle import *

size = 100
side = 6
pensize(3)
speed(0)
for i in range(side):
    pencolor('red')
    forward(size)
    for i in range(side):
        pencolor('green')
        forward(size//2)
        fillcolor('blue')
        begin_fill()
        for i in range(side):
            pencolor('red')
            forward(size//4)
            left(360/side)
        end_fill()
        left(360/side) 
        circle(size//4)
    left(360/side)

mainloop()