import pygame
import time

class Tetrimino:
    def __init__(type):
        self.x = 0
        self.y = 0


pygame.init()
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

fall_speed = 0.5
start_time = time,.time()
grid = [[0 for _ in range(10)] for _ in range(20)]
tetrominoes =  [
    # 'I' Tetromino
    [[1, 1, 1, 1],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    # Other Tetrominoes...
]

running = True
while running:
    if time.time() - start_time > fall_speed:
        # Move the Tetromino down
        current_tetromino.y += 1
        start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_tetromino.x -= 1
            elif event.key == pygame.K_RIGHT:
                current_tetromino.x += 1
            elif event.key == pygame.K_DOWN:
                current_tetromino.y += 1
            elif event.key == pygame.K_UP:
                current_tetromino.rotate()


        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
