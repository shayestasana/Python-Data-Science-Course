import pgzrun
from random import randint

HEIGHT = 800
HEIGHT = 700
WIDTH = 1000

ps = 3 # player speed
es = 1 # enemy speed

game_over = False  # switch
game_started = False # switch

center = (WIDTH//2, HEIGHT//2) # points to center coordinates of screen

bg = Actor('bg', center=(0,0))
p = Actor('ironman', pos=(100,100))
e = Actor('zombie', pos=(700,100))

def show_screen_1():
    screen.fill('#ffff00')
    bg.draw()
    screen.draw.text('Our Game', center=center, fontsize=100, color='white')
    screen.draw.text('press Space to start', center = (center[0], center[1]+100), 
                        fontsize=50, color='white')

def show_game_screen():
    bg.draw()
    p.draw()
    e.draw()

def show_game_over():
    bg.draw()
    screen.draw.text('Game Over', center=center, fontsize=100, color='white')

def draw():
    screen.clear()
    if not game_started:
        show_screen_1()
    elif game_started and not game_over:
        show_game_screen()
    elif game_over:
        show_game_over()

def update():
    global game_started
    if keyboard.SPACE and not game_started:
        game_started = True
        bg.image = 'bg2'
    if game_started and not game_over:
        player_control()
        enemy_control()

def player_control():
    if keyboard.RIGHT and not p.right > WIDTH:
        p.x += ps
        p.angle = -10
    elif keyboard.LEFT and not p.left < 0:
        p.x += -ps
        p.angle = 10
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += ps
    elif keyboard.UP and not p.top < 0:
        p.y += -ps
    else:
        p.angle = 0

def enemy_control():
    global game_over
    if p.x > e.x:
        e.x += es
    if p.x < e.x:
        e.x += -es
    if p.y > e.y:
        e.y += es
    if p.y < e.y:
        e.y += -es
    if p.colliderect(e):
        game_over = True

pgzrun.go()