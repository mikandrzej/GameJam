import os

import pygame
from pygame.surface import Surface

import color
from controllers.controller import Controller
from controllers.inputhandler import InputHandler
from properties import Properties
from state import State, GameState
from utils import Utils


class ControllerSelection:
    REQUIRED_CONTROLLERS = 3
    ICONS_SCALE_RATIO = 0.2
    VMARGIN = 0.1
    VMARGIN_LABEL = 0.5

    def __init__(self, properties: Properties, state: State):
        self.state = state
        self.properties = properties
        self._scaledImgGuitar = None
        self._scaledImgGamepad = None
        self._scaledImgBand = None
        self._imgGamepad = pygame.image.load(os.path.join('resources', 'gamepadIcon.png'))
        self._imgBand = pygame.image.load(os.path.join('resources', 'bandIcon.png'))
        self._imgGuitar = pygame.image.load(os.path.join('resources', 'guitarIcon.png'))
        self.images = [self._imgGamepad, self._imgBand, self._imgGuitar]
        self.scaledImages = [self._scaledImgGamepad, self._scaledImgBand, self._scaledImgGuitar]
        self.labels = ["Please press button on a Game Pad", "Please hit a Drum", "Please press button on a Guitar"]
        self.blockWidth = 0
        self.labelFont = pygame.font.Font(self.properties.labelControllerSelectionFont, self.properties.labelControllerSelectionSize)
        self.labelY = 0
        self.collectedControllers = []
        self.waitingForInputFrom = 0
        self.recalculatePositions()


    def update(self, controller: InputHandler):
        # temporary skip for selecting controllers
        if controller.getGenericButtons()[Controller.INP_ACCEPT]:
            self.state.gameState = GameState.SHELF
        if any(controller.getActiveJoysticks()):
            joyId = next(i for i, v in enumerate(controller.getActiveJoysticks()) if v)
            if joyId not in self.collectedControllers:
                controller.setController((Controller.CONTROLLERS[self.waitingForInputFrom], joyId))
                self.waitingForInputFrom += 1
                self.collectedControllers.append(joyId)

        if self.waitingForInputFrom >= self.REQUIRED_CONTROLLERS:
            self.state.gameState = GameState.SHELF

    def draw(self, surface: Surface):
        x = self.blockWidth / 2
        i = 0
        for scaledImg in self.scaledImages:
            centerX = x - (self.ICONS_SCALE_RATIO * self.properties.HEIGHT) / 2
            surface.blit(scaledImg, (centerX,
                                     self.properties.HEIGHT * self.VMARGIN))
            if self.waitingForInputFrom == i:
                TextSurf, TextRect = Utils.textGenerator(self.labels[i], self.labelFont, color.BLACK)
                TextRect.midtop = (centerX, self.labelY)
                surface.blit(TextSurf, TextRect)
            x += self.blockWidth
            i += 1

    def recalculatePositions(self):
        self.blockWidth = self.properties.WIDTH / self.REQUIRED_CONTROLLERS
        self.labelY = self.properties.HEIGHT * self.VMARGIN_LABEL
        i = 0
        for img in self.images:
            self.scaledImages[i] = pygame.transform.scale(img,
                                                          (int(self.ICONS_SCALE_RATIO * self.properties.HEIGHT),
                                                           int(self.ICONS_SCALE_RATIO * self.properties.HEIGHT)))
            i += 1
