from enum import Enum, IntEnum

import pygame

from controllers.controller import Controller

class DrumsInput(IntEnum):
    GREEN = 0
    RED = 1
    BLUE = 2
    ORANGE = 5
    YELLOW = 3
    PEDAL = 4

class Drums(Controller):
    DRUM_MAP = {
        0: Controller.INP_ACCEPT,
        1: Controller.INP_PAUSE,
    }
    def __init__(self):
        super().__init__()
        self.emptyInput = {
            DrumsInput.GREEN: False,
            DrumsInput.RED: False,
            DrumsInput.BLUE: False,
            DrumsInput.ORANGE: False,
            DrumsInput.YELLOW: False,
            DrumsInput.PEDAL: False
        }
        self.input = self.emptyInput.copy()
        self.label = "Drums"

    def handleEvents(self, events, genericButtons):
        for event in events:
            if self.initState is False and hasattr(event, "joy") and event.joy == self.joystick.get_id():
                self.input = self.emptyInput.copy()
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button in list(map(int, DrumsInput)):
                        if event.button in self.DRUM_MAP.keys():
                            genericButtons[self.DRUM_MAP[event.button]] = True
                        self.input[event.button] = True
