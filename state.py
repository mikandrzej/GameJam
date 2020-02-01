from enum import Enum


class ScreenState(Enum):
    RUNNING = 0
    MAIN_MENU = 1


class GameState(Enum):
    NONE = 0
    SHELF = 1
    PUZZLE = 2


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

    def handleGameState(self, event):
        possibleState = event.key % 48
        if possibleState in range(1, 3):
            self.gameState = possibleState
