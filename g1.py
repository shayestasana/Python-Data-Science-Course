import pgzrun
HEIGHT =500
WIDTH =500
p= Actor('ironman', pos=(100,100))
 
def draw():
    screen.clear()
    screen.draw.text("welcome to pgzero", (10, 10), color='red', fontsize=50)
    screen.draw.text("created by Sana", (10, 360), color='white')
    #screen.draw.text("HiHiHiHi", (0, 0), color='red', fontsize=40)
    #screen.draw.text("Sana", (360, 10), color='white')
    p.draw()

# outside functions

pgzrun.go()
