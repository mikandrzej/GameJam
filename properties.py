class Properties:
    def __init__(self):
        self.WIDTH = 1366
        self.HEIGHT = 768
        self.FPS = 30
        self.GAME_TITLE = "<Your game>"
        self.WINDOW_TITLE = self.GAME_TITLE
        self.delta = 0.0
        self.menuOptionsFontSize = 50
        self.menuOptionsFont = 'freesansbold.ttf'
        self.menuTitleFont = self.menuOptionsFont
        self.menuTitleFontSize = 90
        self.labelControllerSelectionFont = self.menuOptionsFont
        self.labelControllerSelectionSize = 25
        self.labelPuzzleProgressFont = self.menuOptionsFont
        self.labelPuzzleProgressSize = 20
        self.labelTimerFont = self.menuOptionsFont
        self.labelTimerSize = 50

        self.QUEST_TYPES = ['RED', 'BLUE', 'GREEN', 'VIOLET']