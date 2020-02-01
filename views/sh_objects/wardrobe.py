import pygame
import color
from controllers.inputhandler import InputHandler
import os

from state import State
from properties import Properties


class Wardrobe:
    COLOR = color.BLUE
    ICON = pygame.image.load(os.path.join('resources', 'wardrobe_icon.png'))
    IMG_WARDROBE = pygame.image.load(os.path.join('resources', 'wardrobe.png'))
    _scaledIcon = None

    WARDROBE_X = 0.1
    WARDROBE_Y = 0.1
    WARDROBE_WIDTH = 0.7
    WARDROBE_HEIGHT= 0.7

    def __init__(self, properties: Properties, state: State):
        self._properties = properties
        self._state = state
        self._scrWidth = properties.WIDTH
        self._scrHeight = properties.HEIGHT

    def draw(self, surface: pygame.Surface):
        pass

    def scaleImages(self):
        self._scaledWardrobe = pygame.transform.scale(self.IMG_WARDROBE,
                                                      (int(self.WARDROBE_WIDTH * self._properties.WIDTH),
                                                        int(self.WARDROBE_HEIGHT * self._properties.HEIGHT)))

    def update(self, controller: InputHandler):
        pass

    def recalculatePositions(self):
        if self._scrWidth != self._properties.WIDTH or self._scrHeight != self._properties.HEIGHT:
            self.scaleImages()