from turtle import *

pencolor('blue')
pensize(3)
fillcolor('red')
speed('fastest')
shape("turtle")
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    
    end_fill()
goto(20,250)
mainloop()