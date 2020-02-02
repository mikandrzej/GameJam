from enum import IntEnum

import pygame

from controllers.controller import Controller, ControllerInput


class Guitar(Controller):
    GUITAR_HAT_MAP = {
        (0, 1): Controller.INP_UP,
        (0, -1): Controller.INP_DOWN,
        (0, 0): ControllerInput.BAR_STILL,
    }
    GAMEPAD_MAP = {
        0: Controller.INP_ACCEPT,
        6: Controller.INP_PAUSE,
    }
    TILT_AXIS = 4
    METAL_AXIS = 3

    def __init__(self):
        super().__init__()
        self.label = "Guitar"
        self.emptyInput = {
            ControllerInput.GREEN: False,
            ControllerInput.RED: False,
            ControllerInput.BLUE: False,
            ControllerInput.ORANGE: False,
            ControllerInput.YELLOW: False,
            ControllerInput.BAR_UP: False,
            ControllerInput.BAR_DOWN: False,
            ControllerInput.BAR_STILL: False,
        }
        self.inputMetal = {
            ControllerInput.METAL_UP: True,
            ControllerInput.METAL_DOWN: False,
        }
        self.inputTilt = {
            ControllerInput.TILT_STILL: True,
            ControllerInput.TILT_DOWN: False,
            ControllerInput.TILT_UP: False,
        }
        self.input = self.emptyInput.copy()


    def handleEvents(self, events, genericButtons):
        self.input = self.emptyInput.copy()
        for event in events:
            if self.initState is False and hasattr(event, "joy") and event.joy == self.joystick.get_id():
                if event.type == pygame.JOYBUTTONDOWN:
                    self.input[event.button] = True
                if event.type == pygame.JOYHATMOTION:
                    if event.value in self.GUITAR_HAT_MAP.keys():
                        genericButtons[self.GUITAR_HAT_MAP[event.value]] = True
                        if self.GUITAR_HAT_MAP[event.value] == Controller.INP_UP:
                            self.input[ControllerInput.BAR_UP] = True
                        elif self.GUITAR_HAT_MAP[event.value] == Controller.INP_DOWN:
                            self.input[ControllerInput.BAR_DOWN] = True
                        else:
                            self.input[ControllerInput.BAR_STILL] = True
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == self.METAL_AXIS:
                        if event.value >= 0.25:
                            self.inputMetal[ControllerInput.METAL_DOWN] = True
                            self.inputMetal[ControllerInput.METAL_UP] = False
                        elif event.value < -0.25:
                            self.inputMetal[ControllerInput.METAL_UP] = True
                            self.inputMetal[ControllerInput.METAL_DOWN] = False
                    elif event.axis == self.TILT_AXIS:
                        if event.value >= 0.25:
                            self.inputTilt[ControllerInput.TILT_DOWN] = True
                            self.inputTilt[ControllerInput.TILT_STILL] = False
                            self.inputTilt[ControllerInput.TILT_UP] = False
                        elif 0.25 > event.value > -0.25:
                            self.inputTilt[ControllerInput.TILT_STILL] = True
                            self.inputTilt[ControllerInput.TILT_DOWN] = False
                            self.inputTilt[ControllerInput.TILT_UP] = False
                        elif event.value < -0.25:
                            self.inputTilt[ControllerInput.TILT_UP] = True
                            self.inputTilt[ControllerInput.TILT_STILL] = False
                            self.inputTilt[ControllerInput.TILT_DOWN] = False
