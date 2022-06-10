#!/usr/bin/pyhon
#player.py

'''Holds player class definition'''

__author__ = "Dev Menon"
__version__ = "1.0"

import pygame


class Player:
    def __init__(self, x, y, to_kill, to_kill_img,
                 idle_right, run_right, jump_right, attack_right, hurt_right, die_right,
                 idle_left, run_left, jump_left, attack_left, hurt_left, die_left,
                 idle_cols, run_cols, jump_cols, attack_cols, hurt_cols, die_cols):
        '''constructs a player
        :param x: the x coord of player
        :param y: the y coord of player
        :param to_kill: how many hyenas player has left kill
        :param to_kill_img: the img for to kill UI
        :param idle_right: the spritesheet for idle right
        :param run_right: the spritesheet for run right
        :param jump_right: the spritesheet for jump right
        :params attack_right: the spritesheet for attack right
        :param hurt_right: the spritesheet for hurt right
        :param die_right: the spritesheet for die right
        :param idle_left: the spritesheet for idle left
        :param run_left: the spritesheet for run left
        :param jump_left: the spritesheet for jump left
        :param attack_left: the spritesheet for attack left
        :param hurt_left: the spritesheet for hurt left
        :param die_left: the spritesheet for die left
        :param idle_cols: num of cols in idle spritesheet
        :param run_cols: num of cols in run spritesheet
        :param jump_cols: num of cols in jump spritesheet
        :param attack_cols: num of cols in attack spritesheet
        :param hurt_cols: num of cols in hurt spritesheet
        :param die_cols: num of cols in die spritesheet'''

        self.x = x
        self.y = y

        self.to_kill = to_kill
        self.to_kill_img = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(to_kill_img)))

        self.damage = 40

        self.health = 100
        self.max_health = 100
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length

        self.action = "idle"
        self.direction = "right"

        self.dam_taken_from = ""

        self.idle_right = pygame.transform.scale2x(pygame.image.load(idle_right))
        self.run_right = pygame.transform.scale2x(pygame.image.load(run_right))
        self.jump_right = pygame.transform.scale2x(pygame.image.load(jump_right))
        self.attack_right = pygame.transform.scale2x(pygame.image.load(attack_right))
        self.hurt_right = pygame.transform.scale2x(pygame.image.load(hurt_right))
        self.die_right = pygame.transform.scale2x(pygame.image.load(die_right))

        self.idle_left = pygame.transform.scale2x(pygame.image.load(idle_left))
        self.run_left = pygame.transform.scale2x(pygame.image.load(run_left))
        self.jump_left = pygame.transform.scale2x(pygame.image.load(jump_left))
        self.attack_left = pygame.transform.scale2x(pygame.image.load(attack_left))
        self.hurt_left = pygame.transform.scale2x(pygame.image.load(hurt_left))
        self.die_left = pygame.transform.scale2x(pygame.image.load(die_left))

        self.idle_cols = idle_cols
        self.run_cols = run_cols
        self.jump_cols = jump_cols
        self.attack_cols = attack_cols
        self.hurt_cols = hurt_cols
        self.die_cols = die_cols

        self.idle_rect = self.idle_right.get_rect()
        self.run_rect = self.run_right.get_rect()
        self.jump_rect = self.jump_right.get_rect()
        self.attack_rect = self.attack_right.get_rect()
        self.hurt_rect = self.hurt_right.get_rect()
        self.die_rect = self.die_right.get_rect()

        idle_w = self.idle_cell_width = self.idle_rect.width / idle_cols
        idle_h = self.idle_cell_height = self.idle_rect.height

        run_w = self.run_cell_width = self.run_rect.width / run_cols
        run_h = self.run_cell_height = self.run_rect.height

        jump_w = self.jump_cell_width = self.jump_rect.width / jump_cols
        jump_h = self.jump_cell_height = self.jump_rect.height

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

        self.jump_cells = []
        for i in range(jump_cols):
            self.jump_cells.append((i * jump_w, 0, jump_w, jump_h))

        self.attack_cells = []
        for i in range(attack_cols):
            self.attack_cells.append((i * attack_w, 0, attack_w, attack_h))

        self.hurt_cells = []
        for i in range(hurt_cols):
            self.hurt_cells.append((i * hurt_w, 0, hurt_w, hurt_h))

        self.die_cells = []
        for i in range(die_cols):
            self.die_cells.append((i * die_w, 0, die_w, die_h))

        self.idle_index = 0
        self.run_index = 0
        self.jump_index = 0
        self.attack_index = 0
        self.hurt_index = 0
        self.die_right_index = 0
        self.die_left_index = die_cols - 1

    def draw_self(self, surface):
        '''draws player depending on action
        :param surface: the surface to draw the player on'''

        if self.direction == "right":
            if self.action == "idle" or self.action == "heal":
                surface.blit(self.idle_right, (self.x, self.y), self.idle_cells[self.idle_index])
            elif self.action == "run":
                surface.blit(self.run_right, (self.x, self.y), self.run_cells[self.run_index])
            elif self.action == "jump":
                surface.blit(self.jump_right, (self.x, self.y), self.jump_cells[self.jump_index])
            elif self.action == "attack":
                surface.blit(self.attack_right, (self.x, self.y), self.attack_cells[self.attack_index])
            elif self.action == "hurt":
                surface.blit(self.hurt_right, (self.x, self.y), self.hurt_cells[self.hurt_index])
            elif self.action == "die":
                surface.blit(self.die_right, (self.x, self.y), self.die_cells[self.die_right_index])

        elif self.direction == "left":
            if self.action == "idle" or self.action == "heal":
                surface.blit(self.idle_left, (self.x, self.y), self.idle_cells[self.idle_index])
            elif self.action == "run":
                surface.blit(self.run_left, (self.x, self.y), self.run_cells[self.run_index])
            elif self.action == "jump":
                surface.blit(self.jump_left, (self.x, self.y), self.jump_cells[self.jump_index])
            elif self.action == "attack":
                surface.blit(self.attack_left, (self.x, self.y), self.attack_cells[self.attack_index])
            elif self.action == "hurt":
                surface.blit(self.hurt_left, (self.x, self.y), self.hurt_cells[self.hurt_index])
            elif self.action == "die":
                surface.blit(self.die_left, (self.x, self.y), self.die_cells[self.die_left_index])

    def update_health_bar(self, surface):
        '''updates health bar of player
        :param surface: the surface to draw the health bar on'''

        if self.health > 70:
            pygame.draw.rect(surface, (106, 221, 131), (30, 30, self.health / self.health_ratio, 40))
        elif self.health > 30:
            pygame.draw.rect(surface, (239, 246, 113), (30, 30, self.health / self.health_ratio, 40))
        else:
            pygame.draw.rect(surface, (242, 103, 103), (30, 30, self.health / self.health_ratio, 40))

        pygame.draw.rect(surface, (255, 255, 255), (30, 30, self.health_bar_length, 40), 6)

    def update_to_kill(self, surface, font_size):
        '''updates the to kill of the player
        :param surface: the surface to draw the to kill on
        :param font_size: font size of to kill UI text'''

        font = pygame.font.Font("Assets/UI/Fonts/OriginTech.ttf", font_size)
        surface.blit(self.to_kill_img, (1100, 30))
        text = font.render(": " + str(self.to_kill), True, (255, 255, 255))
        surface.blit(text, (1175, 30))

    def heal(self, amount):
        '''heals player
        :param amount: amount of health to give player'''

        if self.health != self.max_health:
            self.health += amount

    def take_damage(self, amount):
        '''applies damage to player
        :param amount: amount of health to take away from player'''

        if self.health > 0:
            self.health -= amount
        elif self.health <= 0:
            self.health = 0

