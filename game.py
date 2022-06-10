#!/usr/bin/python
#game.py

'''runs the Pitch Black game'''

__author__ = "Dev Menon"
__version__ = "1.0"

import pygame
import player
import hyena
import spell
import power_up as pu
import button
import random


###############
# MENU
###############
def draw_menu_window():
    '''draws the menu window'''

    win.blit(woods, ((pos[0] / 100) - 20, (pos[1] / 100) - 20))
  
    win.blit(title, (400, 200))

    start.draw(win)

    # Make sure brawl button start a game of the last game mode selected
    # If last game mode was never selected it defaults to easy game mode
    try:
        if last_gamemode == "easy":
            button_manager(start, 80, easy_init)
        if last_gamemode == "medium":
            button_manager(start, 80, medium_init)
        if last_gamemode == "hard":
            button_manager(start, 80, hard_init)
    except NameError:
        button_manager(start, 80, easy_init)

    levels.draw(win)
    button_manager(levels, 80, levels_screen)

    ins.draw(win)
    button_manager(ins, 80, instructions_screen)

    quit.draw(win)
    button_manager(quit, 80, quit_game)

    pygame.display.update()


def menu():
    '''runs the menu for the game'''

    global win, width, height
    global fps, woods, font, run
    global title, start, levels, ins, quit
    global pos, event_type

    # SETUP
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Menu")
    dis_info = pygame.display.Info()
    width = dis_info.current_w
    height = dis_info.current_h

    pygame.font.init()

    fps = 50

    woods = pygame.transform.scale(pygame.image.load('Assets/UI/dark_woods.png'), (width + 80, height + 80)).convert()

    # MAIN MENU
    clock = pygame.time.Clock()

    font = pygame.font.Font("Assets/UI/Fonts/OriginTech.ttf", 100)

    title = font.render("PITCH BLACK", True, (255, 255, 255))

    start = button.Button((255, 255, 255), 300, 500, 300, 100, 80, text="BRAWL")
    levels = button.Button((255, 255, 255), 800, 500, 350, 100, 80, text="LEVELS")
    ins = button.Button((255, 255, 255), 280, 700, 350, 100, 80, text="HOW TO")
    quit = button.Button((255, 255, 255), 880, 700, 200, 100, 80, text="QUIT")

    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            event_type = event.type

            if event.type == pygame.QUIT:
                run = False

        draw_menu_window()

    pygame.quit()


###############
# LEVELS
###############
def draw_levels_window():
    '''draws the levels window'''

    win.blit(woods, ((pos[0] / 100) - 20, (pos[1] / 100) - 20))

    win.blit(levels_text, (550, 50))

    easy.draw(win)
    button_manager(easy, 80, easy_init)

    medium.draw(win)
    button_manager(medium, 80, medium_init)

    hard.draw(win)
    button_manager(hard, 80, hard_init)

    exit.draw(win)
    button_manager(exit, 64, menu)

    pygame.display.update()


def levels_screen():
    '''runs the levels screen'''

    global win, width, height
    global fps, woods, font, run
    global levels_text, easy, medium, hard, exit
    global pos, event_type

    # SETUP
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Levels")
    dis_info = pygame.display.Info()
    width = dis_info.current_w
    height = dis_info.current_h

    pygame.font.init()

    fps = 50

    woods = pygame.transform.scale(pygame.image.load('Assets/UI/dark_woods.png'), (width + 80, height + 80)).convert()

    # MAIN MENU
    clock = pygame.time.Clock()

    font = pygame.font.Font("Assets/UI/Fonts/OriginTech.ttf", 100)

    levels_text = font.render("LEVELS", True, (255, 255, 255))

    easy = button.Button((255, 255, 255), 620, 300, 220, 100, 80, text="EASY")
    medium = button.Button((255, 255, 255), 560, 500, 350, 100, 80, text="MEDIUM")
    hard = button.Button((255, 255, 255), 620, 700, 220, 100, 80, text="HARD")

    exit = button.Button((255, 255, 255), 1150, 50, 300, 100, 64, text="EXIT")

    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            event_type = event.type

            if event.type == pygame.QUIT:
                run = False

        draw_levels_window()

    pygame.quit()


