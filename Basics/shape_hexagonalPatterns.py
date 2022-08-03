from turtle import *
bgcolor('black')
speed('fastest')
colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for i in range(360):
    pencolor(colors[ i%6])
    width(i/100 +1)
    forward(i)
    left(59)
mainloop()
