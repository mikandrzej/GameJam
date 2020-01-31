import pygame

import color
from properties import Properties

class Bookstand:
    POS_X = 0.2
    POS_Y = 0.2
    WIDTH = 0.6
    HEIGHT = 0.6
    BOARD_WIDTH = 0.01
    SHELFS = 3
    OBJECTS_ON_SHELF = 5

    def __init__(self, properties: Properties):
        self.properties = properties

        objects = []
        for x in range(self.OBJECTS_ON_SHELF):
            pass
        self._objects = objects


    def draw(self, surface: pygame.Surface):
        self._drawShelf(surface)

    def _drawShelf(self, surface: pygame.Surface):
        bookstand = pygame.Rect(self.POS_X * self.properties.WIDTH,
                            self.POS_Y * self.properties.HEIGHT,
                            self.WIDTH * self.properties.WIDTH,
                            self.HEIGHT * self.properties.HEIGHT
                            )

        shelfs = []
        for x in range(self.SHELFS):
            shelf = pygame.Rect((self.POS_X + self.BOARD_WIDTH) * self.properties.WIDTH,
                                ((self.POS_Y + (x * (self.HEIGHT/3))) + self.BOARD_WIDTH) * self.properties.HEIGHT,
                                (self.WIDTH - (2*self.BOARD_WIDTH)) * self.properties.WIDTH,
                                ((self.HEIGHT / self.SHELFS) - (2*self.BOARD_WIDTH)) * self.properties.HEIGHT
                                )
            shelfs.append(shelf)

        pygame.draw.rect(surface, color.COL_BOOKSTAND, bookstand)
        for shelf in shelfs:
            pygame.draw.rect(surface, color.COL_SHELF, shelf)



