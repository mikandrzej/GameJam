from controllers.controller import Controller as Ctrl
from controllers.controller import ControllerInput as CtrlInp

QUESTS_CAR = {
    "GAMEPAD" : {
        "RED" : [
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL
        ],
        "BLUE" : [
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
        ],
        "GREEN" : [
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
        ],
        "VIOLET" : [
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
            Ctrl.INP_UP,
            Ctrl.INP_RIGHT,
            Ctrl.INP_DOWN,
            Ctrl.INP_LEFT,
            Ctrl.INP_STICK_STILL,
        ]
    },
    "DRUMS" : {
        "RED" : [
            CtrlInp.PEDAL,
            CtrlInp.RED,
            CtrlInp.BLUE,
            CtrlInp.GREEN,
            CtrlInp.YELLOW
        ],
        "BLUE" : [
            CtrlInp.PEDAL,
            CtrlInp.RED,
            CtrlInp.BLUE,
            CtrlInp.GREEN,
            CtrlInp.YELLOW
        ],
        "GREEN" : [
            CtrlInp.PEDAL,
            CtrlInp.RED,
            CtrlInp.BLUE,
            CtrlInp.GREEN,
            CtrlInp.YELLOW
        ],
        "VIOLET" : [
            CtrlInp.PEDAL,
            CtrlInp.RED,
            CtrlInp.BLUE,
            CtrlInp.GREEN,
            CtrlInp.YELLOW
        ]
    },
    "GUITAR" : {
        "RED" : [
            CtrlInp.PEDAL,
            CtrlInp.RED,
            CtrlInp.BLUE,
            CtrlInp.GREEN,
            CtrlInp.YELLOW
        ],
        "BLUE" : [
        ],
        "GREEN" : [
        ],
        "VIOLET" : [
        ]
    }
}