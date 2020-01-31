#!/usr/bin/env python2

import pygame
import random

from game import Game
from properties import WIDTH, HEIGHT

if __name__ == '__main__':
    game = Game(width=WIDTH, height=HEIGHT)
    game.run()
    pygame.quit()