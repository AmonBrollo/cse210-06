import colorsys
import pygame
import sys
import time
import random

from casting.ship import Player, Enemy
from casting.explosion import Explosion, explosion_group
from casting.controls import audio_cfg, display_cfg
from casting.scores import scores
from casting.icon_button import IconButton
from scripting.collide import collide
from scripting.assets import Assets
from .background import bg_obj

from director import config
from constants import Path, Image, Font, Colors

pause = False

play_btn = IconButton(Image.PLAY_IMAGE)


def game(isMouse=False):
    global pause
    lives = 6
    laser_vel = 10

    sub_font = pygame.font.Font(Font.neue_font, 40)
    sub_small_font = pygame.font.Font(Font.neue_font, 35)
    pop_up_font = pygame.font.Font(Font.edit_undo_font, 55)

    #load and play ingame music
    audio_cfg.play_music(Path.GAME_MUSIC_PATH)

    enemies = []
    wave_length = 0
    enemy_vel = 1

    player = Player(config.center_x, 585, mouse_movement=isMouse)
    if isMouse == True:
        pygame.mouse.set_visible(False)
    elif isMouse == False:
        pygame.mouse.set_visible(True)

    lost = False
    win = False
    boss_entry = True

    pause_btn = IconButton(Image.PAUSE_IMAGE)

    explosion_group.empty()

    def redraw_window():
        bg_obj.update()
        bg_obj.render()

        player.draw()

        for enemyShip in enemies:
            enemyShip.draw()

        if pause == True:
            play_btn.draw((config.center_x, 45), True, True)

        else:
            pause_btn.draw((config.center_x, 45), True, True)

        # Lives
        for index in range(1, lives + 1):
            Assets.image.draw(Image.HEART_IMAGE,
                            (config.starting_x + 37 * index - 7, 30))

        # Draw Text
        Assets.text.draw(f'{player.get_level()} / 10' , sub_small_font, Colors.CYAN,
                        (config.starting_x + 33, 75))

        score = player.get_score()
        leftScoreIdx = 0
        if score >= 100 and score < 1000:
            leftScoreIdx = 1

        elif score >= 1000:
            leftScoreIdx = 2

        score_label = Assets.text.render(
            f'{score}', sub_font, Colors.GREEN)
        Assets.text.drawSurface(
            score_label, (config.ending_x - score_label.get_width() - 30, 20))
        Assets.image.draw(Image.STAR_IMAGE,
                        (config.ending_x - Image.SKULL_IMAGE.get_width() - 85 - leftScoreIdx*23, 26))

        kills = player.get_kills()
        leftKillsIdx = 0
        if kills >= 100:
            leftKillsIdx = 1

        Assets.image.draw(Image.SKULL_IMAGE,
                        (config.ending_x - Image.SKULL_IMAGE.get_width() - 30, 75))                          

        if win:
            scores.append(True,)