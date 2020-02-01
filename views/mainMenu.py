import this

import pygame

import color
from controller import Controller
from properties import Properties
from state import State, GameState, ScreenState
from utils import Utils


class MainMenu:
    VMARGIN_OPTIONS = 0.4
    VMARGIN_TITLE = 0.1

    def __init__(self, properties: Properties, state: State):
        self.state = state
        self.mainMenu = [("Start Game", self.startNewGame), ("Exit", self.exitGame)]
        self.pauseOptions = [("Start New Game", self.startNewGame), ("Resume game", self.resumeGame), ("Exit", self.exitGame)]
        self.options = self.mainMenu
        self.activeOption = 0
        self.properties = properties
        self.titleFont = pygame.font.Font(self.properties.menuTitleFont, self.properties.menuTitleFontSize)
        self.menuFont = pygame.font.Font(self.properties.menuOptionsFont, self.properties.menuOptionsFontSize)
        self.titleY = self.VMARGIN_TITLE * self.properties.HEIGHT
        self.optionsStartY = self.VMARGIN_OPTIONS * self.properties.HEIGHT

    def update(self, controller: Controller):
        if controller.getButtons()[Controller.INP_UP]:
            self.activeOption -= 1
        if controller.getButtons()[Controller.INP_DOWN]:
            self.activeOption += 1
        self.activeOption %= len(self.options)
        if controller.getButtons()[Controller.INP_ACCEPT]:
            self.options[self.activeOption][1]()

    def draw(self, surface: pygame.Surface):
        # draw title
        TextSurf, TextRect = Utils.textGenerator(self.properties.GAME_TITLE, self.titleFont, color.RED)
        TextRect.midtop = ((self.properties.WIDTH / 2), self.titleY)
        surface.blit(TextSurf, TextRect)
        # draw options
        y = self.optionsStartY
        i = 0
        for optionTitle, method in self.options:
            TextSurf, TextRect = Utils.textGenerator(optionTitle, self.menuFont, color.BLUE if i == self.activeOption else color.BLACK)
            TextRect.midtop = ((self.properties.WIDTH / 2), y)
            surface.blit(TextSurf, TextRect)
            i += 1
            y += 100

    def startNewGame(self):
        # if self.state.gameState != GameState.NONE:
        self.options = self.pauseOptions
        self.state.screenState = ScreenState.RUNNING
        self.state.gameState = GameState.SHELF

    def resumeGame(self):
        self.state.screenState = ScreenState.RUNNING

    def exitGame(self):
        self.state.mainLoopRunning = False