def easy_init():
    '''initializes game for easy mode'''

    global last_gamemode
    global to_kill, spawn_int
    last_gamemode = "easy"
    to_kill = 5
    spawn_int = 300
    game()


def medium_init():
    '''initializes game for medium mode'''

    global last_gamemode
    global to_kill, spawn_int
    last_gamemode = "medium"
    to_kill = 10
    spawn_int = 200
    game()


def hard_init():
    '''initializes game for hard mode'''

    global last_gamemode
    global to_kill, spawn_int
    last_gamemode = "hard"
    to_kill = 20
    spawn_int = 100
    game()


###############
# INSTRUCTIONS
###############
def ins_setup():
    '''runs the instruction setup'''

    global win, width, height
    global fps, run
    global p, vel_x, vel_y
    global woods

    # SETUP
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Instructions")
    dis_info = pygame.display.Info()
    width = dis_info.current_w
    height = dis_info.current_h

    fps = 50

    p = player.Player(710, 750, 5, "Assets/UI/to_kill.png",
                      "Assets/Cyborg/Cyborg_idle_right.png",
                      "Assets/Cyborg/Cyborg_run_right.png",
                      "Assets/Cyborg/Cyborg_jump_right.png",
                      "Assets/Cyborg/Cyborg_attack3_right.png",
                      "Assets/Cyborg/Cyborg_hurt_right.png",
                      "Assets/Cyborg/Cyborg_death_right.png",
                      "Assets/Cyborg/Cyborg_idle_left.png",
                      "Assets/Cyborg/Cyborg_run_left.png",
                      "Assets/Cyborg/Cyborg_jump_left.png",
                      "Assets/Cyborg/Cyborg_attack3_left.png",
                      "Assets/Cyborg/Cyborg_hurt_left.png",
                      "Assets/Cyborg/Cyborg_death_left.png",
                      4, 6, 4, 8, 2, 6)
    vel_x = 5
    vel_y = 15

    woods = pygame.transform.scale(pygame.image.load('Assets/UI/dark_woods.png'), (width, height)).convert()


def draw_ins_window():
    '''draws the instruction window'''

    global dodge_elapsed, heal_elapsed, to_kill_num_elapsed

    win.blit(woods, (0, 0))

    exit.draw(win)
    button_manager(exit, 64, menu)

    p.draw_self(win)
    p.update_health_bar(win)
    p.update_to_kill(win, 64)

    text = font1.render("60", True, (255, 255, 255))
    win.blit(text, (700, 30))

    if not run_left:
        win.blit(a, (350, 200))
    elif not run_right:
        win.blit(d, (350, 200))
    elif not jump:
        win.blit(space, (350, 200))
    elif not attack:
        win.blit(left_mouse, (50, 200))
    elif not dodge:
        y = 200
        dodge_elapsed += 1
        for line in dodge_text:
            text = font2.render(line, True, (255, 255, 255))
            win.blit(text, (50, y))
            y += 50
    elif not heal:
        y = 200
        heal_elapsed += 1
        for line in heal_text:
            text = font2.render(line, True, (255, 255, 255))
            win.blit(text, (50, y))
            y += 50
    elif not to_kill_num:
        y = 200
        to_kill_num_elapsed += 1
        for line in to_kill_num_text:
            text = font2.render(line, True, (255, 255, 255))
            win.blit(text, (50, y))
            y += 50

    pygame.display.update()


