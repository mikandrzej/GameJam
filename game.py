import pygame
import random

import color
from properties import Properties
from state import State
from views.bookstand import Bookstand


class Game:
    def __init__(self, properties: Properties):
        self.properties = properties
        self.state = State()
        ## initialize pygame and create window
        pygame.init()
        pygame.mixer.init()  ## For sound
        self.screen = pygame.display.set_mode((properties.WIDTH,
                                               properties.HEIGHT),
                                              pygame.RESIZABLE)
        pygame.display.set_caption(properties.GAME_TITLE)
        self.clock = pygame.time.Clock()  ## For syncing the FPS

        self.bookstand = Bookstand(self.properties)

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
        self.screen.fill(color.WHITE)
        self.bookstand.draw(self.screen)
        # all_sprites.draw(screen)
        ########################

    def run(self):
        ## Game loop
        self.state.running = True
        while self.state.running:
            self.clock.tick(self.properties.FPS)  ## will make the loop run at the same speed all the time
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
