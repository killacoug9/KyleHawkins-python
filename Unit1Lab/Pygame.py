import pygame as pg
draw = pg.draw
import base_game as bg

# Start PyGame system
pg.init()

# Create a screen with dimensions
screen = pg.display.set_mode([600, 800])

# Helper variables
is_running = True
GREEN = (0, 255, 0)
radius = 50

while is_running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
         ###################################

    draw.rect(screen, GREEN, (100, 100))
    pg.display.update()

pg.quit()