def instructions_screen():
    '''runs the instruction screen'''

    global p_attack_elapsed, dodge_elapsed, heal_elapsed, to_kill_num_elapsed
    global animate, game_over
    global jumping, attacking, can_attack, p_hurt, p_dead
    global run_left, run_right, jump, attack, dodge, heal, to_kill_num
    global hyenas, spells, power_ups
    global font1, font2
    global run, pos, event_type
    global a, d, space, left_mouse, dodge_text, heal_text, to_kill_num_text, exit

    ins_setup()

    clock = pygame.time.Clock()

    anim_elapsed = 0
    p_attack_elapsed = 0
    dodge_elapsed = 0
    heal_elapsed = 0
    to_kill_num_elapsed = 0

    jumping = False
    attacking = False
    can_attack = True
    p_hurt = False
    p_dead = False

    animate = False
    game_over = False

    run_left = False
    run_right = False
    jump = False
    attack = False
    dodge = False
    heal = False
    to_kill_num = False

    hyenas = []
    spells = []
    power_ups = []

    font1 = pygame.font.Font("Assets/UI/Fonts/OriginTech.ttf", 64)
    font2 = pygame.font.Font("Assets/UI/Fonts/OriginTech.ttf", 50)

    a = font1.render("PRESS 'A' TO RUN LEFT", True, (255, 255, 255))
    d = font1.render("PRESS 'D' TO RUN RIGHT", True, (255, 255, 255))
    space = font1.render("PRESS 'SPACE' TO JUMP", True, (255, 255, 255))
    left_mouse = font1.render("PRESS LEFT MOUSE BUTTON TO ATTACK", True, (255, 255, 255))

    dodge_text = ["TRY AND DODGE THE BLACK HOLES SHOT BY THE ",
                  "HYENAS BY JUMPING OVER THEM"]

    heal_text = ["IF YOU DO TAKE DAMAGE TO THE BLACK HOLES, ",
                 "YOU CAN WALK OVER THE MEDKITS TO HEAL"]

    to_kill_num_text = ["ELIMINATE AS MANY HYENAS AS SHOWN IN THE ",
                        "TOP RIGHT CORNER OF THE GAME IN THE GIVEN ",
                        "AMOUNT OF TIME TO WIN"]

    exit = button.Button((255, 255, 255), 1190, 50, 300, 100, 64, text="EXIT")

    run = True
    while run:
        clock.tick(fps)

        anim_elapsed += 1
        p_attack_elapsed += 1

        # make sure animation is slower than movement
        if anim_elapsed == 5:
            animate = True
            anim_elapsed = 0
        else:
            animate = False

        # make sure player cannot spam attack
        if p_attack_elapsed == 35:
            can_attack = True

        if dodge_elapsed == 300:
            dodge = True

        if heal_elapsed == 300:
            heal = True

        if to_kill_num_elapsed == 400:
            to_kill_num = True

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            event_type = event.type

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: # Make sure user has to click key individually for each iteration

                # ATTACK AND CHECK ATTACK
                if event.button == 1 and attacking is False and can_attack and p.action != "jump":
                    attacking = True
                    attack = True
                    if p.direction == "right":
                        p.attack_index = 0
                    elif p.direction == "left":
                        p.attack_index = 6

            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()

                # CHECK RUN AND JUMP
                if key_pressed[pygame.K_a]:
                    run_left = True
                elif key_pressed[pygame.K_d]:
                    run_right = True
                elif key_pressed[pygame.K_SPACE]:
                    jump = True

        player_controller()

        draw_ins_window()

    pygame.quit()


###############
# GAME
###############
def setup():
    '''runs the setup for main game'''

    global win, width, height
    global fps
    global p, vel_x, vel_y
    global woods
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Pitch Black")
    dis_info = pygame.display.Info()
    width = dis_info.current_w
    height = dis_info.current_h

    fps = 50

    p = player.Player(710, 750, to_kill, "Assets/UI/to_kill.png",
                      "Assets/Cyborg/Cyborg_idle_right.png",
                      "Assets/Cyborg/Cyborg_run_right.png",
                      "Assets/Cyborg/Cyborg_jump_right.png",
                      "Assets/Cyborg/Cyborg_attack3_right.png",
                      "Assets/Cyborg/Cyborg_hurt_right.png",
                      "Assets/Cyborg/Cyborg_death_right.png",
                      "Assets/Cyborg/Cyborg_idle_left.png",
                      "Assets/Cyborg/Cyborg_run_left.png",
                      "Assets/Cyborg/Cyborg_jump_left.png",
                      "Assets/Cyborg/Cyborg_attack3_left.png",
                      "Assets/Cyborg/Cyborg_hurt_left.png",
                      "Assets/Cyborg/Cyborg_death_left.png",
                      4, 6, 4, 8, 2, 6)
    vel_x = 5
    vel_y = 15

    woods = pygame.transform.scale(pygame.image.load('Assets/UI/dark_woods.png'), (width, height)).convert()


