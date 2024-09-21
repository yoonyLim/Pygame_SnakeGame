import pygame as pg
import content.game_state as gs
from content.assets.textbox import TextBox
from content.assets.button import Button
from content.utilities import tools
import content.scenes.games.normal_game as normal
import content.scenes.games.hard_game as hard

import random
from typing import Tuple

def getInt(val: int):
    return round(val / gs.GRID_SIZE) * gs.GRID_SIZE

def getRandomInt(min: int, max: int):
    return round(random.randrange(min, max - gs.GRID_SIZE) / gs.GRID_SIZE) * gs.GRID_SIZE

def drawGrid():
    for x in range(0, gs.SCREEN_WIDTH, gs.GRID_SIZE):
        for y in range(0, gs.SCREEN_HEIGHT, gs.GRID_SIZE):
            rect = pg.Rect(x, y, gs.GRID_SIZE, gs.GRID_SIZE)
            pg.draw.rect(gs.SCREEN, gs.CHARCOAL, rect, 1)

# starting coordinates
x = getInt(gs.SCREEN_WIDTH / 2)
y = getInt(gs.SCREEN_HEIGHT / 2)

# movement coordinates
x_change = gs.GRID_SIZE
y_change = 0

# snake body
snake_list = []
snake_length = 1

# food
food_x = getRandomInt(0, gs.SCREEN_WIDTH)
food_y = getRandomInt(0, gs.SCREEN_HEIGHT)
food_list = [[food_x, food_y]]

timer = 0
score = 0

# fever time
isFeverTime = False
numFoodUntilFeverTime = gs.NUM_FOOD_NEEDED_FOR_FEVER_TIME
numBonusFood = 0

# hard mode
bomb_x = 0
bomb_y = 0

def resetGame():
    global x, y, x_change, y_change, snake_list, snake_length, food_x, food_y, food_list, timer, score, isFeverTime, numFoodUntilFeverTime, numBonusFood

    gs.GAME_OVER = False
    gs.GAME_PAUSED = False
    x = getInt(gs.SCREEN_WIDTH / 2)
    y = getInt(gs.SCREEN_HEIGHT / 2)
    x_change = gs.GRID_SIZE
    y_change = 0
    snake_list = []
    snake_length = 1
    food_x = getRandomInt(0, gs.SCREEN_WIDTH)
    food_y = getRandomInt(0, gs.SCREEN_HEIGHT)
    food_list = [[food_x, food_y]]
    food_length = 1
    timer = 0
    score = 0
    isFeverTime = False
    numFoodUntilFeverTime = gs.NUM_FOOD_NEEDED_FOR_FEVER_TIME
    numBonusFood = int(gs.SCREEN_WIDTH / gs.GRID_SIZE)

    gs.FPS = 15

# draw snake on screen
def drawSnake(grid_size: int, snake_list: list[list[int, int]], color: Tuple[int, int, int]):
    for snake_part in snake_list:
        pg.draw.rect(gs.SCREEN, color, [snake_part[0], snake_part[1], grid_size, grid_size])

# draw food on screen
def drawFood(grid_size: int, food_list: list[list[int, int]], color: Tuple[int, int, int]):
    for food in food_list:
        pg.draw.rect(gs.SCREEN, color, [food[0], food[1], grid_size, grid_size])

