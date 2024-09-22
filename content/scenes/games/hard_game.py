import pygame as pg
import content.game_state as gs

from typing import Tuple
import random

# draw bomb on screen
def drawBomb(grid_size: int, x_pos: int, y_pos: int, color: Tuple[int, int, int]):
    pg.draw.rect(gs.SCREEN, color, [x_pos, y_pos, 2 * grid_size, 2 * grid_size])

def getRandomInt(min: int, max: int):
    return round(random.randrange(min, max - gs.GRID_SIZE) / gs.GRID_SIZE) * gs.GRID_SIZE

fps_timer = 0

# bomb
bomb_x = getRandomInt(0, gs.SCREEN_WIDTH - gs.GRID_SIZE)
bomb_y = getRandomInt(0, gs.SCREEN_HEIGHT - gs.GRID_SIZE)
bomb_timer = 0
shouldGetNewBomb = True

def getNewBomb(snake_x: int, snake_y: int, food_list: list[list[int, int]]):
    global bomb_x, bomb_y, shouldGetNewBomb

    # check for duplicate positions
    while True:
        isDone = False

        bomb_x = getRandomInt(0, gs.SCREEN_WIDTH - gs.GRID_SIZE)
        bomb_y = getRandomInt(0, gs.SCREEN_HEIGHT - gs.GRID_SIZE)

        # check duplicate position
        for food in food_list:
            if (bomb_x == food[0] or bomb_x + gs.GRID_SIZE == food[0]) or (bomb_y == food[1] or bomb_y + gs.GRID_SIZE == food[1]):
                break
            isDone = True

        if (bomb_x == snake_x or bomb_x + gs.GRID_SIZE == snake_x) or (bomb_y == snake_y or bomb_y + gs.GRID_SIZE == snake_y):
            continue
        
        if isDone == True:
            break

def play(snake_x: int, snake_y: int, food_list: list[list[int, int]]):
    global fps_timer, bomb_x, bomb_y, bomb_timer, shouldGetNewBomb

    fps_timer += 1 / gs.FPS
    bomb_timer += 1 / gs.FPS
    
    # increase game speed every sec
    if fps_timer >= 1:
        gs.FPS += gs.FPS_INCREMENT
        fps_timer = 0

    # for generating a new bomb per 5 sec
    if bomb_timer >= gs.BOMB_REDRAW_TIME:
        shouldGetNewBomb = True
        bomb_timer = 0

    # generate a bomb if bomb timer is up
    if shouldGetNewBomb == True:
        getNewBomb(snake_x, snake_y, food_list)
        shouldGetNewBomb = False

    # death condition check by screen boundary
    if (bomb_x == snake_x or bomb_x + gs.GRID_SIZE == snake_x) and (bomb_y == snake_y or bomb_y + gs.GRID_SIZE == snake_y):
        gs.GAME_OVER = True
        fps_timer = 0
        bomb_timer = 0
    
    drawBomb(gs.GRID_SIZE, bomb_x, bomb_y, gs.RED)

    return (bomb_x, bomb_y)