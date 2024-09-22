import pygame as pg
import content.game_state as gs
from content.assets.button import Button
from content.assets.textbox import TextBox
from content.utilities import tools

def updateScreenSize(option: int):
    if option == 0:
        tools.setScreen(640, 480)
    elif option == 1:
        tools.setScreen(1280, 720)
    elif option == 2:
        tools.setScreen(1920, 1080)
    elif option == 3:
        tools.setScreen(2560, 1440)
    else:
        tools.setScreen(pg.display.set_mode().get_size()[0], pg.display.set_mode().get_size()[1])

def updateGridSize(option: int):
    if option == 0:
        gs.GRID_SIZE = 10
    elif option == 1:
        gs.GRID_SIZE = 20
    elif option == 2:
        gs.GRID_SIZE = 30
    else:
        gs.GRID_SIZE = 40

def updateCategoryBtns(btns: list[Button], idx: int, temp_idx: int):
    tools.updateBtns(btns, temp_idx, gs.BUTTON_DEFAULT_COLOR, gs.BUTTON_SELECTED_COLOR)
    if idx != temp_idx:
        btns[idx].setColor(gs.BLUE)
        btns[idx].update()

def update():
    gs.MOUSE_POS = pg.mouse.get_pos()

    # initialize textboxes
    RESOLUTION_TXTBOX = TextBox(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 8, "RESOLUTION", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE, gs.TEXTBOX_COLOR)
    DIFFICULTY_TXTBOX = TextBox(gs.SCREEN_WIDTH / 2, 2 * gs.SCREEN_HEIGHT / 6, "DIFFICULTY", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE, gs.TEXTBOX_COLOR)
    GIRD_TXTBOX = TextBox(gs.SCREEN_WIDTH / 2, 3 * gs.SCREEN_HEIGHT / 6, "SHOW GRID", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE, gs.TEXTBOX_COLOR)
    GRID_SIZE_TXTBOX = TextBox(gs.SCREEN_WIDTH / 2, 4 * gs.SCREEN_HEIGHT / 6, "BLOCK SIZE", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE, gs.TEXTBOX_COLOR)
    LIST_TXTBOXES = [RESOLUTION_TXTBOX, DIFFICULTY_TXTBOX, GIRD_TXTBOX, GRID_SIZE_TXTBOX]

    # go back to main menu button (the last category)
    BACK_TO_MAIN_MENU_BTN = Button(gs.SCREEN_WIDTH / 2, 5 * gs.SCREEN_HEIGHT / 6, "BACK TO MAIN MENU", gs.FONT_FAMILY, gs.BUTTON_FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 4)

    # for resolution buttons postion
    RESOLUTION_FIRST_ROW_HALF_WIDTH = tools.getTxtRectSize("640 X 4801280 X 7201920 X 1080", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[0] / 2
    RESOLUTION_SECOND_ROW_HALF_WIDTH = tools.getTxtRectSize("2560 X 1440FULLSCREEN", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[0] / 2

    # resolution buttons
    RESOLUTION_SD_BTN = Button(gs.SCREEN_WIDTH / 2 - RESOLUTION_FIRST_ROW_HALF_WIDTH, gs.SCREEN_HEIGHT / 8 + tools.getTxtRectSize("RESOLUTION", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "640 X 480", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 0)
    RESOLUTION_HD_BTN = Button(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 8 + tools.getTxtRectSize("RESOLUTION", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "1280 X 720", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 1)
    RESOLUTION_FHD_BTN = Button(gs.SCREEN_WIDTH / 2 + RESOLUTION_FIRST_ROW_HALF_WIDTH, gs.SCREEN_HEIGHT / 8 + tools.getTxtRectSize("RESOLUTION", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "1920 X 1080", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 2)
    RESOLUTION_QHD_BTN = Button(gs.SCREEN_WIDTH / 2 - RESOLUTION_SECOND_ROW_HALF_WIDTH, gs.SCREEN_HEIGHT / 8 + 2 * tools.getTxtRectSize("RESOLUTION", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "2560 X 1440", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 3)
    RESOLUTION_FULLSCREEN_BTN = Button(gs.SCREEN_WIDTH / 2 + RESOLUTION_FIRST_ROW_HALF_WIDTH, gs.SCREEN_HEIGHT / 8 + 2 * tools.getTxtRectSize("RESOLUTION", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "FULLSCREEN", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 4)
    LIST_RESOLUTION_BTNS = [RESOLUTION_SD_BTN, RESOLUTION_HD_BTN, RESOLUTION_FHD_BTN, RESOLUTION_QHD_BTN, RESOLUTION_FULLSCREEN_BTN]

    # for difficulty buttons position
    DIFFICULTY_ROW_HALF_WIDTH = tools.getTxtRectSize("NORMALHARD", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[0] / 2

    # difficulty buttons
    DIFFICULTY_NORMAL_BTN = Button(gs.SCREEN_WIDTH / 2 - DIFFICULTY_ROW_HALF_WIDTH, 2 * gs.SCREEN_HEIGHT / 6 + tools.getTxtRectSize("DIFFICULTY", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "NORMAL", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 0)
    DIFFICULTY_HARD_BTN = Button(gs.SCREEN_WIDTH / 2 + DIFFICULTY_ROW_HALF_WIDTH, 2 * gs.SCREEN_HEIGHT / 6 + tools.getTxtRectSize("DIFFICULTY", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "HARD", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 1)
    LIST_DIFFICULTY_BTNS = [DIFFICULTY_NORMAL_BTN, DIFFICULTY_HARD_BTN]

    # for grid buttons position
    GRID_ROW_HALF_WIDTH = tools.getTxtRectSize("NOYES", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[0] / 2

    # show grid buttons
    GRID_NO_BTN = Button(gs.SCREEN_WIDTH / 2 - GRID_ROW_HALF_WIDTH, 3 * gs.SCREEN_HEIGHT / 6 + tools.getTxtRectSize("SHOW GRID", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "NO", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 0)
    GRID_YES_BTN = Button(gs.SCREEN_WIDTH / 2 + GRID_ROW_HALF_WIDTH, 3 * gs.SCREEN_HEIGHT / 6 + tools.getTxtRectSize("SHOW GRID", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "YES", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 1)
    LIST_GRID_BTNS = [GRID_NO_BTN, GRID_YES_BTN]
    
    # for block size buttons position
    GRID_SIZE_ROW_HALF_WIDTH = tools.getTxtRectSize("10203040", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[0] / 2

    # block size buttons
    GRID_SIZE_10_BTN = Button(gs.SCREEN_WIDTH / 2 - GRID_SIZE_ROW_HALF_WIDTH, 4 * gs.SCREEN_HEIGHT / 6 + tools.getTxtRectSize("GRID SIZE", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "10", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 0)
    GRID_SIZE_20_BTN = Button(gs.SCREEN_WIDTH / 2 - GRID_SIZE_ROW_HALF_WIDTH / 3, 4 * gs.SCREEN_HEIGHT / 6 + tools.getTxtRectSize("GRID SIZE", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "20", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 1)
    GRID_SIZE_30_BTN = Button(gs.SCREEN_WIDTH / 2 + GRID_SIZE_ROW_HALF_WIDTH / 3, 4 * gs.SCREEN_HEIGHT / 6 + tools.getTxtRectSize("GRID SIZE", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "30", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 2)
    GRID_SIZE_40_BTN = Button(gs.SCREEN_WIDTH / 2 + GRID_SIZE_ROW_HALF_WIDTH, 4 * gs.SCREEN_HEIGHT / 6 + tools.getTxtRectSize("GRID SIZE", gs.FONT_FAMILY, gs.TEXTBOX_FONT_SIZE)[1], "40", gs.FONT_FAMILY, gs.FONT_SIZE, gs.BUTTON_DEFAULT_COLOR, 3)
    LIST_GRID_SIZE_BTNS = [GRID_SIZE_10_BTN, GRID_SIZE_20_BTN, GRID_SIZE_30_BTN, GRID_SIZE_40_BTN]

    # update current selected buttons
    tools.updateBtns(LIST_RESOLUTION_BTNS, gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX, gs.BUTTON_DEFAULT_COLOR, gs.BLUE)
    tools.updateBtns(LIST_DIFFICULTY_BTNS, gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX, gs.BUTTON_DEFAULT_COLOR, gs.BLUE)
    tools.updateBtns(LIST_GRID_BTNS, gs.OPTIONS_SCREEN_CURRENT_GRID_INDEX, gs.BUTTON_DEFAULT_COLOR, gs.BLUE)
    tools.updateBtns(LIST_GRID_SIZE_BTNS, gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX, gs.BUTTON_DEFAULT_COLOR, gs.BLUE)

    # get input
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                gs.GAME_CLOSE = True
            elif event.key == pg.K_DOWN or event.key == pg.K_s:
                gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX = (gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX + 1) % (len(LIST_TXTBOXES) + 1)
            elif event.key == pg.K_UP or event.key == pg.K_w:
                gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX = (gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX + len(LIST_TXTBOXES)) % (len(LIST_TXTBOXES) + 1)
            elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                if gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 0:
                    gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_TEMP_INDEX = (gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_TEMP_INDEX + 1) % len(LIST_RESOLUTION_BTNS)
                elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 1:
                    gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_TEMP_INDEX = (gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_TEMP_INDEX + 1) % len(LIST_DIFFICULTY_BTNS)
                elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 2:
                    gs.OPTIONS_SCREEN_CURRENT_GRID_TEMP_INDEX = (gs.OPTIONS_SCREEN_CURRENT_GRID_TEMP_INDEX + 1) % len(LIST_GRID_BTNS)
                elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 3:
                    gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_TEMP_INDEX = (gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_TEMP_INDEX + 1) % len(LIST_GRID_SIZE_BTNS)
            elif event.key == pg.K_LEFT or event.key == pg.K_a:
                if gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 0:
                    gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_TEMP_INDEX = (gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_TEMP_INDEX + len(LIST_RESOLUTION_BTNS) - 1) % len(LIST_RESOLUTION_BTNS)
                elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 1:
                    gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_TEMP_INDEX = (gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_TEMP_INDEX + len(LIST_DIFFICULTY_BTNS) - 1) % len(LIST_DIFFICULTY_BTNS)
                elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 2:
                    gs.OPTIONS_SCREEN_CURRENT_GRID_TEMP_INDEX = (gs.OPTIONS_SCREEN_CURRENT_GRID_TEMP_INDEX + len(LIST_GRID_BTNS) - 1) % len(LIST_GRID_BTNS)
                elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 3:
                    gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_TEMP_INDEX = (gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_TEMP_INDEX + len(LIST_GRID_SIZE_BTNS) - 1) % len(LIST_GRID_SIZE_BTNS)
            # confirm by enter
            elif event.key == pg.K_RETURN:
                if gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 0:
                    gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX = gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_TEMP_INDEX
                    updateScreenSize(gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX)
                elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 1:
                    gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX = gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_TEMP_INDEX
                elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 2:
                    gs.OPTIONS_SCREEN_CURRENT_GRID_INDEX = gs.OPTIONS_SCREEN_CURRENT_GRID_TEMP_INDEX
                elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 3:
                    gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX = gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_TEMP_INDEX
                    updateGridSize(gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX)
                else:
                    gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX = 0
                    gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_TEMP_INDEX = 0
                    gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_TEMP_INDEX = 0
                    gs.CURRENT_SCENE_INDEX = 0
        elif event.type == pg.MOUSEBUTTONDOWN:
            # resolution
            if RESOLUTION_SD_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX = 0
                updateScreenSize(gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX)
            elif RESOLUTION_HD_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX = 1
                updateScreenSize(gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX)
            elif RESOLUTION_FHD_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX = 2
                updateScreenSize(gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX)
            elif RESOLUTION_QHD_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX = 3
                updateScreenSize(gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX)
            elif RESOLUTION_FULLSCREEN_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX = 4
                updateScreenSize(gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX)
            # difficulty
            elif DIFFICULTY_NORMAL_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX = 0
            elif DIFFICULTY_HARD_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX = 1
            # show grid
            elif GRID_NO_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_GRID_INDEX = 0
            elif GRID_YES_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_GRID_INDEX = 1
            # grid size
            elif GRID_SIZE_10_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX = 0
                updateGridSize(gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX)
            elif GRID_SIZE_20_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX = 1
                updateGridSize(gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX)
            elif GRID_SIZE_30_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX = 2
                updateGridSize(gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX)
            elif GRID_SIZE_40_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX = 3
                updateGridSize(gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX)
            # back to main menu
            elif BACK_TO_MAIN_MENU_BTN.checkForInput(gs.MOUSE_POS):
                gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX = 0
                gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_TEMP_INDEX = 0
                gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_TEMP_INDEX = 0
                gs.CURRENT_SCENE_INDEX = 0

    # update selected btn in each category
    if gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 0:
        updateCategoryBtns(LIST_RESOLUTION_BTNS, gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_INDEX, gs.OPTIONS_SCREEN_CURRENT_RESOLUTION_TEMP_INDEX)
    elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 1:
        updateCategoryBtns(LIST_DIFFICULTY_BTNS, gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_INDEX, gs.OPTIONS_SCREEN_CURRENT_DIFFICULTY_TEMP_INDEX)
    elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 2:
        updateCategoryBtns(LIST_GRID_BTNS, gs.OPTIONS_SCREEN_CURRENT_GRID_INDEX, gs.OPTIONS_SCREEN_CURRENT_GRID_TEMP_INDEX)
    elif gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX == 3:
        updateCategoryBtns(LIST_GRID_SIZE_BTNS, gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_INDEX, gs.OPTIONS_SCREEN_CURRENT_GRID_SIZE_TEMP_INDEX)

    tools.updateTxtBoxes(LIST_TXTBOXES)
    tools.updateBtns([BACK_TO_MAIN_MENU_BTN], gs.OPTIONS_SCREEN_CURRENT_OPTION_INDEX, gs.BUTTON_DEFAULT_COLOR, gs.BUTTON_SELECTED_COLOR)