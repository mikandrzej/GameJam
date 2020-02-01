import pygame
import random
import os

import color
from properties import Properties
from views.sh_objects.objectA import ObjectA
from views.sh_objects.objectB import ObjectB
from views.sh_objects.objectC import ObjectC
from controller import Controller

OBJECTS = [
    ObjectA,
    ObjectB,
    ObjectC
]


class Bookstand:
    POS_X = 0.1
    POS_Y = 0.1
    WIDTH = 0.8
    HEIGHT = 0.8
    BOARD_THICKNESS = 0.01
    OFFSET_UP = 0.05
    OFFSET_DOWN = 0.17
    OBJECT_OFFSET = 0.03
    SHELFS = 5
    OBJECTS_ON_SHELF = 7
    SELECTED_RECT_OFFSET = 0.01
    SELECTED_RECT_WIDTH = 0.01

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

        self._imgBookstand = pygame.image.load(os.path.join('resources', 'regal.bmp'))

        self._calculateCoordinates()

        self._selectedObject = 0

    def _calculateCoordinates(self):
        self._shelfPositionX = self.POS_X + self.BOARD_THICKNESS
        self._shelfPositionsY = []
        for x in range(self.SHELFS):
            self._shelfPositionsY.append(self.POS_Y + self.OFFSET_UP + (x / self.SHELFS) * (self.HEIGHT - self.OFFSET_DOWN - self.OFFSET_UP))
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

        self._scaledImgBookstand = pygame.transform.scale(self._imgBookstand, (int(self.WIDTH * self.properties.WIDTH),
                                                                               int(self.HEIGHT * self.properties.HEIGHT)))
    def draw(self, surface: pygame.Surface):
        self._drawShelf(surface)
        self._drawObjects(surface)

    def update(self, controller: Controller):
        if controller.getButtons()[Controller.INP_RIGHT]:
            self._selectedObject += 1
        if controller.getButtons()[Controller.INP_LEFT]:
            self._selectedObject -= 1
        if controller.getButtons()[Controller.INP_DOWN]:
            self._selectedObject += self.OBJECTS_ON_SHELF
        if controller.getButtons()[Controller.INP_UP]:
            self._selectedObject -= self.OBJECTS_ON_SHELF
        self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS

    def _drawShelf(self, surface: pygame.Surface):
        area = pygame.Rect(self.POS_X * self.properties.WIDTH,
                           self.POS_Y * self.properties.HEIGHT,
                           self.WIDTH * self.properties.WIDTH,
                           self.HEIGHT * self.properties.HEIGHT)
        surface.blit(self._scaledImgBookstand, area)


    def _drawObjects(self, surface: pygame.Surface):
        for ind, obj in enumerate(self._objects):
            area = pygame.Rect(self._objPositionsX[ind] * self.properties.WIDTH,
                               self._objPositionsY[ind] * self.properties.HEIGHT,
                               self._objectWidth * self.properties.WIDTH,
                               self._objectHeight * self.properties.HEIGHT)
            objSurface = pygame.Surface((area.width, area.height))
            obj.draw(objSurface)
            surface.blit(objSurface, area)
            if self._selectedObject == ind:
                rect = pygame.Rect((self._objPositionsX[ind] - self.SELECTED_RECT_OFFSET) * self.properties.WIDTH,
                                    (self._objPositionsY[ind] - self.SELECTED_RECT_OFFSET) * self.properties.HEIGHT,
                                    (self._objectWidth + self.SELECTED_RECT_OFFSET * 2) * self.properties.WIDTH,
                                    (self._objectHeight + self.SELECTED_RECT_OFFSET * 2) * self.properties.HEIGHT
                                    )
                pygame.draw.rect(surface, color.COL_SELECTED, rect, 5)

    def recalculatePositions(self):
        if self._scrWidth != self.properties.WIDTH or self._scrHeight != self.properties.HEIGHT:
            self._calculateCoordinates()