def draw_game_window():
    '''draws the game window'''

    win.blit(woods, (0, 0))

    for power_up in power_ups:
        power_up.draw_self(win)

    for h in hyenas:
        h.draw_self(win)
        if h.action != "die":
            h.update_health_bar(win)

    p.draw_self(win)
    p.update_health_bar(win)
    p.update_to_kill(win, 64)
    if game_paused is False:
        update_timer()
        pause.draw(win)

    for s in spells:
        s.draw_self(win)

    if game_paused:
        pause_screen()

    if game_over:
        game_over_screen()

    pygame.display.update()


def game_over_screen():
    '''runs the game over screen'''

    game_over_win = pygame.Surface((1920, 1080), pygame.SRCALPHA)
    game_over_win.fill((0, 0, 0, 128))
    win.blit(game_over_win, (0, 0))

    if p_win:
        win.blit(vic_result, (500, 200))
    else:
        win.blit(def_result, (520, 200))

    restart.draw(win)
    button_manager(restart, 80, game)

    quit.draw(win)
    button_manager(quit, 80, quit_game)

    quit.draw(win)
    button_manager(quit, 80, quit_game)

    main_menu.draw(win)
    button_manager(main_menu, 80, menu)


def pause_screen():
    '''runs the pause screen'''

    pause_win = pygame.Surface((1920, 1080), pygame.SRCALPHA)
    pause_win.fill((0, 0, 0, 128))
    win.blit(pause_win, (0, 0))

    win.blit(paused, (520, 200))

    resume.draw(win)
    button_manager(resume, 80, resume_game)

    quit.draw(win)
    button_manager(quit, 80, quit_game)

    main_menu.draw(win)
    button_manager(main_menu, 80, menu)


def button_manager(but, orig_size, func):
    '''manages a button in game
    :param but: button it is managing
    :param orig_size: original size of button
    :param func: function to run if player hits button'''

    if event_type == pygame.MOUSEBUTTONDOWN:
        if but.is_over(pos):
            func()

    if event_type == pygame.MOUSEMOTION:
        if but.is_over(pos):
            but.font_size = orig_size + 20
        else:
            but.font_size = orig_size


def update_timer():
    '''updates game timer'''

    global timer, timer_elapsed
    global p_win, game_over

    text = font1.render(str(timer), True, (255, 255, 255))
    win.blit(text, (700, 30))

    if timer <= 0:
        game_over = True
        p_win = False

    if timer_elapsed >= 50 and game_over is False:
        timer -= 1
        timer_elapsed = 0


def pause_game():
    '''pauses game'''

    global game_paused
    game_paused = True


def resume_game():
    '''resumes game'''

    global game_paused
    game_paused = False


def quit_game():
    '''quits game'''

    global run
    run = False


