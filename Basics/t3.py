from turtle import *

side = 6
size = 100
speed('fastest')
pencolor("red")
bgcolor('white')
pensize(3)

for i in range(side):
    pencolor("red")
    fd(size)
    for i in range(side):
        pencolor("green")
        fd(size//2)
        lt(360/side)
    lt(360/side)

mainloop()