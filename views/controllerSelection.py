import os

import pygame
from pygame.surface import Surface

import color
from controller import Controller
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
        self._scaledImgGamePad = None
        self._scaledImgBand = None
        self._imgGamePad = pygame.image.load(os.path.join('resources', 'gamepadIcon.png'))
        self._imgBand = pygame.image.load(os.path.join('resources', 'bandIcon.png'))
        self._imgGuitar = pygame.image.load(os.path.join('resources', 'guitarIcon.png'))
        self.images = [self._imgGamePad, self._imgBand, self._imgGuitar]
        self.scaledImages = [self._scaledImgGamePad, self._scaledImgBand, self._scaledImgGuitar]
        self.labels = ["Please press button on a Game Pad", "Please hit a Drum", "Please press button on a Guitar"]
        self.controllers = ["GamePad", "Drums", "Guitar"]
        self.blockWidth = 0
        self.labelFont = pygame.font.Font(self.properties.labelControllerSelectionFont, self.properties.labelControllerSelectionSize)
        self.labelY = 0
        self.collectedControllers = []
        self.waitingForInputFrom = 0
        self.recalculatePositions()


    def update(self, controller: Controller):
        # temporary skip for selecting controllers
        if controller.getKeyboardButtons()[Controller.INP_ACCEPT]:
            self.state.gameState = GameState.SHELF
        if any(controller.getActivatedJoysticks()):
            joyId = next(i for i, v in enumerate(controller.getActivatedJoysticks()) if v)
            if joyId not in self.collectedControllers:
                controller.setController((self.controllers[self.waitingForInputFrom], joyId))
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
