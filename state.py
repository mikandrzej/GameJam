from enum import Enum


class ScreenState(Enum):
    RUNNING = 0
    MAIN_MENU = 1


class GameState(Enum):
    NONE = 0
    CONTROLLER_SELECTION = 1
    SHELF = 2
    PUZZLE = 3


class State:
    def __init__(self):
        self.mainLoopRunning = True
        self.screenState = ScreenState.MAIN_MENU
        self.gameState = GameState.NONE

    def handleScreenState(self):
        if self.screenState == ScreenState.MAIN_MENU:
            self.screenState = ScreenState.RUNNING
        elif self.screenState == ScreenState.RUNNING:
            self.screenState = ScreenState.MAIN_MENU

