#!/usr/bin/pyhon
#power_up.py

'''Holds power up class definition'''

__author__ = "Dev Menon"
__version__ = "1.0"

import pygame

class Powerup:
    def __init__(self, x, y, type):
        '''constructs a powerup
        :param x: the x coord of powerup
        :param y: the y coord of powerup
        :param type: type of powerup'''

        self.x = x
        self.y = y
        self.type = type

        self.elapsed = 0

        if self.type == "health":
            self.image = pygame.image.load("Assets/UI/medkit.png")
            self.img_rect = self.image.get_rect()

    def draw_self(self, surface):
        '''draws powerup
        :param surface: the surface to draw the powerup on'''

        surface.blit(self.image, (self.x, self.y))
        self.elapsed += 1

    def take_effect(self, player):
        '''takes effect of power on player
        :param player: the player it is taking effect on'''

        if self.type == "health":
            player.action = "heal"
