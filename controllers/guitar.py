import pygame

from controllers.controller import Controller


class Guitar(Controller):
    def __init__(self):
        super().__init__()
        self.label = "Guitar"

    def handleEvents(self, events, genericButtons):
        for event in events:
            if self.initState and event.type == pygame.JOYBUTTONDOWN:
                return event.joy
        return -1

    def handleEvents(self, events, genericButtons):
        for event in events:
            if self.initState is False and hasattr(event, "joy") and event.joy == self.joystick.get_id():
                if event.type == pygame.JOYBUTTONDOWN:
                    pass
                if event.type == pygame.JOYHATMOTION:
                    pass
                if event.type == pygame.JOYAXISMOTION:
                    pass