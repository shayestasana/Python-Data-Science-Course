import turtle
import random

turtle.title("My Turtle Program")
s = turtle.getscreen()
t=turtle.Turtle()
t.pensize(5)       #Thickness of pen... default size is 1
turtle.bgcolor("lightblue")
t.shape("turtle")    #change the way the turtle looks
t.speed("slow")

#n=10
#while n <= 40:
#    t.circle(n)
#   n = n+10

for x in range(5):
    randColor=random.randrange(0,len(colors))
    t.color(colors[randColor], colors[random.randrange(0, len(colors))])
    rand1= random.randrange(-300,300)
    rand2= random.randrange(-300,300)
    t.penup()
    t.setpos((rand1, rand2))
    t.pendown()
    t.begin_fill()
    t.circle(random.randrange(0, 80))
    t.end_fill()