def player_controller():
    '''lets the user control the player'''

    global jumping, attacking, can_attack, p_hurt, p_dead, p_win, game_over
    global p_attack_elapsed, p_heal_elapsed, p_hurt_elapsed
    global vel_y

    key_pressed = pygame.key.get_pressed()

    if jumping is False and key_pressed[pygame.K_SPACE]:  # make sure cannot jump in air
        jumping = True
        attacking = False

    ##################
    # WIN
    ##################
    if p.to_kill <= 0 and p.action != "jump":
        p.action = "idle"

        p_win = True

        if p.idle_index > 2 and animate:
            p.idle_index = 0
            game_over = True
        elif animate:
            p.idle_index += 1

    ##################
    # DIE
    ##################
    elif p.health <= 0:
        p.action = "die"

        p_win = False

        if p.direction == "right":  # DIE RIGHT
            if p.die_right_index > 4 and animate:
                p_dead = True
                game_over = True
            elif animate:
                p.die_right_index += 1

        elif p.direction == "left":  # DIE RIGHT
            if p.die_left_index < 1 and animate:
                p_dead = True
                game_over = True
            elif animate:
                p.die_left_index -= 1

    ##################
    # HEAL
    ##################
    elif p.action == "heal":
        p_heal_elapsed += 1

        p.heal(20 / 15)

        if p.idle_index > 2 and animate:
            p.idle_index = 0
        elif animate:
            p.idle_index += 1

    ##################
    # HURT
    ##################
    elif p_hurt:
        p.action = "hurt"

        p_hurt_elapsed += 1

        p.take_damage(p.dam_taken_from.damage / 15)

        if p.dam_taken_from.producer.direction == "right":
            p.x += 1

        elif p.dam_taken_from.producer.direction == "left":
            p.x -= 1

        if p.direction == "right":  # HURT RIGHT
            if p_hurt_elapsed > 15:
                p_hurt_elapsed = 0
                p_hurt = False
            else:
                p.hurt_index = 1

        elif p.direction == "left":  # HURT LEFT
            if p_hurt_elapsed > 15:
                p_hurt_elapsed = 0
                p_hurt = False
            else:
                p.hurt_index = 0

    ##################
    # JUMP
    ##################
    elif jumping and game_over is False:
        p.action = "jump"
        p.y -= vel_y
        vel_y -= 2
        if vel_y < -15:
            jumping = False
            vel_y = 15

        if key_pressed[pygame.K_d]:  # JUMP RIGHT
            p.direction = "right"
            if 1355 > p.x:
                p.x += vel_x
            if p.jump_index > 2 and animate:
                p.jump_index = 0
            elif animate:
                p.jump_index += 1

        elif key_pressed[pygame.K_a]:  # JUMP LEFT
            p.direction = "left"
            if p.x > -20:
                p.x -= vel_x
            if p.jump_index < 1 and animate:
                p.jump_index = 3
            elif animate:
                p.jump_index -= 1

    ##################
    # ATTACK
    ##################
    elif attacking and game_over is False:
        p.action = "attack"

        if p.direction == "right":  # ATTACK RIGHT
            if p.attack_index > 6 and animate:
                attacking = False
                can_attack = False
                p_attack_elapsed = 0
            elif animate:
                p.attack_index += 1

        elif p.direction == "left":  # ATTACK LEFT
            if p.attack_index < 1 and animate:
                attacking = False
                can_attack = False
                p_attack_elapsed = 0
            elif animate:
                p.attack_index -= 1

        for h in hyenas:
            h_x_dist = abs(p.x - h.x)

            if h.direction == "right":
                if p.direction == "left":
                    x_thres = 70
                elif p.direction == "right":
                    x_thres = 50
                if h_x_dist < x_thres:
                    h.action = "hurt"

            elif h.direction == "left":
                if p.direction == "right":
                    x_thres = 70
                elif p.direction == "left":
                    x_thres = 50
                if h_x_dist < x_thres:
                    h.action = "hurt"



    ##################
    # RUN
    ##################
    elif key_pressed[pygame.K_d] and game_over is False:  # RUN RIGHT
        p.action = "run"
        p.direction = "right"

        if 1355 > p.x:
            p.x += vel_x
        if p.run_index > 4 and animate:
            p.run_index = 0
        elif animate:
            p.run_index += 1

    elif key_pressed[pygame.K_a] and game_over is False:  # RUN LEFT
        p.action = "run"
        p.direction = "left"

        if p.x > -20:
            p.x -= vel_x
        if p.run_index < 1 and animate:
            p.run_index = 5
        elif animate:
            p.run_index -= 1

    ##################
    # IDLE
    ##################
    else:  # IDLE RIGHT OR LEFT
        p.action = "idle"

        if p.idle_index > 2 and animate:
            p.idle_index = 0
        elif animate:
            p.idle_index += 1


