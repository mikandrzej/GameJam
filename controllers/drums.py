from enum import Enum, IntEnum

import pygame

from controllers.controller import Controller, ControllerInput


class Drums(Controller):
    DRUM_MAP = {
        7: Controller.INP_ACCEPT,
        6: Controller.INP_PAUSE
    }
    def __init__(self):
        super().__init__()
        self.emptyInput = {
            ControllerInput.GREEN: False,
            ControllerInput.RED: False,
            ControllerInput.BLUE: False,
            ControllerInput.ORANGE: False,
            ControllerInput.YELLOW: False,
            ControllerInput.PEDAL: False
        }
        self.input = self.emptyInput.copy()
        self.label = "Drums"

    def handleEvents(self, events, genericButtons):
        self.input = self.emptyInput.copy()
        for event in events:
            if self.initState is False and hasattr(event, "joy") and event.joy == self.joystick.get_id():
                self.input = self.emptyInput.copy()
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button in ControllerInput.all: # it should be DrumInput?
                        if event.button in self.DRUM_MAP.keys():
                            genericButtons[self.DRUM_MAP[event.button]] = True
                        self.input[event.button] = True
