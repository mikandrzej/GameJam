import math
from math import cos, sin, atan2

import pygame

from controllers.controller import Controller
from controllers.drums import Drums
from controllers.gamepad import Gamepad
from controllers.guitar import Guitar
from controllers.keyboard import Keyboard


class InputHandler:
    def __init__(self):
        self.gamepad = Gamepad()
        self.guitar = Guitar()
        self.drums = Drums()
        self.keyboard = Keyboard()
        self.emptyGenericButtons = {
            Controller.INP_PAUSE: False,
            Controller.INP_UP: False,
            Controller.INP_RIGHT: False,
            Controller.INP_DOWN: False,
            Controller.INP_LEFT: False,
            Controller.INP_ACCEPT: False
        }
        self.genericButtons = self.emptyGenericButtons.copy()
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        self.activeJoysticks = pygame.joystick.get_count() * [False]
        for joy in self.joysticks:
            joy.init()

    def initControllers(self, events):
        activatedController = self.gamepad.initController(events) # get id of last used controller not exactly gamepad
        if activatedController != -1:
            self.activeJoysticks[activatedController] = True

    def handleEvents(self, events):
        if False in self.activeJoysticks:
            self.activeJoysticks = pygame.joystick.get_count() * [False]
            self.initControllers(events)

        self.genericButtons = self.emptyGenericButtons.copy()
        self.keyboard.handleEvents(events, self.genericButtons)
        self.gamepad.handleEvents(events, self.genericButtons)
        self.drums.handleEvents(events, self.genericButtons)
        self.guitar.handleEvents(events, self.genericButtons)

    def getActiveJoysticks(self):
        return self.activeJoysticks

    def getGenericButtons(self):
        return self.genericButtons

    def setController(self, whichController):
        targetGamepad = next(x for x in [self.gamepad, self.drums, self.guitar] if x.label == whichController[0])
        targetGamepad.setJoystick(next(x for x in self.joysticks if x.get_id() == whichController[1]))
        targetGamepad.initState = False


