import pygame


class Controller:


    INP_PAUSE = 0
    INP_UP = 1
    INP_RIGHT = 2
    INP_DOWN = 4
    INP_LEFT = 8
    INP_ACCEPT = 16

    GAMEPAD_MAP = {
        0: INP_ACCEPT,
        6: INP_PAUSE,
    }
    GAMEPAD_HAT_MAP = {
        (0, 1): INP_UP,
        (1, 0): INP_RIGHT,
        (0, -1): INP_DOWN,
        (-1, 0): INP_LEFT,
    }
    def __init__(self):
        self.KEYBOARD = 0
        self.GAMEPAD = 0
        self.DRUMS = 0
        self.GUITAR = 0
        self.emptyButtons = {
            self.INP_PAUSE: False,
            self.INP_UP: False,
            self.INP_RIGHT: False,
            self.INP_DOWN: False,
            self.INP_LEFT: False,
            self.INP_ACCEPT: False
        }
        self.buttons = self.emptyButtons.copy()
        self.joystickButtons = [self.emptyButtons.copy(), self.emptyButtons.copy(), self.emptyButtons.copy()]
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        self.activeJoysticks = [False, False, False]
        for joy in self.joysticks:
            joy.init()

    def handleEvents(self, events):
        self.buttons = self.emptyButtons.copy()
        self.activeJoysticks = [False, False, False]
        for event in events:  # gets all the events which have occured till now and keeps tab of them.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.buttons[self.INP_PAUSE] = True
                elif event.key == pygame.K_UP:
                    self.buttons[self.INP_UP] = True
                elif event.key == pygame.K_RIGHT:
                    self.buttons[self.INP_RIGHT] = True
                elif event.key == pygame.K_DOWN:
                    self.buttons[self.INP_DOWN] = True
                elif event.key == pygame.K_LEFT:
                    self.buttons[self.INP_LEFT] = True
                elif event.key == pygame.K_RETURN:
                    self.buttons[self.INP_ACCEPT] = True
            if event.type == pygame.JOYBUTTONDOWN:
                self._handleJoystickButton(event)
            if event.type == pygame.JOYHATMOTION:
                self._handleJoystickHat(event)

    def _handleJoystickHat(self, event):
        joy = pygame.joystick.Joystick(event.joy)
        hats = joy.get_numhats()
        for i in range(hats):
            hat = joy.get_hat(i)
            if hat in self.GAMEPAD_HAT_MAP.keys():
                self.buttons[self.GAMEPAD_HAT_MAP[hat]] = True

    def _handleJoystickButton(self, event):
        self.activeJoysticks[event.joy] = True
        if event.button in self.GAMEPAD_MAP.keys(): # if button mapper contains map for given key
            self.buttons[self.GAMEPAD_MAP[event.button]] = True

    def getKeyboardButtons(self):
        return self.buttons

    def getJoystickButtons(self):
        return self.joystickButtons

    def getActivatedJoysticks(self):
        return self.activeJoysticks

    def setController(self, whichController):
        #  ["GamePad", "Drum", "Guitar"]
        if whichController[0] == "GamePad":
            self.GAMEPAD = whichController
        elif whichController[0] == "Drums":
            self.DRUMS = whichController
        elif whichController[0] == "Guitar":
            self.GUITAR = whichController
