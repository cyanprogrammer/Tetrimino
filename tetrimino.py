import pygame as pg

class Player:
    def __init__(self, wh):
        self.img = pg.image.load("img/Player.png")
        self.rect = self.img.get_rect()
        self.rect.y = wh - self.img.get_height()

class Pig:
    def __init__(self):
        self.img

pg.init()
win_width = 800
win_height = 600
win = pg.display.set_mode((win_width, win_height))
clock = pg.time.Clock()

player = Player(win_height)
running = True
while running:
    for event in pg.event.get():
        #if event.type == pg.KEYDOWN:
        #    if event.key == pg.K_LEFT:
        #    elif event.key == pg.K_RIGHT:
        #    elif event.key == pg.K_DOWN:
        #    elif event.key == pg.K_UP:
                
        if event.type == pg.QUIT:
            running = False

    win.blit(player.img, player.rect)

    pg.display.update()
