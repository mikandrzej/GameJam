import pygame
import random

import color
from properties import Properties
from views.sh_objects.objectA import ObjectA

OBJECTS = [
    ObjectA,
    ObjectA,
    ObjectA,
    ObjectA
]


class Bookstand:
    POS_X = 0.2
    POS_Y = 0.2
    WIDTH = 0.6
    HEIGHT = 0.6
    BOARD_THICKNESS = 0.01
    OBJECT_OFFSET = 0.03
    SHELFS = 3
    OBJECTS_ON_SHELF = 5

    def __init__(self, properties: Properties):
        self.properties = properties
        self._scrWidth = properties.WIDTH
        self._scrHeight = properties.HEIGHT

        objects = []
        for x in range(self.OBJECTS_ON_SHELF * self.SHELFS):
            rand = random.randrange(len(OBJECTS))
            object = OBJECTS[rand]()
            objects.append(object)
        self._objects = objects

        self._calculateCoordinates()

    def _calculateCoordinates(self):
        self._shelfPositionX = self.POS_X + self.BOARD_THICKNESS
        self._shelfPositionsY = []
        for x in range(self.SHELFS):
            self._shelfPositionsY.append(self.POS_Y + self.BOARD_THICKNESS + (x / self.SHELFS) * (self.HEIGHT - self.BOARD_THICKNESS))
        self._shelfWidth = self.WIDTH - 2 * self.BOARD_THICKNESS
        self._shelfHeight = (self.HEIGHT - self.BOARD_THICKNESS) / self.SHELFS - self.BOARD_THICKNESS

        self._objectWidth = (self._shelfWidth - self.OBJECT_OFFSET) / self.OBJECTS_ON_SHELF - self.OBJECT_OFFSET
        self._objectHeight = self._shelfHeight - 2 * self.OBJECT_OFFSET

        self._objPositionsX = []
        for x in range(self.OBJECTS_ON_SHELF * self.SHELFS):
            self._objPositionsX.append(self._shelfPositionX + self.OBJECT_OFFSET + (x % self.OBJECTS_ON_SHELF) * (self._objectWidth + self.OBJECT_OFFSET))
        self._objPositionsY = []
        for y in range(self.OBJECTS_ON_SHELF * self.SHELFS):
            self._objPositionsY.append(self._shelfPositionsY[y // self.OBJECTS_ON_SHELF] + self.OBJECT_OFFSET)

    def draw(self, surface: pygame.Surface):
        self._drawShelf(surface)
        self._drawObjects(surface)

    def _drawShelf(self, surface: pygame.Surface):
        bookstand = pygame.Rect(self.POS_X * self.properties.WIDTH,
                                self.POS_Y * self.properties.HEIGHT,
                                self.WIDTH * self.properties.WIDTH,
                                self.HEIGHT * self.properties.HEIGHT
                                )

        shelfs = []
        for y in range(self.SHELFS):
            shelf = pygame.Rect(self._shelfPositionX * self.properties.WIDTH,
                                self._shelfPositionsY[y] * self.properties.HEIGHT,
                                self._shelfWidth * self.properties.WIDTH,
                                self._shelfHeight * self.properties.HEIGHT
                                )
            shelfs.append(shelf)

        pygame.draw.rect(surface, color.COL_BOOKSTAND, bookstand)
        for shelf in shelfs:
            pygame.draw.rect(surface, color.COL_SHELF, shelf)

    def _drawObjects(self, surface: pygame.Surface):
        for ind, obj in enumerate(self._objects):
            area = pygame.Rect(self._objPositionsX[ind] * self.properties.WIDTH,
                               self._objPositionsY[ind] * self.properties.HEIGHT,
                               self._objectWidth * self.properties.WIDTH,
                               self._objectHeight * self.properties.HEIGHT)
            objSurface = pygame.Surface((area.width, area.height))
            obj.draw(objSurface)
            surface.blit(objSurface, area)

    def recalculatePositions(self):
        if self._scrWidth != self.properties.WIDTH or self._scrHeight != self.properties.HEIGHT:
            self._calculateCoordinates()