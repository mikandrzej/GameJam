import pygame
import random

from color import BLUE, BLACK
from properties import FPS, GAME_TITLE
from state import State


class Game:
    def __init__(self, width: int, height: int):
        self.state = State()
        ## initialize pygame and create window
        pygame.init()
        pygame.mixer.init()  ## For sound
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()  ## For syncing the FPS

    def handleEvents(self):
        # 1 Process input/events
        for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
            ## listening for the the X button at the top
            if event.type == pygame.QUIT:
                self.state.running = False
            if event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                self.screen = pygame.display.set_mode((event.w, event.h),
                                                      pygame.RESIZABLE)

    def update(self):
        pass

    def draw(self):
        # 3 Draw/render
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, BLUE, (200, 150, 100, 50))
        # all_sprites.draw(screen)
        ########################

    def run(self):
        ## Game loop
        self.state.running = True
        while self.state.running:
            self.clock.tick(FPS)  ## will make the loop run at the same speed all the time
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
