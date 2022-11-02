import pgzrun
from random import randint

HEIGHT =500
WIDTH =600

music.play('bgm')  #background music

p = Actor('ironman', (100, 100))  # global variable
c = Actor('cookie')
c.x= randint(64, WIDTH-64)
c.y= randint(64, HEIGHT-64)

score = 0
speed=3


def draw():
    screen.fill("Black")
    c.draw()
    p.draw()  # local variable
    screen.draw.text(f'score:{score}', (WIDTH-80, 10))

def update():
    player_control()
    update_score()

def update_score():
    global score # it calls the global  variable score
    if p.colliderect(c):   #when image collides
        score += 1 
        c.pos = (randint(64, WIDTH-64), randint(64, HEIGHT-64))
        sounds.eating2.play()

def player_control():
    if keyboard.RIGHT and not p.right>WIDTH:
        p.x += speed
        p.angle = -10
    elif keyboard.LEFT and not p.left<0:
        p.x += -speed
        p.angle = 10
    elif keyboard.DOWN and not p.bottom>HEIGHT:
        p.y += speed
    elif keyboard.UP and not p.top<0:
        p.y += -speed
    else:
        p.angle = 0




pgzrun.go()   # outside the function