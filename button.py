#!/usr/bin/pyhon
#button.py

'''Holds button class definition'''

__author__ = "Dev Menon"
__version__ = "1.0"

import pygame


class Button:
    def __init__(self, color, x, y, width, height, font_size, text=''):
        '''constructs a button
        :param color: color of text in button
        :param x: the x coord of button
        :param y: the y coord of button
        :param width: width of button
        :param height: height of button
        :param font_size: font_size of text in button
        :param text: text in button'''

        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.text = text

    def draw(self, surface):
        '''draws button
        :param surface: the surface to draw the button on'''

        if self.text != '':
            font = pygame.font.Font("Assets/UI/Fonts/OriginTech.ttf", self.font_size)
            text = font.render(self.text, True, self.color)
            # CENTER BUTTON ANCHOR
            surface.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        '''checks if cursor is over the button
        :param pos: the position of the cursor
        :return: True if cursor is over the button or else False'''

        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
