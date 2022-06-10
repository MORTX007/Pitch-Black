#!/usr/bin/pyhon
#spell.py

'''Holds spell class definition'''

__author__ = "Dev Menon"
__version__ = "1.0"

import pygame

class Spell:
    def __init__(self, x, y, producer):
        '''constructs a spell
        :param x: the x coord of spell
        :param y: the y coord of spell
        :param producer: the producer of the spell'''

        self.x = x
        self.y = y

        self.producer = producer

        self.damage = 20

        self.spell = pygame.transform.scale2x(pygame.image.load("Assets/Spell/Spell.png"))

        self.cols = 8

        self.spell_rect = self.spell.get_rect()

        spell_w = self.spell_cell_width = self.spell_rect.width / self.cols
        spell_h = self.spell_cell_height = self.spell_rect.height

        self.spell_cells = []
        for i in range(self.cols):
            self.spell_cells.append((i * spell_w, 0, spell_w, spell_h))

        self.spell_index = 0

    def draw_self(self, surface):
        '''draws spell
        :param surface: the surface to draw the spell on'''

        surface.blit(self.spell, (self.x, self.y), self.spell_cells[self.spell_index])