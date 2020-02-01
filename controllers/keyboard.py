import pygame

from controllers.controller import Controller


class Keyboard(Controller):
    def __init__(self):
        super().__init__()
        self.joystick = None

    def handleEvents(self, events, genericButtons):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    genericButtons[Controller.INP_PAUSE] = True
                elif event.key == pygame.K_UP:
                    genericButtons[Controller.INP_UP] = True
                elif event.key == pygame.K_RIGHT:
                    genericButtons[Controller.INP_RIGHT] = True
                elif event.key == pygame.K_DOWN:
                    genericButtons[Controller.INP_DOWN] = True
                elif event.key == pygame.K_LEFT:
                    genericButtons[Controller.INP_LEFT] = True
                elif event.key == pygame.K_RETURN:
                    genericButtons[Controller.INP_ACCEPT] = True

    def setJoystick(self, joystick):
        raise Exception("Trying to set joystick to keyboard")