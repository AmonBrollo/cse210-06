import sys
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
    settings_btn = IconButton(Image.TOOLBOX_IMAGE, Text.SETTINGS)

    exit_btn = IconButton(Image.EXIT_IMAGE)

    run = True
    while run:
        pygame.mouse.set_visible(True)
        slow_bg_obj.update()
        slow_bg_obj.render()

        # Ships
        Assets.image.draw(Image.BOSS_SHIP, (config.center_x, 200), True)
        Assets.image.draw(Image.FLAME_LASER, (config.center_x, 360), True)
        Assets.image.draw(Image.PLAYER_SPACE_SHIP, (config.center_x-46, 575))
        Assets.image.draw(Image.PLAYER_LASER, (config.center_x, 490), True)

        mouse_btn.draw(
            (config.center_x - 210, config.center_y + 42), (195, 66))
        keyboard_btn.draw(
            (config.center_x + 15, config.center_y + 42), (195, 66))

        Assets.text.draw('Play Game', title_font, Colors.WHITE,
                         (config.center_x, config.center_y-10), True, True)

        # Control Page
        control_btn.draw((config.starting_x + 65, 53), True, True)

        # ScoreBoard Page
        trophy_btn.draw((config.ending_x - 65, 55), True, True)

        # Settings Page
        settings_btn.draw((config.ending_x - 65, 165), True, True)

        # Shis Page
        ships_btn.draw((config.starting_x + 65, 165), True, True)

        audio_cfg.display_volume()

        exit_btn.draw((config.ending_x - 75, config.ending_y - 40), True, True)

        Assets.image.draw(Image.TITLE_LOGO, (config.center_x, 10), True)

        pygame.display.flip()
        config.clock.tick(config.FPS)  # capping frame rate to 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.VIDEORESIZE:
                if not display_cfg.fullscreen:
                    config.update(event.w, event.h)

            # Keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    config.update(
                        config.monitor_size[0], config.monitor_size[1])
                    display_cfg.toggle_full_screen()

            # Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_btn.isOver():
                        game(True)
                    if keyboard_btn.isOver():
                        game()
                    if control_btn.isOver():
                        controls()
                    if trophy_btn.isOver():
                        score_board()
                    if ships_btn.isOver():
                        ships()
                    if settings_btn.isOver():
                        settings()
                    if exit_btn.isOver():
                        run = False

            # Mouse hover events
            if event.type == pygame.MOUSEMOTION:
                if mouse_btn.isOver():
                    mouse_btn.outline = True
                else:
                    mouse_btn.outline = False

                if keyboard_btn.isOver():
                    keyboard_btn.outline = True
                else:
                    keyboard_btn.outline = False

                if control_btn.isOver():
                    control_btn.outline = True
                else:
                    control_btn.outline = False

                if trophy_btn.isOver():
                    trophy_btn.outline = True
                else:
                    trophy_btn.outline = False

                if settings_btn.isOver():
                    settings_btn.outline = True
                else:
                    settings_btn.outline = False

                if ships_btn.isOver():
                    ships_btn.outline = True
                else:
                    ships_btn.outline = False

                if exit_btn.isOver():
                    exit_btn.outline = True
                else:
                    exit_btn.outline = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            run = False

        if keys[pygame.K_c]:
            controls()

        if keys[pygame.K_s]:
            score_board()

    pygame.guit()
    sys.exit(0)


if __name__ == "__main__":
    main()
