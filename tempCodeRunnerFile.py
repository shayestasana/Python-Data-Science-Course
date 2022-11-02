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