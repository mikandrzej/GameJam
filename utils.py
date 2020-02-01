import color

class Utils:
    @staticmethod
    def textGenerator(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()