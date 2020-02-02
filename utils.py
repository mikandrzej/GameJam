import color

class Utils:
    @staticmethod
    def textGenerator(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

class GameTimer:
    timer = 0.0
    minutes = 0
    seconds = 0
    timerStr = ''

    def __init__(self):
        pass

    def addTime(self, val: float):
        self.timer += val
        _seconds = int(self.timer / 1000.0)
        self.minutes = _seconds // 60
        self.seconds = _seconds % 60
        self._createString()

    def _createString(self):
        timStr = ''
        if self.minutes < 10:
            timStr += '0'
        timStr += str(self.minutes)
        timStr += ":"
        if self.seconds < 10:
            timStr += '0'
        timStr += str(self.seconds)
        self.timerStr = timStr