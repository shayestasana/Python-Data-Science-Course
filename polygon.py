from turtle import *

speed('slowest')
pencolor('red')
bgcolor('lightblue')

side =3
size=80
for i in range(side):
    fd(size)
    lt(360/side)

mainloop()  #it is defined outside the loop

