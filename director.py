from distutils.command.config import config
import pygame
import os
import ctypes

from scripting.resource_path import resource_path

class Director:
    def __init__(self):
        # Root Vars
        self.TITLE = 'SPACE AND CONQUER'
        self.WIDTH = 750
        self.HEIGHT = 750

        #Load Background Image
        self.backgroundImage = pygame.image.load(resource_path(os.path.join('assets', 'graphics', 'background-black-wide.png')))

        windows_user = ctypes.windll.user32
        self.monitor_size = (windows_user.GetSystemMetrics(0), windows_user.GetSystemMetrics(1))

        #Set Background Dimensions
        self.BG = pygame.transform.scale(self.backgroundImage self.monitor_size)

        self.FPS = 60
        self.clock = pygame.time.Clock()

        #print(pygame.display.Info())
        self.CANVAS = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)

        self.screen_rect = self.CANVAS.get_rect()
        self.center_x = self.screen_rect.centerx
        self.starting_x = 0
        self.ending_y = self.HEIGHT
    
    def update(self, width, height):
        self.CANVAS = pygame.display.set_mode((width, height), pygame.RESIZEABLE)
        self.WIDTH = width
        self.HEIGHT = height
        self.center_x = width//2
        self.center_y = height//2
        self.ending_x = width
        self.ending_y = height
        self.BG = pygame.transform.scale(self.backgroundImage, (self.WIDTH, self.HEIGHT))

config = Director()


