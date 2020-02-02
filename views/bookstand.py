import pygame
import random
import os

import color
from controllers.controller import Controller
from controllers.inputhandler import InputHandler
from properties import Properties
from views.sh_objects.wardrobe import Wardrobe
from views.sh_objects.car import Car
from state import State, GameState

OBJECTS = [
    None,
    Wardrobe,
    Car
]

class Bookstand:
    POS_X = 0.1
    POS_Y = 0.1
    WIDTH = 0.8
    HEIGHT = 0.8
    BOARD_THICKNESS = 0.1
    OFFSET_UP = 0.15
    OFFSET_DOWN = 0.2
    OBJECT_OFFSET = 0.04
    SHELFS = 2
    OBJECTS_ON_SHELF = 4
    SELECTED_RECT_OFFSET = 0.01
    SELECTED_RECT_WIDTH = 0.01

    def __init__(self, properties: Properties, state: State):
        self._properties = properties
        self._scrWidth = properties.WIDTH
        self._scrHeight = properties.HEIGHT
        self._state = state

        objects = []
        for x in range(self.OBJECTS_ON_SHELF * self.SHELFS):
            rand = random.randrange(len(OBJECTS))
            if OBJECTS[rand] != None:
                object = OBJECTS[rand](self._properties, self._state)
                objects.append(object)
                self._selectedObject = x
            else:
                objects.append(None)
        self._objects = objects

        self._imgBookstand = pygame.image.load(os.path.join('resources', 'regal.bmp'))

        self._calculateCoordinates()

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

        self._scaledImgBookstand = pygame.transform.scale(self._imgBookstand, (int(self.WIDTH * self._properties.WIDTH),
                                                                               int(self.HEIGHT * self._properties.HEIGHT)))
        for obj in self._objects:
            if obj == None:
                continue
            obj._scaledIcon = pygame.transform.scale(obj.ICON, (int(self._objectWidth * self._properties.WIDTH),
                                                                               int(self._objectHeight * self._properties.HEIGHT)))
    def draw(self, surface: pygame.Surface):
        if self._state.gameState == GameState.SHELF:
            self._drawShelf(surface)
            self._drawObjects(surface)
        elif self._state.gameState == GameState.PUZZLE:
            if self._objects[self._selectedObject] != None:
                self._objects[self._selectedObject].draw(surface)

    def update(self, controller: InputHandler):
        if self._state.gameState == GameState.SHELF:
            if controller.getGenericButtons()[Controller.INP_RIGHT]:
                self._selectedObject += 1
                self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS
                while(self._objects[self._selectedObject] == None):
                    self._selectedObject += 1
                    self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS
            if controller.getGenericButtons()[Controller.INP_LEFT]:
                self._selectedObject -= 1
                self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS
                while(self._objects[self._selectedObject] == None):
                    self._selectedObject -= 1
                    self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS
            if controller.getGenericButtons()[Controller.INP_DOWN]:
                self._selectedObject += self.OBJECTS_ON_SHELF
                self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS
                while(self._objects[self._selectedObject] == None):
                    self._selectedObject += 1
                    self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS
            if controller.getGenericButtons()[Controller.INP_UP]:
                self._selectedObject -= self.OBJECTS_ON_SHELF
                self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS
                while(self._objects[self._selectedObject] == None):
                    self._selectedObject -= 1
                    self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS
            self._selectedObject %= self.OBJECTS_ON_SHELF * self.SHELFS
            if controller.getGenericButtons()[Controller.INP_ACCEPT]:
                self._state.gameState = GameState.PUZZLE
        elif self._state.gameState == GameState.PUZZLE:
            self._objects[self._selectedObject].update(controller)


    def _drawShelf(self, surface: pygame.Surface):
        area = pygame.Rect(self.POS_X * self._properties.WIDTH,
                           self.POS_Y * self._properties.HEIGHT,
                           self.WIDTH * self._properties.WIDTH,
                           self.HEIGHT * self._properties.HEIGHT)
        surface.blit(self._scaledImgBookstand, area)


    def _drawObjects(self, surface: pygame.Surface):
        for ind, obj in enumerate(self._objects):
            if obj == None:
                continue
            area = pygame.Rect(self._objPositionsX[ind] * self._properties.WIDTH,
                               self._objPositionsY[ind] * self._properties.HEIGHT,
                               self._objectWidth * self._properties.WIDTH,
                               self._objectHeight * self._properties.HEIGHT)
            # objSurface = pygame.Surface((area.width, area.height))
            # obj.draw(objSurface)
            surface.blit(obj._scaledIcon, area)
            if self._selectedObject == ind:
                rect = pygame.Rect((self._objPositionsX[ind] - self.SELECTED_RECT_OFFSET) * self._properties.WIDTH,
                                   (self._objPositionsY[ind] - self.SELECTED_RECT_OFFSET) * self._properties.HEIGHT,
                                   (self._objectWidth + self.SELECTED_RECT_OFFSET * 2) * self._properties.WIDTH,
                                   (self._objectHeight + self.SELECTED_RECT_OFFSET * 2) * self._properties.HEIGHT
                                   )
                pygame.draw.rect(surface, color.COL_SELECTED, rect, 5)

    def recalculatePositions(self):
        if self._scrWidth != self._properties.WIDTH or self._scrHeight != self._properties.HEIGHT:
            self._calculateCoordinates()