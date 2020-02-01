import pygame

from controllers.controller import Controller


class Guitar(Controller):
    def __init__(self):
        super().__init__()

    def handleEvents(self, events, genericButtons):
        for event in events:
            if self.initState and event.type == pygame.JOYBUTTONDOWN:
                return event.joy
        return -1