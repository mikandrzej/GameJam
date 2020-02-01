import pygame

from controllers.controller import Controller


class Drums(Controller):
    def __init__(self):
        super().__init__()
        self.INP_UP = True
        self.label = "Drums"

    def handleEvents(self, events, genericButtons):
        for event in events:
            if self.initState is False and hasattr(event, "joy") and event.joy == self.joystick.get_id():
                if event.type == pygame.JOYBUTTONDOWN:
                    pass
                if event.type == pygame.JOYHATMOTION:
                    pass
                if event.type == pygame.JOYAXISMOTION:
                    pass