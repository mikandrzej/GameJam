import pygame


class Controller:
    INP_PAUSE = 0
    INP_UP = 1
    INP_RIGHT = 2
    INP_DOWN = 4
    INP_LEFT = 8

    def __init__(self):
        self.emptyButtons = {
            self.INP_PAUSE: False,
            self.INP_UP: False,
            self.INP_RIGHT: False,
            self.INP_DOWN: False,
            self.INP_LEFT: False
        }
        self.buttons = self.emptyButtons.copy()

    def handleEvents(self, events):
        self.buttons = self.emptyButtons.copy()
        for event in events:  # gets all the events which have occured till now and keeps tab of them.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.buttons[self.INP_PAUSE] = True
                elif event.key == pygame.K_UP:
                    self.buttons[self.INP_UP] = True
                elif event.key == pygame.K_RIGHT:
                    self.buttons[self.INP_RIGHT] = True
                elif event.key == pygame.K_DOWN:
                    self.buttons[self.INP_DOWN] = True
                elif event.key == pygame.K_LEFT:
                    self.buttons[self.INP_LEFT] = True

    def getButtons(self):
        return self.buttons
