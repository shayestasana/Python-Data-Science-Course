from turtle import *

speed('fast')
pencolor("red")
bgcolor('white')
       #Thickness of pen

n=10
lt(180)
for i in range(100):
    pencolor("red")
    fd(n)        
    rt(90)
    pencolor("blue")
    write('***', font=('arial',30,'normal'),align='center')
    n=n+2
mainloop()

#another way
#for i in range(100)
#fd(i*2)
#lt(90)
#
