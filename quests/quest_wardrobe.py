from controllers.controller import Controller as Ctrl
from controllers.controller import ControllerInput as CtrlInp

QUESTS_WARDROBE = {
    "GAMEPAD" : {
        "RED" : [
            Ctrl.INP_RIGHT,
            Ctrl.INP_UP,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_DOWN,
            Ctrl.INP_RIGHT,
            Ctrl.INP_UP,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
        ],
        "BLUE" : [
Ctrl.INP_LEFT,
Ctrl.INP_STICK_STILL,
Ctrl.INP_UP,
Ctrl.INP_RIGHT,
Ctrl.INP_STICK_STILL,
Ctrl.INP_RIGHT,
Ctrl.INP_UP,
Ctrl.INP_LEFT,
Ctrl.INP_STICK_STILL,
Ctrl.INP_DOWN

        ],
        "GREEN" : [
Ctrl.INP_LEFT,
Ctrl.INP_STICK_STILL,
Ctrl.INP_UP,
Ctrl.INP_RIGHT,
Ctrl.INP_STICK_STILL,
Ctrl.INP_RIGHT,
Ctrl.INP_STICK_STILL,
Ctrl.INP_LEFT,
Ctrl.INP_DOWN,
Ctrl.INP_RIGHT,

        ],
        "VIOLET" : [
Ctrl.INP_STICK_STILL,
Ctrl.INP_RIGHT,
Ctrl.INP_STICK_STILL,
Ctrl.INP_DOWN,
Ctrl.INP_STICK_STILL,
Ctrl.INP_LEFT,
Ctrl.INP_STICK_STILL,
Ctrl.INP_UP,
Ctrl.INP_RIGHT,
Ctrl.INP_UP,

        ]
    },
    "DRUMS" : {
        "RED" : [
            CtrlInp.YELLOW,
            CtrlInp.PEDAL,
            CtrlInp.YELLOW,
            CtrlInp.YELLOW,
            CtrlInp.YELLOW,
            CtrlInp.ORANGE,
            CtrlInp.GREEN,
            CtrlInp.ORANGE,
            CtrlInp.PEDAL,
            CtrlInp.YELLOW
        ],
        "BLUE" : [
            CtrlInp.PEDAL,
            CtrlInp.RED,
            CtrlInp.RED,
            CtrlInp.BLUE,
            CtrlInp.PEDAL,
            CtrlInp.YELLOW,
            CtrlInp.GREEN,
            CtrlInp.PEDAL,
            CtrlInp.RED,
            CtrlInp.BLUE
        ],
        "GREEN" : [
            CtrlInp.ORANGE,
            CtrlInp.ORANGE,
            CtrlInp.PEDAL,
            CtrlInp.GREEN,
            CtrlInp.YELLOW,
            CtrlInp.GREEN,
            CtrlInp.GREEN,
            CtrlInp.BLUE,
            CtrlInp.PEDAL,
            CtrlInp.PEDAL,
        ],
        "VIOLET" : [
            CtrlInp.YELLOW,
            CtrlInp.ORANGE,
            CtrlInp.BLUE,
            CtrlInp.ORANGE,
            CtrlInp.RED,
            CtrlInp.RED,
            CtrlInp.BLUE,
            CtrlInp.RED,
            CtrlInp.YELLOW,
            CtrlInp.YELLOW,
        ]
    },
    "GUITAR" : {
        "RED" : [
            CtrlInp.RED,
            CtrlInp.YELLOW,
            CtrlInp.BLUE,
            CtrlInp.BLUE,
            CtrlInp.RED,
            CtrlInp.RED,
            CtrlInp.BLUE,
            CtrlInp.GREEN,
            CtrlInp.BLUE,
            CtrlInp.YELLOW,

        ],
        "BLUE" : [
            CtrlInp.BLUE,
            CtrlInp.BLUE,
            CtrlInp.BLUE,
            CtrlInp.BLUE,
            CtrlInp.GREEN,
            CtrlInp.YELLOW,
            CtrlInp.BLUE,
            CtrlInp.BLUE,
            CtrlInp.GREEN,
            CtrlInp.YELLOW,
        ],
        "GREEN" : [
            CtrlInp.BLUE,
            CtrlInp.BLUE,
            CtrlInp.RED,
            CtrlInp.BLUE,
            CtrlInp.RED,
            CtrlInp.RED,
            CtrlInp.YELLOW,
            CtrlInp.GREEN,
            CtrlInp.GREEN,
            CtrlInp.GREEN,

        ],
        "VIOLET" : [
            CtrlInp.RED,
            CtrlInp.YELLOW,
            CtrlInp.GREEN,
            CtrlInp.RED,
            CtrlInp.RED,
            CtrlInp.YELLOW,
            CtrlInp.BLUE,
            CtrlInp.YELLOW,
            CtrlInp.RED,
            CtrlInp.YELLOW,
        ]
    }
}