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
