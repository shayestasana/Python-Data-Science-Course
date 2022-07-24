from turtle import *

speed('fast')
pencolor("yellow")
bgcolor('white')
pensize(10)
side =4
size=100
fillcolor('green')
begin_fill()
for i in range(side):
    fd(size)
    lt(90)
    fd(size)
    rt(90)
    fd(size)
    lt(90)
end_fill()
mainloop()