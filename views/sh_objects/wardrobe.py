import pygame
import color
from controllers.inputhandler import InputHandler
import os

from state import State
from properties import Properties
from utils import Utils

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
    IMGS_SCREW = {
        'BLACK' :   pygame.image.load(os.path.join('resources', 'screw.png')),
        'RED'   :   pygame.image.load(os.path.join('resources', 'screw_red.png')),
        'BLUE'   :   pygame.image.load(os.path.join('resources', 'screw_blue.png')),
        'GREEN'   :   pygame.image.load(os.path.join('resources', 'screw_green.png')),
        'VIOLET'   :   pygame.image.load(os.path.join('resources', 'screw_violet.png')),
        'DONE'   :   pygame.image.load(os.path.join('resources', 'screw_done.png'))
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
    SCREW_X = 0.4
    SCREW_Y = 0.55
    SCREW_WIDTH = 0.08
    SCREW_HEIGHT = SCREW_WIDTH / 1.164179104477612
    SCREW_ROTATE = 0
    PROGRESS_X = 0.8
    PROGRESS_Y = 0.1
    PROGRESS_WIDTH = 0.1
    PROGRESS_HEIGHT = 0.025
    PROGRESS_OFFSET = 0.03
    PROGRESS_BOUND_WIDTH = 0.005
    PROGRESS_TEXT_X = 0.95
    PROGRESS_TEXT_NAIL = 'Nail'
    PROGRESS_TEXT_SCREW = 'Screw'

    def __init__(self, properties: Properties, state: State):
        self._properties = properties
        self._state = state
        self._scrWidth = properties.WIDTH
        self._scrHeight = properties.HEIGHT

        self._nailTimer = 0
        self._nailType = 'DONE'
        self._screwType = 'DONE'

        self._nailProgress = 0
        self._screwProgress = 0

        self._scaleImages()
        self._calculateCoordinates()

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
        surface.blit(self._scaledScrews[self._screwType],
                     pygame.Rect(self.SCREW_X * self._properties.WIDTH,
                                self.SCREW_Y * self._properties.HEIGHT,
                                self.SCREW_WIDTH * self._properties.WIDTH,
                                self.SCREW_HEIGHT * self._properties.HEIGHT))
        self._drawProgress(surface)
        self._drawFonts(surface)

    def _drawFonts(self, surface: pygame.Surface):
        #nail text
        self._progressNailFont = pygame.font.Font(self._properties.labelPuzzleProgressFont,
                                                  self._properties.labelPuzzleProgressSize)
        textSurf, textRect = Utils.textGenerator(self.PROGRESS_TEXT_NAIL,
                                                 self._progressNailFont,
                                                 color.COL_PUZZLE_PROGRESS_TEXT)
        textRect.midtop = (self.PROGRESS_TEXT_X * self._properties.WIDTH,
                           self._progressYs[0] * self._properties.HEIGHT)
        surface.blit(textSurf, textRect)

        #screw text
        self._progressScrewFont = pygame.font.Font(self._properties.labelPuzzleProgressFont,
                                                  self._properties.labelPuzzleProgressSize)
        textSurf, textRect = Utils.textGenerator(self.PROGRESS_TEXT_SCREW,
                                                 self._progressNailFont,
                                                 color.COL_PUZZLE_PROGRESS_TEXT)
        textRect.midtop = (self.PROGRESS_TEXT_X * self._properties.WIDTH,
                           self._progressYs[1] * self._properties.HEIGHT)
        surface.blit(textSurf, textRect)

    def _calculateCoordinates(self):
        self._progressX = self.PROGRESS_X
        self._progressInnerX = self.PROGRESS_X + self.PROGRESS_BOUND_WIDTH
        self._progressYs = []
        self._progressInnerYs = []
        for x in range(5):
            self._progressYs.append(
                self.PROGRESS_Y + (self.PROGRESS_OFFSET * x)
            )
            self._progressInnerYs.append(
                self.PROGRESS_Y + self.PROGRESS_BOUND_WIDTH + (self.PROGRESS_OFFSET * x)
            )
        self._progressInnerWidth = self.PROGRESS_WIDTH - 2 * self.PROGRESS_BOUND_WIDTH
        self._progressInnerHeight = self.PROGRESS_HEIGHT - 2 * self.PROGRESS_BOUND_WIDTH

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
        self._scaledScrews = {}
        for screw in self.IMGS_SCREW:
            rotScrew = pygame.transform.rotate(self.IMGS_SCREW[screw], self.SCREW_ROTATE)
            self._scaledScrews[screw] = pygame.transform.scale(rotScrew,
                                                      (int(self.SCREW_WIDTH * self._properties.WIDTH),
                                                        int(self.SCREW_HEIGHT * self._properties.HEIGHT)))

    def _drawProgress(self, surface: pygame.Surface):
        # nail progress
        rectOuter = pygame.Rect(
            self._progressX * self._properties.WIDTH,
            self._progressYs[0] * self._properties.HEIGHT,
            self.PROGRESS_WIDTH * self._properties.WIDTH,
            self.PROGRESS_HEIGHT * self._properties.HEIGHT
        )
        rectInner = pygame.Rect(
            self._progressInnerX * self._properties.WIDTH,
            self._progressInnerYs[0] * self._properties.HEIGHT,
            self._progressInnerWidth * self._nailProgress * self._properties.WIDTH,
            self._progressInnerHeight * self._properties.HEIGHT
        )
        pygame.draw.rect(surface, color.COL_PUZZLE_PROGRESS_BAR_OUTER, rectOuter)
        if self._nailProgress < 0.7:
            col = color.COL_PUZZLE_PROGRESS_BAR_MIN
        elif self._nailProgress < 1:
            col = color.COL_PUZZLE_PROGRESS_BAR_MID
        else:
            col = color.COL_PUZZLE_PROGRESS_BAR_MAX

        pygame.draw.rect(surface, col, rectInner)

        # screw progress
        rectOuter = pygame.Rect(
            self._progressX * self._properties.WIDTH,
            self._progressYs[1] * self._properties.HEIGHT,
            self.PROGRESS_WIDTH * self._properties.WIDTH,
            self.PROGRESS_HEIGHT * self._properties.HEIGHT
        )
        rectInner = pygame.Rect(
            self._progressInnerX * self._properties.WIDTH,
            self._progressInnerYs[1] * self._properties.HEIGHT,
            self._progressInnerWidth * self._screwProgress * self._properties.WIDTH,
            self._progressInnerHeight * self._properties.HEIGHT
        )
        pygame.draw.rect(surface, color.COL_PUZZLE_PROGRESS_BAR_OUTER, rectOuter)
        if self._screwProgress < 0.7:
            col = color.COL_PUZZLE_PROGRESS_BAR_MIN
        elif self._screwProgress < 1:
            col = color.COL_PUZZLE_PROGRESS_BAR_MID
        else:
            col = color.COL_PUZZLE_PROGRESS_BAR_MAX
        pygame.draw.rect(surface, col, rectInner)

    def update(self, controller: InputHandler):
        self._nailTimer += self._properties.delta
        if self._nailTimer < 500:
            self._nailType = 'RED'
            self._nailProgress = 0.2
        elif self._nailTimer < 800:
            self._nailProgress = 0.8
        else:
            self._nailType = 'DONE'
            self._nailProgress = 1

        if self._nailTimer > 1000:
            self._nailTimer = 0

    def _recalculatePositions(self):
        if self._scrWidth != self._properties.WIDTH or self._scrHeight != self._properties.HEIGHT:
            self._scaleImages()
            self._calculateCoordinates()