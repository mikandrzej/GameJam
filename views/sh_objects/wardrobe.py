import pygame
import color
from controller import Controller
import os

from state import State, GameState
from properties import Properties

class Wardrobe:
    COLOR = color.BLUE
    ICON = pygame.image.load(os.path.join('resources', 'wardrobe_icon.png'))
    IMG_WARDROBE = pygame.image.load(os.path.join('resources', 'wardrobe.png'))
    IMGS_NAIL = {
        'BLACK' :   pygame.image.load(os.path.join('resources', 'nail.png')),
        'RED'   :   pygame.image.load(os.path.join('resources', 'nail_red.png')),
        'BLUE'   :   pygame.image.load(os.path.join('resources', 'nail_blue.png')),
        'GREEN'   :   pygame.image.load(os.path.join('resources', 'nail_green.png')),
        'VIOLET'   :   pygame.image.load(os.path.join('resources', 'nail_violet.png')),
        'DONE'   :   pygame.image.load(os.path.join('resources', 'nail_done.png'))
    }
    _scaledIcon = {}

    WARDROBE_X = 0.1
    WARDROBE_Y = 0.1
    WARDROBE_WIDTH = 0.7
    WARDROBE_HEIGHT= 0.7
    NAIL_X = 0.5
    NAIL_Y = 0.45
    NAIL_WIDTH = 0.08
    NAIL_HEIGHT = NAIL_WIDTH / 1.164179104477612
    NAIL_ROTATE = 30
    PROGRESS_X = 0.8
    PROGRESS_Y = 0.1
    PROGRESS_WIDTH = 0.1
    PROGRESS_HEIGHT = 0.025
    PROGRESS_OFFSET = 0.01

    def __init__(self, properties: Properties, state: State):
        self._properties = properties
        self._state = state
        self._scrWidth = properties.WIDTH
        self._scrHeight = properties.HEIGHT

        self._nailTimer = 0
        self._nailType = 'DONE'

        self._nailProgress = 0
        self._screwProgress = 0

        self._scaleImages()

    def draw(self, surface: pygame.Surface):
        self._recalculatePositions()
        surface.blit(self._scaledWardrobe,
                     pygame.Rect(self.WARDROBE_X * self._properties.WIDTH,
                                self.WARDROBE_Y * self._properties.HEIGHT,
                                self.WARDROBE_WIDTH * self._properties.WIDTH,
                                self.WARDROBE_HEIGHT * self._properties.HEIGHT))
        surface.blit(self._scaledNails[self._nailType],
                     pygame.Rect(self.NAIL_X * self._properties.WIDTH,
                                self.NAIL_Y * self._properties.HEIGHT,
                                self.NAIL_WIDTH * self._properties.WIDTH,
                                self.NAIL_HEIGHT * self._properties.HEIGHT))

    def _calculateCoordinates(self):
        self._progressX = self.PROGRESS_X * self._properties.WIDTH
        self._progressYs = []
        for x in range(5):
            self._progressYs.append(
                (self.PROGRESS_Y + (self.PROGRESS_OFFSET * x)) * self._properties.HEIGHT
            )

    def _scaleImages(self):
        self._scaledWardrobe = pygame.transform.scale(self.IMG_WARDROBE,
                                                      (int(self.WARDROBE_WIDTH * self._properties.WIDTH),
                                                        int(self.WARDROBE_HEIGHT * self._properties.HEIGHT)))
        self._scaledNails = {}
        for nail in self.IMGS_NAIL:
            rotNail = pygame.transform.rotate(self.IMGS_NAIL[nail], self.NAIL_ROTATE)
            self._scaledNails[nail] = pygame.transform.scale(rotNail,
                                                      (int(self.NAIL_WIDTH * self._properties.WIDTH),
                                                        int(self.NAIL_HEIGHT * self._properties.HEIGHT)))

    def _drawProgress(self, surface: pygame.Surface):


    def update(self, controller: Controller):
        self._nailTimer += self._properties.delta
        if self._nailTimer > 500:
            self._nailType = 'DONE'
        else:
            self._nailType = 'RED'

        if self._nailTimer > 1000:
            self._nailTimer = 0

    def _recalculatePositions(self):
        if self._scrWidth != self._properties.WIDTH or self._scrHeight != self._properties.HEIGHT:
            self._scaleImages()