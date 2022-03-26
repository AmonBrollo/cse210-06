import sys
from tkinter.tix import Tree
from turtle import title
import pygame
import argparse

from scripting.assets import Assets
from services.game import game
from services.controls import controls
from services.score_board import score_board
from services.ships import ships
from services.settings import settings
from services.background import slow_bg_obj
from casting.button import Button
from casting.icon_button import IconButton
from casting.controls import audio_cfg, display_cfg
from director import config
from constants import Path, Image, Font, Colors, Text

# parsing arguments
ag = argparse.ArgumentParser()
ag.add_argument("--mute", help="disable all sounds", action="store_true")
args = vars(ag.parse_args())

if args["mute"]:
    audio_cfg.toggle_mute()

pygame.font.init()

pygame.display.set_caption(config.TITLE)
pygame.display.set_icon(Image.PLAYER_SPACE_SHIP)

def main():
    title_font = pygame.font.Font(Font.edit_undo_font, 82)

    audio_cfg.play_music(Path.MENU_MUSIC_PATH)

    mouse_btn = Button(Colors.BACKGROUND_BLACK, Colors.WHITE, "MOUSE")
    keyboard_btn = Button(Colors.BACKGROUND_BLACK, Colors.WHITE, "KEYBOARD")
    control_btn = IconButton(Image.CONTROL_IMAGE, Text.CONTROLS)
    ships_btn = IconButton(Image.SHIPS_IMAGE, Text.SHIPS)
    trophy_btn = IconButton(Image.TROPHY_IMAGE, Text.SCOREBOARD)
    settings_btn = IconButton(Image.EXIT_IMAGE)

    exit_btn = IconButton(Image.EXIT_IMAGE)
    
    run = True
    while run:
        pygame.mouse.set_visible(True)
        slow_bg_obj.update()
        slow_bg_obj.render()

        # Ships
        Assets.image.draw(Image.BOSS_SHIP, (config.center_x, 110), True)
        Assets.image.draw(Image.FLAME_LASER, (config.center_x, 360), True)
        Assets.image.draw(Image.PLAYER_SPACE_SHIP, (config.center_x-46, 575))
        Assets.image.draw(Image.PLAYER_LASER, (config.center_x, 490), True)

        mouse_btn.draw(
            (config.center_x - 210, config.center_y + 42), (195, 66))
        keyboard_btn.draw(
            (config.center_x + 15, config.center_y + 42), (195, 66))
        
        Assets.text.draw('Start Game', title_font, Colors.WHITE,
                        (config.center_x, config.center_y-10), True, True)

        # Control Page
        control_btn.draw((config.starting_x + 65, 53), True, True)

        # ScoreBoard Page
        trophy_btn.draw((config.ending_x - 65, 55), True, True)

        #Settings Page
        settings_btn.draw((config.ending_x - 65, 165), True, True)

        #Shis Page
        ships_btn.draw((config.starting_x + 65, 165), True, True)

        audio_cfg.display_volume()

        


