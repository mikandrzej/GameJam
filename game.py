import pygame
import random

import color
from properties import Properties
from state import State, ScreenState, GameState
from views.bookstand import Bookstand
from views.mainMenu import MainMenu


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
        self.mainMenu = MainMenu()
        self.bookstand = Bookstand(self.properties)

    def handleEvents(self):
        # 1 Process input/events
        for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
            ## listening for the the X button at the top
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state.handleScreenState()
                self.state.handleGameState(event)
            if event.type == pygame.QUIT:
                self.state.mainLoopRunning = False
            if event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                self.screen = pygame.display.set_mode((event.w, event.h),
                                                      pygame.RESIZABLE)

    def update(self):
        print(self.state.gameState)
        print(self.state.screenState)

    def draw(self):
        # 3 Draw/render
        self.screen.fill(color.WHITE)
        if self.state.screenState == ScreenState.RUNNING:
            if self.state.gameState == GameState.SHELF:
                self.bookstand.draw(self.screen)
            elif self.state.gameState == GameState.PUZZLE:
                self.screen.fill(color.BLUE)
        else:
            self.mainMenu.draw(self.screen)
        # all_sprites.draw(screen)
        ########################

    def run(self):
        ## Game loop
        self.state.mainLoopRunning = True
        while self.state.mainLoopRunning:
            self.properties.delta = self.clock.tick(self.properties.FPS)  ## will make the loop run at the same speed all the time
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
