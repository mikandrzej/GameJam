import pygame
import random

import color
from controller import Controller
from properties import Properties
from state import State, ScreenState, GameState
from views.bookstand import Bookstand
from views.controllerSelection import ControllerSelection
from views.mainMenu import MainMenu


class Game:
    def __init__(self, properties: Properties):
        self.properties = properties
        self.state = State()
        ## initialize pygame and create window
        pygame.init()
        # pygame.mixer.init()  ## For sound
        pygame.joystick.init()
        self.screen = pygame.display.set_mode((properties.WIDTH,
                                               properties.HEIGHT),
                                              pygame.RESIZABLE)
        pygame.display.set_caption(properties.GAME_TITLE)
        self.clock = pygame.time.Clock()  ## For syncing the FPS
        self.mainMenu = MainMenu(self.properties, self.state)
        self.bookstand = Bookstand(self.properties)
        self.controller = Controller()
        self.controllerSelection = ControllerSelection(self.properties, self.state)

    def handleEvents(self):
        # 1 Process input/events
        events = pygame.event.get()
        self.controller.handleEvents(events)
        for event in events:  # gets all the events which have occured till now and keeps tab of them.
            if event.type == pygame.KEYDOWN:
                self.state.handleGameState(event)
            if event.type == pygame.QUIT:
                self.state.mainLoopRunning = False
            if event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                self.properties.HEIGHT = event.h
                self.properties.WIDTH = event.w
                self.screen = pygame.display.set_mode((self.properties.WIDTH,
                                                       self.properties.HEIGHT),
                                                       pygame.RESIZABLE)
                self.bookstand.recalculatePositions()
                self.controllerSelection.recalculatePositions()

    def update(self):
        if self.controller.getKeyboardButtons()[Controller.INP_PAUSE]:
            self.state.handleScreenState()
        if self.state.screenState == ScreenState.MAIN_MENU:
            self.mainMenu.update(self.controller)
        else:
            if self.state.gameState == GameState.CONTROLLER_SELECTION:
                self.controllerSelection.update(self.controller)
            else:
                self.bookstand.update(self.controller)

    def draw(self):
        # 3 Draw/render
        self.screen.fill(color.WHITE)
        if self.state.screenState == ScreenState.RUNNING:
            if self.state.gameState == GameState.CONTROLLER_SELECTION:
                self.controllerSelection.draw(self.screen)
            elif self.state.gameState == GameState.SHELF:
                self.bookstand.draw(self.screen)
            elif self.state.gameState == GameState.PUZZLE:
                self.screen.fill(color.BLUE)
        else:
            self.mainMenu.draw(self.screen)

    def run(self):
        while self.state.mainLoopRunning:
            self.properties.delta = self.clock.tick(self.properties.FPS)  ## will make the loop run at the same speed all the time
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
