#!/usr/bin/env python2

import pygame
import random

from game import Game
from properties import Properties

if __name__ == '__main__':
    properties = Properties()
    game = Game(properties)
    game.run()
    pygame.quit()