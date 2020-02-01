import pygame

from controllers.controller import Controller


class Gamepad(Controller):
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


    LEFT_STICK = (0, 1)
    RIGHT_STICK = (0, 1)

    def handleEvents(self, events, genericButtons):
        for event in events:
            # dodaj filtrowanie per zapisane id joya
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button in self.GAMEPAD_MAP.keys():  # if button mapper contains map for given key
                    genericButtons[self.GAMEPAD_MAP[event.button]] = True
            if event.type == pygame.JOYHATMOTION:
                if event.value in self.GAMEPAD_HAT_MAP.keys():
                    genericButtons[self.GAMEPAD_HAT_MAP[event.value]] = True
            if event.type == pygame.JOYAXISMOTION:
                pass
