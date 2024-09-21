import pygame as pg
import content.game_state as gs
import content.scenes.main_menu as main_menu_scene
import content.scenes.play_screen as play_scene
import content.scenes.options_screen as options_scene
import content.scenes.quit as quit_scene

def main():
    pg.init()

    pg.display.set_caption("Snake Game")

    LIST_SCENES = [main_menu_scene, play_scene, options_scene, quit_scene]

    while not gs.GAME_CLOSE:
        gs.SCREEN.fill(gs.BG_COLOR)
        LIST_SCENES[gs.CURRENT_SCENE_INDEX].update()

        pg.display.update()
        gs.CLOCK.tick(gs.FPS)

    pg.quit()
    quit()