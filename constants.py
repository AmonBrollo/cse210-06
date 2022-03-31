import pygame
import os

from scripting.resource_path import resource_path
from scripting.assets import Assets

# List of all game sounds
soundlist = []

# Initialize Sound System
pygame.mixer.init()


class Path:
    # Path Vars
    FONT_PATH = os.path.join('assests', 'fonts')
    EXPLOSION_PATH = os.path.join('assets', 'graphics', 'explosion')
    GRAPHICS_PATH = os.path.join('assets', 'graphics')
    SOUND_PATH = os.path.join('assets', 'sounds')

    # Load Music
    GAME_MUSIC_PATH = resource_path(os.path.join(SOUND_PATH, 'ingame.wav'))
    MENU_MUSIC_PATH = resource_path(os.path.join(SOUND_PATH, 'menu.wav'))


class Font:
    # Font Vars
    edit_undo_font = Assets.font.load(Path.FONT_PATH, 'beat.ttf')
    neue_font = Assets.font.load(Path. FONT_PATH, 'beat.ttf')
    karmatic_arcade_font = Assets.font.load(
        Path.FONT_PATH, 'karmatic_arcade.ttf')


class Image:
    TITLE_LOGO = Assets.image.scale(Path.GRAPHICS_PATH, 'title_logo.png', 3/7)

    # Load Enemy Ships
    EASY_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'easy.png')
    MEDIUM_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'medium.png')
    HARD_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'hard.png')
    BOSS_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'boss.png')
    UFO_SPACE_SHIP = Assets.image.scale(Path.GRAPHICS_PATH, 'ufo.png', 1/7)

    # Load Player
    PLAYER_SPACE_SHIP = Assets.image.load(
        Path.GRAPHICS_PATH, 'retro-spaceship.png')
    PLAYER_LASER = Assets.image.load(
        Path.GRAPHICS_PATH, 'pixel_laser_cosmic.png')

    # Load Lasers
    RED_LASER = Assets.image.load(Path.GRAPHICS_PATH, 'pixel_laser_red.png')
    BLUE_LASER = Assets.image.load(Path.GRAPHICS_PATH, 'pixel_laser_blue.png')
    GREEN_LASER = Assets.image.load(
        Path.GRAPHICS_PATH, 'pixel_laser_green.png')
    FLAME_LASER = Assets.image.load(
        Path.GRAPHICS_PATH, 'pixel_laser_flame.png')

    # Load audio image
    VOL_ICON = Assets.image.load(Path.GRAPHICS_PATH, 'audio.png')
    MUTE_ICON = Assets.image.load(Path.GRAPHICS_PATH, 'mute.png')
    DEMON_ICON = Assets.image.scale(Path.GRAPHICS_PATH, 'demon.png', 1/11)

    # Screen Images
    CONTROL_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'joystick.png')
    TROPHY_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'trophy.png')
    SHIPS_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'medium.png', 5/6)
    SHIPS_IMAGE_2 = Assets.image.scale(Path.GRAPHICS_PATH, 'hard.png', 1/4)
    TOOLBOX_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'toolbox.png', 1/2)
    TOOLS_IMAGE = Assets.image.scale(Path.GAME_MUSIC_PATH, 'tools.png', 1/4)
    TOOLS_IMAGE = pygame.transform.rotate(TOOLS_IMAGE, -45)

    GO_BACK_IMAGE = Assets.image.scale(
        Path.GRAPHICS_PATH, 'back_arrow.png', 6/25)

    EXIT_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'exit_button.png', 1/3)

    # Other Images
    HEART_RANGE = Assets.image.scale(Path.GRAPHICS_PATH, 'heart.png', 1)
    STAR_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'star.png', 1/4)
    SKULL_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'skull.png', 1/8)
    SKULL_IMAGE_2 = Assets.image.scale(Path.GRAPHICS_PATH, 'skull.png', 1/8)
    WON_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'won.png', 5/20)

    PLUS_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'plus.png', 1/6)
    MINUS_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'minus.png', 1/6)

    PAUSE_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'pause.png', 2/7)
    PLAY_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'play.png', 2/7)
    PLAY_IMAGE_2 = Assets.image.scale(Path.GRAPHICS_PATH, 'play.png', 1/2.9)

    HOME_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'home.png', 2/5)
    NEXT_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'next_button.png', 1/3)
    BACK_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'back_button.png', 1/3)
    LEVELS_IMAGE = Assets.image.scale(
        Path.GRAPHICS_PATH, 'levels_button.png', 1/3)
    SCORE_IMAGE = Assets.image.scale(
        Path.GRAPHICS_PATH, 'score_button.png', 1/3)
    KILLS_IMAGE = Assets.image.scale(
        Path.GRAPHICS_PATH, 'kills_button.png', 1/3)

    MOUSE = Assets.image.scale(Path.GRAPHICS_PATH, 'mouse.png', 1/2)
    LEFT_MOUSE_CLICK = Assets.image.scale(
        Path.GRAPHICS_PATH, 'left_click_mouse.png', 1/2)
    RIGHT_MOUSE_CLICK = Assets.image.scale(
        Path.GRAPHICS_PATH, 'right_click_mouse.png', 1/2)
    WASD_KEYS = Assets.image.scale(Path.GRAPHICS_PATH, 'wasd_keys.png', 1/2)
    ARROW_KEYS = Assets.image.scale(Path.GRAPHICS_PATH, 'arrow_keys.png', 1/2)
    BACKSPACE_KEYS = Assets.image.scale(
        Path.GRAPHICS_PATH, 'backspace_key.png', 1/2)
    SPACEBAR_KEY = Assets.image.scale(
        Path.GRAPHICS_PATH, 'spacebar_key.png', 1/2)
    PLUS_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'plus_key.png', 1/2)
    MINUS_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'minus_key.png', 1/2)
    P_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'p_key.png', 1/2)
    F_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'f_key.png', 1/2)
    M_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'mute_key.png', 1/2)

    class Sound:
        PLAYER_LASER_SOUND = Assets.sounds.load(
            Path.SOUND_PATH, 'ownlaser.wav')
        ENEMY_LASER_SOUND = Assets.sounds.load(
            Path.SOUND_PATH, 'enemylaser.wav')
        EXPLODE_SOUND = Assets.sounds.load(Path.SOUND_PATH, 'explode.wav')
        LASER_HIT_SOUND = Assets.sounds.load(Path.SOUND_PATH, 'laser_hit.wav')

    class Colors:
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BACKGROUND_BLACK = (7, 8, 16)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        GREEN2 = (0, 209, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        CYAN = (0, 255, 255)
        MAGENTA = (255, 0, 255)
        PURPLE = (131, 1, 123)
        ORANGE = (238, 98, 17)
        GREY = (200, 200, 200)
        TRANS = (1, 1, 1)

    class Text:
        SHIPS = 'SHIPS'
        SETTINGS = 'SETTINGS'
        CONTROLS = 'CONTROLS'
        SCOREBOARD = 'SCOREBOARD'
