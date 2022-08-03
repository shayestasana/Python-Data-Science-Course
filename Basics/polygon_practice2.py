import turtle

turtle.title("My Turtle Program")
s = turtle.getscreen()
t=turtle.Turtle()
t.pensize(5)       #Thickness of pen... default size is 1
turtle.bgcolor("lightblue")
t.shape("turtle")    #change the way the turtle looks
t.speed(10)

# t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.fillcolor("orange") 

t.right(90)   #can use t.rt()
t.forward(100)   #can use t.fd()
t.left(90)    #can use t.lt()
t.backward(100)    #can use t.bk()

t.penup()
t.goto(100,100)
t.home()    #means t.goto(0,0)
t.pendown()

t.begin_fill()
t.circle(60)
t.end_fill()
