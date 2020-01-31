import pygame

from properties import Properties

class Bookstand:
    POS_X = 0.2
    POS_Y = 0.2
    WIDTH = 0.6
    HEIGHT = 0.6

    COLOR = (0,0,0)

    def __init__(self, properties: Properties):
        self.properties = properties

    def draw(self, surface: pygame.Surface):
        self._drawShelf(surface)

    def _drawShelf(self, surface: pygame.Surface):
        bookstand = pygame.Rect(self.POS_X * self.properties.WIDTH,
                            self.POS_X * self.properties.HEIGHT,
                            self.WIDTH * self.properties.WIDTH,
                            self.HEIGHT * self.properties.HEIGHT
                            )
        pygame.draw.rect(surface, self.COLOR, bookstand)
        bookstand = pygame.Rect(self.POS_X * self.properties.WIDTH,
                            self.POS_X * self.properties.HEIGHT,
                            self.WIDTH * self.properties.WIDTH,
                            self.HEIGHT * self.properties.HEIGHT
                            )
        pygame.draw.rect(surface, self.COLOR, bookstand)