def hyena_controller():
    '''manages all hyenas in game'''

    global hyenas, spells

    if spawn_hyena or len(hyenas) == 0:
        h_direction = random.choice(["right", "left"])

        if h_direction == "right":
            h_x = -75
        elif h_direction == "left":
            h_x = width + 75

        hy = hyena.Hyena(h_x, 750, h_direction,
                        "Assets/Hyena/Hyena_idle_right.png",
                        "Assets/Hyena/Hyena_run_right.png",
                        "Assets/Hyena/Hyena_attack_right.png",
                        "Assets/Hyena/Hyena_hurt_right.png",
                        "Assets/Hyena/Hyena_death_right.png",
                        "Assets/Hyena/Hyena_idle_left.png",
                        "Assets/Hyena/hyena_run_left.png",
                        "Assets/Hyena/Hyena_attack_left.png",
                        "Assets/Hyena/Hyena_hurt_left.png",
                        "Assets/Hyena/Hyena_death_left.png",
                         4, 6, 6, 2, 6)
        hyenas.append(hy)

    for h in hyenas:
        if random.randint(1, 300) == 1 and h.action != "attack":  # will hyena attack or not
            h.action = "attack"

    for h in hyenas:
        if -100 < h.x < 1700:
            ##################
            # DIE
            ##################
            if h.health <= 0:
                h.action = "die"

                if h.direction == "right":
                    if h.die_right_index < 1 and animate:
                        h.die_elapsed += 1
                        if h.die_elapsed == 50:
                            h.die_elapsed = 0
                            hyenas.remove(h)
                            del h
                    elif animate:
                        h.die_right_index -= 1

                elif h.direction == "left":
                    if h.die_left_index > 4 and animate:
                        h.die_elapsed += 1
                        if h.die_elapsed == 50:
                            h.die_elapsed = 0
                            hyenas.remove(h)
                            del h
                    elif animate:
                        h.die_left_index += 1

            ##################
            # HURT
            ##################
            elif h.action == "hurt":
                h.hurt_elapsed += 1

                h.take_damage(p.damage / 40)

                if h.health <= 0:
                    p.to_kill -= 1

                if h.direction == "right":  # HURT RIGHT
                    if h.hurt_elapsed > 40:
                        h.hurt_elapsed = 0
                        h.action = "run"
                    else:
                        h.hurt_right_index = 1

                elif h.direction == "left":  # HURT LEFT
                    if h.hurt_elapsed > 40:
                        h.hurt_elapsed = 0
                        h.action = "run"
                    else:
                        h.hurt_left_index = 0

            ##################
            # ATTACK
            ##################
            elif h.action == 'attack':
                if h.direction == "right":  # ATTACK RIGHT
                    if h.attack_right_index < 1 and animate:
                        h.attack_right_index = h.attack_cols - 1
                        h.action = "run"
                    elif animate:
                        h.attack_right_index -= 1
                        if h.attack_right_index == 2:
                            sp = spell.Spell(h.x + 35, 780, h)
                            spells.append(sp)
                elif h.direction == "left":  # ATTACK LEFT
                    if h.attack_left_index > 4 and animate:
                        h.attack_left_index = 0
                        h.action = "run"
                    elif animate:
                        h.attack_left_index += 1
                        if h.attack_left_index == 2:
                            sp = spell.Spell(h.x, 780, h)
                            spells.append(sp)

            ##################
            # RUN
            ##################
            elif h.action == "run":
                if h.direction == "right":  # RUN RIGHT
                    h.x += 1
                    if h.run_right_index < 1 and animate:
                        h.run_right_index = 5
                    elif animate:
                        h.run_right_index -= 1
                elif h.direction == "left":  # RUN LEFT
                    h.x -= 1
                    if h.run_left_index > 4 and animate:
                        h.run_left_index = 0
                    elif animate:
                        h.run_left_index += 1
        else:
            hyenas.remove(h)
            del h


def spell_controller():
    '''manages all spells in the game'''

    global spells
    global p_hurt
    for s in spells:
        if -50 < s.x < 1500:
            ##################
            # SPELL ANIMATION
            ##################
            if s.producer.direction == "right":
                s.x += 5
            elif s.producer.direction == "left":
                s.x -= 5

            if s.spell_index > 6 and animate:
                s.spell_index = 0
            elif animate:
                s.spell_index += 1

            ##################
            # HIT PLAYER
            ##################
            s_x_dist = p.x - s.x
            s_y_dist = abs(p.y - s.y)

            if s.producer.direction == "right":
                if -20 < s_x_dist < 5 and s_y_dist < 40 and game_over is False:
                    p_hurt = True
                    p.dam_taken_from = s
                    spells.remove(s)
                    del s

            elif s.producer.direction == "left":
                if 0 > s_x_dist > -50 and s_y_dist < 40 and game_over is False:
                    p_hurt = True
                    p.dam_taken_from = s
                    spells.remove(s)
                    del s
        else:
            spells.remove(s)
            del s


