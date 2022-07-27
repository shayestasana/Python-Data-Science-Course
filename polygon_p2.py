from turtle import *

speed('slow')
pencolor("red")
bgcolor('white')
pensize(10)       #Thickness of pen
side =4
size=50
fillcolor('red')
begin_fill()       #beginning of color filling
for i in range(side):
    fd(size)
    lt(90)
    fd(size)
    rt(90)
    fd(size)
    lt(90)
    
end_fill()     #end of color filling
mainloop()