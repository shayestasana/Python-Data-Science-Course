from turtle import *

pencolor('blue')

fillcolor('red')
speed('fastest')

c=[             #list of coordinates
    (-300,300),
    (0,300),
    (300,300),
    (-150,150),
    (150,150),
    (0,0),
]

penup()    
for i in range(6):
    goto(c[i])
    pendown()
    dot(50)
    penup()

mainloop()

#n=30
#for i in range(3):
 #   dot(15)
  #  penup()
   # goto(n,0)
    #pendown()
    #n=n+30