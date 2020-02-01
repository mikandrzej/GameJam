import pygame


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