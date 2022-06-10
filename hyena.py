#!/usr/bin/pyhon
#hyena.py

'''Holds hyena class definition'''

__author__ = "Dev Menon"
__version__ = "1.0"

import pygame


class Hyena:
    def __init__(self, x, y, direction, idle_right, run_right, attack_right, hurt_right, die_right,
                 idle_left, run_left, attack_left, hurt_left, die_left,
                 idle_cols, run_cols, attack_cols, hurt_cols, die_cols):
        '''constructs a hyena
        :param x: the x coord of hyena
        :param y: the y coord of hyena
        :param idle_right: the spritesheet for idle right
        :param run_right: the spritesheet for run right
        :param attack_right: the spritesheet for attack right
        :param hurt_right: the spritesheet for hurt right
        :param die_right: the spritesheet for die right
        :param idle_left: the spritesheet for idle left
        :param run_left: the spritesheet for run left
        :param attack_left: the spritesheet for attack left
        :param hurt_left: the spritesheet for hurt left
        :param die_left: the spritesheet for die left
        :param idle_cols: num of cols in idle spritesheet
        :param run_cols: num of cols in run spritesheet
        :param attack_cols: num of cols in attack spritesheet
        :param hurt_cols: num of cols in hurt spritesheet
        :param die_cols: num of cols in die spritesheet'''

        self.x = x
        self.y = y

        self.health = 100
        self.max_health = 100
        self.health_bar_length = 50
        self.health_ratio = self.max_health / self.health_bar_length

        self.action = "run"
        self.direction = direction

        self.idle_right = pygame.transform.scale2x(pygame.image.load(idle_right))
        self.run_right = pygame.transform.scale2x(pygame.image.load(run_right))
        self.attack_right = pygame.transform.scale2x(pygame.image.load(attack_right))
        self.hurt_right = pygame.transform.scale2x(pygame.image.load(hurt_right))
        self.die_right = pygame.transform.scale2x(pygame.image.load(die_right))

        self.idle_left = pygame.transform.scale2x(pygame.image.load(idle_left))
        self.run_left = pygame.transform.scale2x(pygame.image.load(run_left))
        self.attack_left = pygame.transform.scale2x(pygame.image.load(attack_left))
        self.hurt_left = pygame.transform.scale2x(pygame.image.load(hurt_left))
        self.die_left = pygame.transform.scale2x(pygame.image.load(die_left))


        self.idle_cols = idle_cols
        self.run_cols = run_cols
        self.attack_cols = attack_cols
        self.hurt_cols = hurt_cols
        self.die_cols = die_cols

        self.idle_rect = self.idle_right.get_rect()
        self.run_rect = self.run_right.get_rect()
        self.attack_rect = self.attack_right.get_rect()
        self.hurt_rect = self.hurt_right.get_rect()
        self.die_rect = self.die_right.get_rect()


        idle_w = self.idle_cell_width = self.idle_rect.width / idle_cols
        idle_h = self.idle_cell_height = self.idle_rect.height

        run_w = self.run_cell_width = self.run_rect.width / run_cols
        run_h = self.run_cell_height = self.run_rect.height

        attack_w = self.attack_cell_width = self.attack_rect.width / attack_cols
        attack_h = self.attack_cell_height = self.attack_rect.height

        hurt_w = self.hurt_cell_width = self.hurt_rect.width / hurt_cols
        hurt_h = self.hurt_cell_height = self.hurt_rect.height

        die_w = self.die_cell_width = self.die_rect.width / die_cols
        die_h = self.die_cell_height = self.die_rect.height

        self.idle_cells = []
        for i in range(idle_cols):
            self.idle_cells.append((i * idle_w, 0, idle_w, idle_h))

        self.run_cells = []
        for i in range(run_cols):
            self.run_cells.append((i * run_w, 0, run_w, run_h))

        self.attack_cells = []
        for i in range(attack_cols):
            self.attack_cells.append((i * attack_w, 0, attack_w, attack_h))

        self.hurt_cells = []
        for i in range(hurt_cols):
            self.hurt_cells.append((i * hurt_w, 0, hurt_w, hurt_h))

        self.die_cells = []
        for i in range(die_cols):
            self.die_cells.append((i * die_w, 0, die_w, die_h))

        self.idle_right_index = self.idle_cols - 1
        self.idle_left_index = 0

        self.run_right_index = self.run_cols - 1
        self.run_left_index = 0

        self.attack_right_index = self.attack_cols - 1
        self.attack_left_index = 0

        self.hurt_right_index = self.hurt_cols - 1
        self.hurt_left_index = 0

        self.die_right_index = self.die_cols - 1
        self.die_left_index = 0

        self.hurt_elapsed = 0
        self.die_elapsed = 0

    def draw_self(self, surface):
        '''draws hyena depending on action
        :param surface: the surface to draw the hyena on'''

        if self.direction == "right":
            if self.action == "idle":
                surface.blit(self.idle_right, (self.x, self.y), self.idle_cells[self.idle_right_index])
            elif self.action == "run":
                surface.blit(self.run_right, (self.x, self.y), self.run_cells[self.run_right_index])
            elif self.action == "attack":
                surface.blit(self.attack_right, (self.x, self.y), self.attack_cells[self.attack_right_index])
            elif self.action == "hurt":
                surface.blit(self.hurt_right, (self.x, self.y), self.hurt_cells[self.hurt_right_index])
            elif self.action == "die":
                surface.blit(self.die_right, (self.x, self.y), self.die_cells[self.die_right_index])

        elif self.direction == "left":
            if self.action == "idle":
                surface.blit(self.idle_left, (self.x, self.y), self.idle_cells[self.idle_left_index])
            elif self.action == "run":
                surface.blit(self.run_left, (self.x, self.y), self.run_cells[self.run_left_index])
            elif self.action == "attack":
                surface.blit(self.attack_left, (self.x, self.y), self.attack_cells[self.attack_left_index])
            elif self.action == "hurt":
                surface.blit(self.hurt_left, (self.x, self.y), self.hurt_cells[self.hurt_left_index])
            elif self.action == "die":
                surface.blit(self.die_left, (self.x, self.y), self.die_cells[self.die_left_index])

    def update_health_bar(self, surface):
        '''updates health bar of hyena
        :param surface: the surface to draw the health bar on'''

        if self.direction == "right":
            x = self.x + 20
        elif self.direction == "left":
            x = self.x + 20
        y = self.y

        if self.health > 70:
            pygame.draw.rect(surface, (106, 221, 131), (x, y, self.health / self.health_ratio, 10))
        elif self.health > 30:
            pygame.draw.rect(surface, (239, 246, 113), (x, y, self.health / self.health_ratio, 10))
        else:
            pygame.draw.rect(surface, (242, 103, 103), (x, y, self.health / self.health_ratio, 10))

        pygame.draw.rect(surface, (0, 0, 0), (x, y, self.health_bar_length, 10), 2)

    def take_damage(self, amount):
        '''applies damage to hyena
        :param amount: amount of health to take away from hyena'''

        if self.health > 0:
            self.health -= amount
        elif self.health <= 0:
            self.health = 0
