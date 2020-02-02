import pygame
import color
import os

from controllers.controller import Controller
from state import State, GameState
from properties import Properties
from utils import Utils

class Car:
    ICON = pygame.image.load(os.path.join('resources', 'car_icon.png'))
    IMG_CAR = pygame.image.load(os.path.join('resources', 'car3.png'))
    IMGS_JACK = {
        'BLACK' :   pygame.image.load(os.path.join('resources', 'car_jack.png')),
        'RED'   :   pygame.image.load(os.path.join('resources', 'car_jack_red.png')),
        'BLUE'   :   pygame.image.load(os.path.join('resources', 'car_jack_blue.png')),
        'GREEN'   :   pygame.image.load(os.path.join('resources', 'car_jack_green.png')),
        'VIOLET'   :   pygame.image.load(os.path.join('resources', 'car_jack_violet.png')),
        'DONE'   :   pygame.image.load(os.path.join('resources', 'car_jack_done.png'))
    }
    IMGS_SCREW = {
        'BLACK' :   pygame.image.load(os.path.join('resources', 'screw.png')),
        'RED'   :   pygame.image.load(os.path.join('resources', 'screw_red.png')),
        'BLUE'   :   pygame.image.load(os.path.join('resources', 'screw_blue.png')),
        'GREEN'   :   pygame.image.load(os.path.join('resources', 'screw_green.png')),
        'VIOLET'   :   pygame.image.load(os.path.join('resources', 'screw_violet.png')),
        'DONE'   :   pygame.image.load(os.path.join('resources', 'screw_done.png'))
    }
    IMGS_LOCK = {
        'BLACK' :   pygame.image.load(os.path.join('resources', 'lock.png')),
        'RED'   :   pygame.image.load(os.path.join('resources', 'lock_red.png')),
        'BLUE'   :   pygame.image.load(os.path.join('resources', 'lock_blue.png')),
        'GREEN'   :   pygame.image.load(os.path.join('resources', 'lock_green.png')),
        'VIOLET'   :   pygame.image.load(os.path.join('resources', 'lock_violet.png')),
        'DONE'   :   pygame.image.load(os.path.join('resources', 'lock_done.png'))
    }
    CAR_X = 0.1
    CAR_Y = 0.1
    CAR_WIDTH = 0.8
    CAR_HEIGHT = 0.8

    JACK_X = 0.2
    JACK_Y = 0.45
    JACK_WIDTH = 0.25
    JACK_HEIGHT = 0.3
    JACK_ROTATE = 0

    SCREW_X = 0.44
    SCREW_Y = 0.4
    SCREW_WIDTH = 0.2
    SCREW_HEIGHT = SCREW_WIDTH / 1.164179104477612
    SCREW_ROTATE = 0

    LOCK_X = 0.35
    LOCK_Y = 0.25
    LOCK_WIDTH = 0.1
    LOCK_HEIGHT = LOCK_WIDTH / 1.164179104477612
    LOCK_ROTATE = 0

    PROGRESS_X = 0.8
    PROGRESS_Y = 0.1
    PROGRESS_WIDTH = 0.1
    PROGRESS_HEIGHT = 0.025
    PROGRESS_OFFSET = 0.03
    PROGRESS_BOUND_WIDTH = 0.005
    PROGRESS_TEXT_X = 0.95
    PROGRESS_TEXT_JACK = 'Jack'
    PROGRESS_TEXT_SCREW = 'Screw'
    PROGRESS_TEXT_LOCK = 'Lock'

    def __init__(self, properties: Properties, state: State):
        pass
        self._properties = properties
        self._state = state
        self._scrWidth = properties.WIDTH
        self._scrHeight = properties.HEIGHT

        self._jackType = 'GREEN'
        self._screwType = 'RED'
        self._lockType = 'RED'

        self._jackProgress = 0
        self._screwProgress = 0
        self._lockProgress = 0

        self._scaleImages()
        self._calculateCoordinates()

    def draw(self, surface: pygame.Surface):
        self._recalculatePositions()
        surface.blit(self._scaledCar,
                     pygame.Rect(self.CAR_X * self._properties.WIDTH,
                                 self.CAR_Y * self._properties.HEIGHT,
                                 self.CAR_WIDTH * self._properties.WIDTH,
                                 self.CAR_HEIGHT * self._properties.HEIGHT))
        surface.blit(self._scaledJacks[self._jackType],
                     pygame.Rect(self.JACK_X * self._properties.WIDTH,
                                self.JACK_Y * self._properties.HEIGHT,
                                self.JACK_WIDTH * self._properties.WIDTH,
                                self.JACK_HEIGHT * self._properties.HEIGHT))
        surface.blit(self._scaledScrews[self._screwType],
                     pygame.Rect(self.SCREW_X * self._properties.WIDTH,
                                self.SCREW_Y * self._properties.HEIGHT,
                                self.SCREW_WIDTH * self._properties.WIDTH,
                                self.SCREW_HEIGHT * self._properties.HEIGHT))
        surface.blit(self._scaledLocks[self._lockType],
                     pygame.Rect(self.LOCK_X * self._properties.WIDTH,
                                self.LOCK_Y * self._properties.HEIGHT,
                                self.LOCK_WIDTH * self._properties.WIDTH,
                                self.LOCK_HEIGHT * self._properties.HEIGHT))
        self._drawProgress(surface)
        self._drawFonts(surface)

    def _drawFonts(self, surface: pygame.Surface):
        #nail text
        self._progressFont = pygame.font.Font(self._properties.labelPuzzleProgressFont,
                                              self._properties.labelPuzzleProgressSize)
        textSurf, textRect = Utils.textGenerator(self.PROGRESS_TEXT_JACK,
                                                 self._progressFont,
                                                 color.COL_PUZZLE_PROGRESS_TEXT)
        textRect.midtop = (self.PROGRESS_TEXT_X * self._properties.WIDTH,
                           self._progressYs[0] * self._properties.HEIGHT)
        surface.blit(textSurf, textRect)

        #screw text
        self._progressFont = pygame.font.Font(self._properties.labelPuzzleProgressFont,
                                              self._properties.labelPuzzleProgressSize)
        textSurf, textRect = Utils.textGenerator(self.PROGRESS_TEXT_SCREW,
                                                 self._progressFont,
                                                 color.COL_PUZZLE_PROGRESS_TEXT)
        textRect.midtop = (self.PROGRESS_TEXT_X * self._properties.WIDTH,
                           self._progressYs[1] * self._properties.HEIGHT)
        surface.blit(textSurf, textRect)

        #lock text
        self._progressFont = pygame.font.Font(self._properties.labelPuzzleProgressFont,
                                              self._properties.labelPuzzleProgressSize)
        textSurf, textRect = Utils.textGenerator(self.PROGRESS_TEXT_LOCK,
                                                 self._progressFont,
                                                 color.COL_PUZZLE_PROGRESS_TEXT)
        textRect.midtop = (self.PROGRESS_TEXT_X * self._properties.WIDTH,
                           self._progressYs[2] * self._properties.HEIGHT)
        surface.blit(textSurf, textRect)

    def _calculateCoordinates(self):
        pass
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
        self._scaledCar = pygame.transform.scale(self.IMG_CAR,
                                                 (int(self.CAR_WIDTH * self._properties.WIDTH),
                                                int(self.CAR_HEIGHT * self._properties.HEIGHT)))
        self._scaledJacks = {}
        for nail in self.IMGS_JACK:
            rotJack = pygame.transform.rotate(self.IMGS_JACK[nail], self.JACK_ROTATE)
            self._scaledJacks[nail] = pygame.transform.scale(rotJack,
                                                      (int(self.JACK_WIDTH * self._properties.WIDTH),
                                                        int(self.JACK_HEIGHT * self._properties.HEIGHT)))
        self._scaledScrews = {}
        for screw in self.IMGS_SCREW:
            rotScrew = pygame.transform.rotate(self.IMGS_SCREW[screw], self.SCREW_ROTATE)
            self._scaledScrews[screw] = pygame.transform.scale(rotScrew,
                                                      (int(self.SCREW_WIDTH * self._properties.WIDTH),
                                                        int(self.SCREW_HEIGHT * self._properties.HEIGHT)))
        self._scaledLocks = {}
        for lock in self.IMGS_LOCK:
            rotLock = pygame.transform.rotate(self.IMGS_LOCK[lock], self.LOCK_ROTATE)
            self._scaledLocks[lock] = pygame.transform.scale(rotLock,
                                                      (int(self.LOCK_WIDTH * self._properties.WIDTH),
                                                        int(self.LOCK_HEIGHT * self._properties.HEIGHT)))

    def _drawProgress(self, surface: pygame.Surface):
        pass
        # jack progress
        rectOuter = pygame.Rect(
            self._progressX * self._properties.WIDTH,
            self._progressYs[0] * self._properties.HEIGHT,
            self.PROGRESS_WIDTH * self._properties.WIDTH,
            self.PROGRESS_HEIGHT * self._properties.HEIGHT
        )
        rectInner = pygame.Rect(
            self._progressInnerX * self._properties.WIDTH,
            self._progressInnerYs[0] * self._properties.HEIGHT,
            self._progressInnerWidth * self._jackProgress * self._properties.WIDTH,
            self._progressInnerHeight * self._properties.HEIGHT
        )
        pygame.draw.rect(surface, color.COL_PUZZLE_PROGRESS_BAR_OUTER, rectOuter)
        if self._jackProgress < 0.7:
            col = color.COL_PUZZLE_PROGRESS_BAR_MIN
        elif self._jackProgress < 1:
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

        # lock progress
        rectOuter = pygame.Rect(
            self._progressX * self._properties.WIDTH,
            self._progressYs[2] * self._properties.HEIGHT,
            self.PROGRESS_WIDTH * self._properties.WIDTH,
            self.PROGRESS_HEIGHT * self._properties.HEIGHT
        )
        rectInner = pygame.Rect(
            self._progressInnerX * self._properties.WIDTH,
            self._progressInnerYs[2] * self._properties.HEIGHT,
            self._progressInnerWidth * self._lockProgress * self._properties.WIDTH,
            self._progressInnerHeight * self._properties.HEIGHT
        )
        pygame.draw.rect(surface, color.COL_PUZZLE_PROGRESS_BAR_OUTER, rectOuter)
        if self._lockProgress < 0.7:
            col = color.COL_PUZZLE_PROGRESS_BAR_MIN
        elif self._lockProgress < 1:
            col = color.COL_PUZZLE_PROGRESS_BAR_MID
        else:
            col = color.COL_PUZZLE_PROGRESS_BAR_MAX
        pygame.draw.rect(surface, col, rectInner)

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
        if self._scrWidth != self._properties.WIDTH or self._scrHeight != self._properties.HEIGHT:
            self._scaleImages()
            self._calculateCoordinates()