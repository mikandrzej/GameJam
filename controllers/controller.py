from enum import IntEnum

import pygame

class ControllerInput:
    GREEN = 0
    RED = 1
    BLUE = 2
    ORANGE = 5
    YELLOW = 3
    PEDAL = 4
    METAL_UP = 5
    METAL_DOWN = 6
    BAR_UP = 7
    BAR_DOWN = 8
    BAR_STILL = 9
    TILT_UP = 10
    TILT_DOWN = 11
    all = [
        GREEN,
        RED,
        BLUE,
        ORANGE,
        YELLOW,
        PEDAL,
        METAL_UP,
        METAL_DOWN,
        BAR_UP,
        BAR_DOWN,
        BAR_STILL,
        TILT_UP,
        TILT_DOWN
    ]



class Controller:
    INP_PAUSE = 0
    INP_UP = 1
    INP_RIGHT = 2
    INP_DOWN = 4
    INP_LEFT = 8
    INP_ACCEPT = 16
    INP_STICK_STILL = 32
    CONTROLLERS = ("Gamepad", "Drums", "Guitar")

    def __init__(self):
        self.joystick = None
        self.initState = True

    def initController(self, events):
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                return event.joy
        return -1

    def handleEvents(self, events, genericButtons):
        pass

    def setJoystick(self, joystick):
        self.joystick = joystick
        self.initState = False