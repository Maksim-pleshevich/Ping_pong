from pygame import *
from random import randint

WIDTH = 600
HEIGHT = 500
FPS = 60
WIN_SCORE = 10
RESTART_TIME = 3000

def generate_color():
    return (randint(0, 255), randint(0, 255),randint(0, 255))

background = generate_color()
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping-pong")
clock = time.Clock()


color_selection = False
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                color_selection = True
        elif e.type == K_UP:
            if e.key == K_SPACE:
                color_selection = False

        if not finish:
            if color_selection:
                background = generate_color()
            window.fill(background)
        else:
            pass
        
    display.update()
    clock.tick(FPS)