def update():
    global x, y, x_change, y_change, snake_list, snake_length, food_x, food_y, food_list, timer, score, isFeverTime, numFoodUntilFeverTime, numBonusFood, bomb_x, bomb_y

    if gs.FIRST_GAME_LOOP:
        resetGame()
        gs.FIRST_GAME_LOOP = False

    while gs.GAME_PAUSED:
        gs.FPS = 30

        gs.MOUSE_POS = pg.mouse.get_pos()

        PAUSE_TXT = TextBox(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 3, "GAME PAUSED", gs.FONT_FAMILY, gs.TITLE_FONT_SIZE, gs.RED)
        RESUME_BTN = Button(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 2, "RESUME", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 0)
        MENU_BTN = Button(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 2 + tools.getTxtRectSize("RESUME", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE)[1], "BACK TO MENU", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 1)
        QUIT_BTN = Button(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 2 + 2 * tools.getTxtRectSize("RESUME", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE)[1], "QUIT", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 2)
        LIST_BTNS = [RESUME_BTN, MENU_BTN, QUIT_BTN]

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()
                elif event.key == pg.K_DOWN:
                    gs.PAUSE_CURRENT_OPTION_INDEX = (gs.PAUSE_CURRENT_OPTION_INDEX + 1) % len(LIST_BTNS)
                elif event.key == pg.K_UP:
                    gs.PAUSE_CURRENT_OPTION_INDEX = (gs.PAUSE_CURRENT_OPTION_INDEX + len(LIST_BTNS) - 1) % len(LIST_BTNS)
                elif event.key == pg.K_RETURN:
                    if gs.PAUSE_CURRENT_OPTION_INDEX == 0:
                        gs.GAME_PAUSED = False
                        gs.PAUSE_CURRENT_OPTION_INDEX = 0
                    elif gs.PAUSE_CURRENT_OPTION_INDEX == 1:
                        gs.CURRENT_SCENE_INDEX = 0
                        gs.PAUSE_CURRENT_OPTION_INDEX = 0
                        resetGame()
                        gs.FPS = 30
                    elif gs.PAUSE_CURRENT_OPTION_INDEX == 2:
                        pg.quit()
                        quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if RESUME_BTN.checkForInput(gs.MOUSE_POS):
                    gs.GAME_PAUSED = False
                    gs.PAUSE_CURRENT_OPTION_INDEX = 0
                elif MENU_BTN.checkForInput(gs.MOUSE_POS):
                    gs.CURRENT_SCENE_INDEX = 0
                    gs.PAUSE_CURRENT_OPTION_INDEX = 0
                    resetGame()
                    gs.FPS = 30
                elif QUIT_BTN.checkForInput(gs.MOUSE_POS):
                    pg.quit()
                    quit()
        
        tools.updateTxtBoxes([PAUSE_TXT])
        tools.updateBtns(LIST_BTNS, gs.PAUSE_CURRENT_OPTION_INDEX, gs.BUTTON_DEFAULT_COLOR, gs.BUTTON_SELECTED_COLOR)

        pg.display.update()
        gs.CLOCK.tick(gs.FPS)

    # game over
    while gs.GAME_OVER:
        gs.FPS = 30
        gs.SCREEN.fill(gs.GRAY)

        if snake_length == 0:
            gs.MOUSE_POS = pg.mouse.get_pos()

            SCORE_TXT = TextBox(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 3, "FINAL SCORE: " + str(score), gs.FONT_FAMILY, gs.TITLE_FONT_SIZE, gs.YELLOW)
            RETRY_BTN = Button(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 2, "RETRY", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 0)
            MENU_BTN = Button(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 2 + tools.getTxtRectSize("RETRY", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE)[1], "BACK TO MENU", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 1)
            QUIT_BTN = Button(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 2 + 2 * tools.getTxtRectSize("RETRY", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE)[1], "QUIT", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 2)
            LIST_BTNS = [RETRY_BTN, MENU_BTN, QUIT_BTN]

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        quit()
                    elif event.key == pg.K_DOWN:
                        gs.PLAY_SCREEN_CURRENT_OPTION_INDEX = (gs.PLAY_SCREEN_CURRENT_OPTION_INDEX + 1) % len(LIST_BTNS)
                    elif event.key == pg.K_UP:
                        gs.PLAY_SCREEN_CURRENT_OPTION_INDEX = (gs.PLAY_SCREEN_CURRENT_OPTION_INDEX + len(LIST_BTNS) - 1) % len(LIST_BTNS)
                    elif event.key == pg.K_RETURN:
                        if gs.PLAY_SCREEN_CURRENT_OPTION_INDEX == 0:
                            resetGame()
                            gs.PLAY_SCREEN_CURRENT_OPTION_INDEX = 0
                        elif gs.PLAY_SCREEN_CURRENT_OPTION_INDEX == 1:
                            gs.CURRENT_SCENE_INDEX = 0
                            gs.PLAY_SCREEN_CURRENT_OPTION_INDEX = 0
                            resetGame()
                            gs.FPS = 30
                        elif gs.PLAY_SCREEN_CURRENT_OPTION_INDEX == 2:
                            pg.quit()
                            quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if RETRY_BTN.checkForInput(gs.MOUSE_POS):
                        resetGame()
                        gs.PLAY_SCREEN_CURRENT_OPTION_INDEX = 0
                    elif MENU_BTN.checkForInput(gs.MOUSE_POS):
                        gs.CURRENT_SCENE_INDEX = 0
                        gs.PLAY_SCREEN_CURRENT_OPTION_INDEX = 0
                        resetGame()
                        gs.FPS = 30
                    elif QUIT_BTN.checkForInput(gs.MOUSE_POS):
                        pg.quit()
                        quit()
            
            tools.updateTxtBoxes([SCORE_TXT])
            tools.updateBtns(LIST_BTNS, gs.PLAY_SCREEN_CURRENT_OPTION_INDEX, gs.BUTTON_DEFAULT_COLOR, gs.BUTTON_SELECTED_COLOR)
        
        # death animation
        else:
            timer += 1 / gs.FPS
            drawSnake(gs.GRID_SIZE, snake_list, gs.RED)
            # to empty list in 1 sec
            if timer >= 1 / (score + 1):
                snake_list.pop()
                snake_length -= 1
                timer = 0

        pg.display.update()
        gs.CLOCK.tick(gs.FPS)

    # if going back to menu
    if gs.CURRENT_SCENE_INDEX == 0:
        return

    # get input
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_change = -gs.GRID_SIZE
                y_change = 0
            elif event.key == pg.K_RIGHT:
                x_change = gs.GRID_SIZE
                y_change = 0
            elif event.key == pg.K_UP:
                y_change = -gs.GRID_SIZE
                x_change = 0
            elif event.key == pg.K_DOWN:
                y_change = gs.GRID_SIZE
                x_change = 0
            elif event.key == pg.K_ESCAPE or event.key == pg.K_TAB:
                gs.GAME_PAUSED = True

    x += x_change
    y += y_change

    # Snake movement logic
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # death condition check by eating itself
    for segment in snake_list[:-1]:
        if segment == snake_head and isFeverTime == False:
            gs.GAME_OVER = True

    # death condition check by screen boundary
    if x >= gs.SCREEN_WIDTH or x < 0 or y >= gs.SCREEN_HEIGHT or y < 0:
        gs.GAME_OVER = True

    # Check if snake has eaten food
    for food in food_list:
        if x == food[0] and y == food[1]:
            food_list.remove(food)

            if len(food_list) == 0:
                # if hard mode, avoid bomb
                if gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX == 1:
                    while True:
                        food_x = getRandomInt(0, gs.SCREEN_WIDTH)
                        food_y = getRandomInt(0, gs.SCREEN_HEIGHT)

                        if (food_x == bomb_x or food_x == bomb_x + gs.GRID_SIZE) and (food_y == bomb_y or food_y == bomb_y + gs.GRID_SIZE):
                            continue
                        
                        break
                else:
                    food_x = getRandomInt(0, gs.SCREEN_WIDTH)
                    food_y = getRandomInt(0, gs.SCREEN_HEIGHT)
                food_list.append([food_x, food_y])

            # closer to fever time
            if isFeverTime == False:
                numFoodUntilFeverTime -= 1
            
            snake_length += 1
            score += 1

    # check if fever time
    if score != 0 and numFoodUntilFeverTime <= 0 and isFeverTime == False:
        isFeverTime = True
        numFoodUntilFeverTime = gs.NUM_FOOD_NEEDED_FOR_FEVER_TIME
        # place multiple food on screen
        for i in range(int(gs.SCREEN_WIDTH / gs.GRID_SIZE)):
            # check for duplicate positions
            while True:
                isDone = False

                food_x = getRandomInt(0, gs.SCREEN_WIDTH)
                food_y = getRandomInt(0, gs.SCREEN_HEIGHT)

                # check duplicate position
                for food in food_list:
                    if food_x == food[0] and food_y == food[1]:
                        break
                    isDone = True

                # if hard mode, avoid bomb
                if gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX == 1 and (food_x == bomb_x or food_x == bomb_x + gs.GRID_SIZE) and (food_y == bomb_y or food_y == bomb_y + gs.GRID_SIZE):
                    continue
                
                if isDone == True:
                    break

            food_list.append([food_x, food_y])

    # check if end fever time
    if isFeverTime == True:
        timer += 1 / gs.FPS
        if timer >= gs.FEVER_TIME_MAX:
            isFeverTime = False
            timer = 0
            # leave only one food on screen
            for i in range(len(food_list) - 1):
                food_list.pop()

    # based on difficulty option
    if gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX == 0:
        normal.play()
    else:
        (bomb_x, bomb_y) = hard.play(x, y, food_list)

    # based on show grid option
    if gs.OPTIONS_SCREEN_CURRENT_GRID_INDEX == 1:
        drawGrid()

    # draw snake and food
    if isFeverTime == True:
        drawSnake(gs.GRID_SIZE, snake_list, (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
    else: 
        drawSnake(gs.GRID_SIZE, snake_list, gs.GREEN)
        
    drawFood(gs.GRID_SIZE, food_list, gs.WHITE)

    # in-game textboxes
    IN_GAME_SCORE_TXT = TextBox(0, 0, "SCORE: " + str(score), gs.FONT_FAMILY, gs.FONT_SIZE, gs.YELLOW, "topleft")
    IN_GAME_FEVER_TIME_TXT = TextBox(gs.SCREEN_WIDTH / 4, 0, str(numFoodUntilFeverTime) + " 'til FEVER TIME", gs.FONT_FAMILY, gs.FONT_SIZE, gs.GOLD, "topleft")
    IN_GAME_DIFFICULTY_TXT = TextBox(gs.SCREEN_WIDTH - tools.getTxtRectSize("DIFFICULTY: " + ("NORMAL" if gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX == 0 else "HARD"), gs.FONT_FAMILY, gs.FONT_SIZE)[0], 0, "DIFFICULTY: " + ("NORMAL" if gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX == 0 else "HARD"), gs.FONT_FAMILY, gs.FONT_SIZE, gs.YELLOW, "topleft")
    
    if y >= gs.SCREEN_HEIGHT / 4:
        tools.updateTxtBoxes([IN_GAME_SCORE_TXT, IN_GAME_FEVER_TIME_TXT, IN_GAME_DIFFICULTY_TXT])

    # prep for game over
    if gs.GAME_OVER == True:
        timer = 0
        snake_list.pop()
        snake_length -= 1