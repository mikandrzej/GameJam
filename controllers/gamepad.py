from math import sqrt

import pygame

from controllers.controller import Controller


class Gamepad(Controller):
    def __init__(self):
        super().__init__()
        self.label = "Gamepad"
        self.leftStickDirections = {
            Controller.INP_UP: False,
            Controller.INP_RIGHT: False,
            Controller.INP_DOWN: False,
            Controller.INP_LEFT: False,
            Controller.INP_STICK_STILL: False
        }
        self.rightStickDirections = {
            Controller.INP_UP: False,
            Controller.INP_RIGHT: False,
            Controller.INP_DOWN: False,
            Controller.INP_LEFT: False,
            Controller.INP_STICK_STILL: False
        }
        self.axises = ((self.leftStickDirections, 0, 1, -1), (self.rightStickDirections, 4, 3, -1))
        self.emptyStickDirections = {
            Controller.INP_UP: False,
            Controller.INP_RIGHT: False,
            Controller.INP_DOWN: False,
            Controller.INP_LEFT: False,
            Controller.INP_STICK_STILL: False
        }
    GAMEPAD_MAP = {
        0: Controller.INP_ACCEPT,
        6: Controller.INP_PAUSE,
    }
    GAMEPAD_HAT_MAP = {
        (0, 1): Controller.INP_UP,
        (1, 0): Controller.INP_RIGHT,
        (0, -1): Controller.INP_DOWN,
        (-1, 0): Controller.INP_LEFT,
    }

    DEAD_ZONE = 0.1
    SCORE_THRESHOLD = 0.5

    def handleEvents(self, events, genericButtons):
        for event in events:
            if self.initState is False and hasattr(event, "joy") and event.joy == self.joystick.get_id():
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button in self.GAMEPAD_MAP.keys():  # if button mapper contains map for given key
                        genericButtons[self.GAMEPAD_MAP[event.button]] = True
                if event.type == pygame.JOYHATMOTION:
                    if event.value in self.GAMEPAD_HAT_MAP.keys():
                        genericButtons[self.GAMEPAD_HAT_MAP[event.value]] = True
                if event.type == pygame.JOYAXISMOTION:
                    self.handleAxises()
        # print(self.rightStickDirections)
        # print(self.leftStickDirections)

    def handleAxises(self):
        for axises in self.axises:
            axisXVal = self.joystick.get_axis(axises[1])
            axisYVal = self.joystick.get_axis(axises[2]) * axises[3]
            if sqrt(pow(axisXVal, 2) + pow(axisYVal, 2)) < self.DEAD_ZONE:
                direction = Controller.INP_STICK_STILL
            elif axisXVal > axisYVal > -1 * axisXVal:
                direction = Controller.INP_RIGHT
            elif axisYVal < axisXVal and axisYVal < -1 * axisXVal:
                direction = Controller.INP_DOWN
            elif axisXVal < axisYVal < -1 * axisXVal:
                direction = Controller.INP_LEFT
            else:
                direction = Controller.INP_UP

            for key in axises[0].keys():
                if direction == key:
                    axises[0][key] = True
                else:
                    axises[0][key] = False