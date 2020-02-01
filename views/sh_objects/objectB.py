import pygame
import color

class ObjectB:
    COLOR = color.RED

    def __init__(self,):
        pass

    def draw(self, surface: pygame.Surface):
        rect = pygame.Rect(0,
                           0,
                           surface.get_width(),
                           surface.get_height()
                            )
        pygame.draw.rect(surface, self.COLOR, rect)