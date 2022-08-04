from turtle import *

value = 400

while value > 0:
    forward(value)
    left(90)
    value -= 20
    write(value)
mainloop() 