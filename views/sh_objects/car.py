import pygame
import color
import os

from controllers.controller import Controller
from state import State, GameState
from properties import Properties
from utils import Utils

class Car:
    ICON = pygame.image.load(os.path.join('resources', 'car_icon.png'))
    # IMG_CAR = pygame.image.load(os.path.join('resources', 'car.png'))
    #
    # PROGRESS_X = 0.8
    # PROGRESS_Y = 0.1
    # PROGRESS_WIDTH = 0.1
    # PROGRESS_HEIGHT = 0.025
    # PROGRESS_OFFSET = 0.03
    # PROGRESS_BOUND_WIDTH = 0.005
    # PROGRESS_TEXT_X = 0.95
    # PROGRESS_TEXT_NAIL = 'Nail'
    # PROGRESS_TEXT_SCREW = 'Screw'

    def __init__(self, properties: Properties, state: State):
        pass
        # self._properties = properties
        # self._state = state
        # self._scrWidth = properties.WIDTH
        # self._scrHeight = properties.HEIGHT
        #
        # self._scaleImages()
        # self._calculateCoordinates()

    def draw(self, surface: pygame.Surface):
        pass
        # self._drawProgress(surface)
        # self._drawFonts(surface)

    def _drawFonts(self, surface: pygame.Surface):
        #nail text
        self._progressNailFont = pygame.font.Font(self._properties.labelPuzzleProgressFont,
                                                  self._properties.labelPuzzleProgressSize)
        textSurf, textRect = Utils.textGenerator(self.PROGRESS_TEXT_NAIL,
                                                 self._progressNailFont,
                                                 color.COL_PUZZLE_NAIL_PROGRESS_TEXT)
        textRect.midtop = (self.PROGRESS_TEXT_X * self._properties.WIDTH,
                           self._progressYs[0] * self._properties.HEIGHT)
        surface.blit(textSurf, textRect)

        #screw text
        self._progressScrewFont = pygame.font.Font(self._properties.labelPuzzleProgressFont,
                                                  self._properties.labelPuzzleProgressSize)
        textSurf, textRect = Utils.textGenerator(self.PROGRESS_TEXT_SCREW,
                                                 self._progressNailFont,
                                                 color.COL_PUZZLE_SCREW_PROGRESS_TEXT)
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
        pass

    def _drawProgress(self, surface: pygame.Surface):
        pass
        # # nail progress
        # rectOuter = pygame.Rect(
        #     self._progressX * self._properties.WIDTH,
        #     self._progressYs[0] * self._properties.HEIGHT,
        #     self.PROGRESS_WIDTH * self._properties.WIDTH,
        #     self.PROGRESS_HEIGHT * self._properties.HEIGHT
        # )
        # rectInner = pygame.Rect(
        #     self._progressInnerX * self._properties.WIDTH,
        #     self._progressInnerYs[0] * self._properties.HEIGHT,
        #     self._progressInnerWidth * self._nailProgress * self._properties.WIDTH,
        #     self._progressInnerHeight * self._properties.HEIGHT
        # )
        # pygame.draw.rect(surface, color.COL_PUZZLE_PROGRESS_BAR_OUTER, rectOuter)
        # if self._nailProgress < 0.7:
        #     col = color.COL_PUZZLE_PROGRESS_BAR_MIN
        # elif self._nailProgress < 1:
        #     col = color.COL_PUZZLE_PROGRESS_BAR_MID
        # else:
        #     col = color.COL_PUZZLE_PROGRESS_BAR_MAX
        #
        # pygame.draw.rect(surface, col, rectInner)
        #
        # # screw progress
        # rectOuter = pygame.Rect(
        #     self._progressX * self._properties.WIDTH,
        #     self._progressYs[1] * self._properties.HEIGHT,
        #     self.PROGRESS_WIDTH * self._properties.WIDTH,
        #     self.PROGRESS_HEIGHT * self._properties.HEIGHT
        # )
        # rectInner = pygame.Rect(
        #     self._progressInnerX * self._properties.WIDTH,
        #     self._progressInnerYs[1] * self._properties.HEIGHT,
        #     self._progressInnerWidth * self._screwProgress * self._properties.WIDTH,
        #     self._progressInnerHeight * self._properties.HEIGHT
        # )
        # pygame.draw.rect(surface, color.COL_PUZZLE_PROGRESS_BAR_OUTER, rectOuter)
        # if self._screwProgress < 0.7:
        #     col = color.COL_PUZZLE_PROGRESS_BAR_MIN
        # elif self._screwProgress < 1:
        #     col = color.COL_PUZZLE_PROGRESS_BAR_MID
        # else:
        #     col = color.COL_PUZZLE_PROGRESS_BAR_MAX
        # pygame.draw.rect(surface, col, rectInner)

    def update(self, controller: Controller):
        pass
        # self._nailTimer += self._properties.delta
        # if self._nailTimer < 500:
        #     self._nailType = 'RED'
        #     self._nailProgress = 0.2
        # elif self._nailTimer < 800:
        #     self._nailProgress = 0.8
        # else:
        #     self._nailType = 'DONE'
        #     self._nailProgress = 1
        #
        # if self._nailTimer > 1000:
        #     self._nailTimer = 0

    def _recalculatePositions(self):
        pass
        # if self._scrWidth != self._properties.WIDTH or self._scrHeight != self._properties.HEIGHT:
        #     self._scaleImages()
        #     self._calculateCoordinates()