def power_up_controller():
    '''manages all powerups in game'''
    global p_heal_elapsed

    chance = random.randint(1, 750)
    types = ["health"]

    # make sure power up does not spawn close to player
    x = random.randint(100, 1200)
    while abs(p.x - x) < 100:
        x = random.randint(100, 1000)

    # make sure power up only spawns if lucky and health is lower than max
    if chance == 1 and p.health < p.max_health and game_over is False:
        power_up = pu.Powerup(x, 800, random.choice(types))
        power_ups.append(power_up)

    for pow_up in power_ups:
        x_dist = abs(p.x - pow_up.x)
        y_dist = abs(p.y - pow_up.y)

        if p.x > pow_up.x:
            x_thres = 20
        else:
            x_thres = 50

        if x_dist < x_thres and y_dist < 75 and game_over is False:
            pow_up.take_effect(p)
            if p_heal_elapsed > 15:
                p_heal_elapsed = 0
                p.action = "idle"
                power_ups.remove(pow_up)
                del pow_up
        elif pow_up.elapsed >= 250 or p.health == p.max_health:
            power_ups.remove(pow_up)
            del pow_up


def game():
    '''runs main game'''

    global hyenas, spells, power_ups
    global jumping, attacking, can_attack, p_hurt, p_dead, timer, game_paused, p_win, game_over, run
    global timer_elapsed, animate, spawn_hyena, p_attack_elapsed, p_heal_elapsed, p_hurt_elapsed
    global pos, event_type, font1, pause
    global paused, vic_result, def_result, resume, restart, main_menu, quit

    # GAME INIT
    setup()

    clock = pygame.time.Clock()

    timer = 60
    game_paused = False
    p_win = False
    game_over = False

    hyenas = []
    spells = []
    power_ups = []

    timer_elapsed = 0
    anim_elapsed = 0
    spawn_elapsed = 0
    p_attack_elapsed = 0
    p_heal_elapsed = 0
    p_hurt_elapsed = 0

    jumping = False
    attacking = False
    can_attack = True
    p_hurt = False
    p_dead = False

    font1 = pygame.font.Font("Assets/UI/Fonts/OriginTech.ttf", 64)
    font2 = pygame.font.Font("Assets/UI/Fonts/OriginTech.ttf", 100)

    pause = button.Button((255, 255, 255), 1350, 10, 100, 100, 80, text="ii")

    # PAUSE SCREEN AND GAME OVER SCREEN INIT
    paused = font2.render("PAUSED", True, (255, 255, 255))
    vic_result = font2.render("VICTORY", True, (255, 255, 255))
    def_result = font2.render("DEFEAT", True, (255, 255, 255))

    resume = button.Button((255, 255, 255), 520, 400, 400, 100, 80, text="RESUME")
    restart = button.Button((255, 255, 255), 520, 400, 400, 100, 80, text="RESTART")
    main_menu = button.Button((255, 255, 255), 480, 550, 500, 100, 80, text="MAIN MENU")
    quit = button.Button((255, 255, 255), 620, 700, 200, 100, 80, text="QUIT")

    # GAME LOOP
    run = True
    while run:
        clock.tick(fps)

        timer_elapsed += 1
        anim_elapsed += 1
        spawn_elapsed += 1
        p_attack_elapsed += 1

        # make sure animation is slower than movement
        if anim_elapsed == 5:
            animate = True
            anim_elapsed = 0
        else:
            animate = False

        # make sure hyena is spawned in specific times only
        if spawn_elapsed == spawn_int:
            spawn_hyena = True
            spawn_elapsed = 0
        else:
            spawn_hyena = False

        # make sure player cannot spam attack
        if p_attack_elapsed == 35:
            can_attack = True

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            event_type = event.type

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: # Make sure user has to click key individually for each iteration

                # ATTACK
                if event.button == 1 and attacking is False and can_attack and p.action != "jump":
                    attacking = True
                    if p.direction == "right":
                        p.attack_index = 0
                    elif p.direction == "left":
                        p.attack_index = 6

            # PAUSE BUTTON
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause.is_over(pos):
                    pause_game()

            if event.type == pygame.MOUSEMOTION:
                if pause.is_over(pos):
                    pause.font_size = 100
                else:
                    pause.font_size = 80

        if game_paused is False:
            player_controller()
            hyena_controller()
            spell_controller()
            power_up_controller()

        draw_game_window()

    pygame.quit()

menu()