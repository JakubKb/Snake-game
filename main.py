import pygame as pg
from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
apple = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
apple.center = get_random_position()
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_direction = (0, 0)
time, time_step = 0, 110
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake_direction = (0, -TILE_SIZE)
            if event.key == pg.K_DOWN:
                snake_direction = (0, TILE_SIZE)
            if event.key == pg.K_LEFT:
                snake_direction = (-TILE_SIZE, 0)
            if event.key == pg.K_RIGHT:
                snake_direction = (TILE_SIZE, 0)
    screen.fill('black')
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    [pg.draw.rect(screen, 'red', apple)]
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_direction)
        segments.append(snake.copy())
        segments = segments[-length:]
    if snake.center == apple.center:
        apple.center = get_random_position()
        length += 1
    pg.display.flip()
    clock.tick(60)

