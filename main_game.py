import datetime
from itertools import cycle

import pygame.transform

from Game import *
from Player import *
from Enemies.Enemy import *
from Enemies.SideswiperEnemy import SideswiperEnemy
from Enemies.FranticEnemy import FranticEnemy

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# screen window caption and icon
pygame.display.set_caption("Galacticon")
icon = pygame.image.load("assets/logo.png").convert_alpha()
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
game = Game()


def begin_screen():
    pygame.mixer.music.load("assets/undertale_dating_tense.wav")
    pygame.mixer.music.play(-1)

    galacticon_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 64)
    colors = [(62, 216, 18), (11, 50, 253)]
    iterator = cycle(range(2))

    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 16)
    menu_text = menu_font.render("Press ENTER to play!", True, (255, 255, 255))
    screen.blit(menu_text, (240, 200))
    menu_text = menu_font.render("Press A for instructions!", True, (255, 255, 255))
    screen.blit(menu_text, (200, 230))
    menu_text = menu_font.render("Press S to see the scoreboard!", True, (255, 255, 255))
    screen.blit(menu_text, (170, 260))
    menu_text = menu_font.render("Press U for no reason whatsoever!", True, (255, 255, 255))
    screen.blit(menu_text, (150, 290))

    begin_screen_running = True
    color_swap_time = datetime.datetime.now()
    while begin_screen_running:
        # title colors
        if datetime.datetime.now() >= color_swap_time:
            color_swap_time = datetime.datetime.now() + datetime.timedelta(seconds=0.3)
            next(iterator)
            galacticon_text_1 = galacticon_font.render("G L C I O", True, colors[next(iterator)])
            galacticon_text_2 = galacticon_font.render("A A T C N", True, colors[next(iterator)])
            screen.blit(galacticon_text_1, (80, 80))
            screen.blit(galacticon_text_2, (144, 80))

        # keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    begin_screen_running = False
                if event.key == pygame.K_a:
                    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect(0, 350, 800, 600))

                    arrow_keys_img = pygame.image.load("assets/arrow_keys.png").convert()
                    arrow_keys_img.set_colorkey((0, 0, 0))
                    screen.blit(arrow_keys_img, (50, 380))
                    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 12)
                    arrow_keys_text = menu_font.render("press and hold the", True, (255, 255, 255))
                    screen.blit(arrow_keys_text, (130, 380))
                    arrow_keys_text = menu_font.render("arrow keys to move", True, (255, 255, 255))
                    screen.blit(arrow_keys_text, (130, 400))

                    space_bar_img = pygame.image.load("assets/space_bar.png").convert()
                    space_bar_img.set_colorkey((0, 0, 0))
                    space_bar_img = pygame.transform.scale(space_bar_img, (128, 32))
                    screen.blit(space_bar_img, (40, 450))
                    arrow_keys_text = menu_font.render("press the space", True, (255, 255, 255))
                    screen.blit(arrow_keys_text, (180, 450))
                    arrow_keys_text = menu_font.render("bar to fire", True, (255, 255, 255))
                    screen.blit(arrow_keys_text, (180, 470))

                    sideswiper_img = pygame.image.load("assets/sideswiper.png").convert()
                    sideswiper_img.set_colorkey((0, 0, 0))
                    screen.blit(sideswiper_img, (640, 385))
                    splicer_img = pygame.image.load("assets/splicer.png").convert()
                    splicer_img.set_colorkey((0, 0, 0))
                    screen.blit(splicer_img, (520, 450))
                    enemy_text = menu_font.render("watch out for these guys!", True, (255, 255, 255))
                    screen.blit(enemy_text, (460, 435))
                if event.key == pygame.K_s:
                    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect(0, 350, 800, 600))
                    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 16)
                    y_coord = 370
                    score_records = Game.read_scoreboard(5)
                    for score_record in score_records:
                        score_text = menu_font.render(score_record[0], True, (255, 255, 255))
                        screen.blit(score_text, (290, y_coord))
                        score_text = menu_font.render(str(score_record[1].rjust(7, "0")), True, (255, 255, 255))
                        screen.blit(score_text, (390, y_coord))
                        y_coord += 30
                if event.key == pygame.K_u:
                    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect(0, 350, 800, 600))
                    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 20)
                    arrow_keys_text = menu_font.render("Well that was pointless.", True, (255, 255, 255))
                    screen.blit(arrow_keys_text, (130, 430))

        pygame.display.update()


def play_game():
    # start game music
    pygame.mixer.music.load("assets/deltarune_knock_you_down.wav")
    pygame.mixer.music.play(-1)

    enemies_grid = game.get_cur_enemy_setup()
    player = Player()

    # game loop
    game_running = True
    while game_running:
        level_is_completed = False
        player_x_change = 0
        player_y_change = 0

        level_running = True
        while level_running:
            screen.fill((0, 0, 0))

            # keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_x_change = -3
                    if event.key == pygame.K_RIGHT:
                        player_x_change = 3
                    if event.key == pygame.K_UP:
                        player_y_change = -3
                    if event.key == pygame.K_DOWN:
                        player_y_change = 3
                    if event.key == pygame.K_SPACE:
                        player.fire()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player_x_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_y_change = 0

            # move and display the player
            player.move(player_x_change, player_y_change)
            player.display(screen)

            # move and display the player's bullets
            player.move_bullets()
            player.remove_offscreen_bullets()
            for bullet in player.bullets_fired:
                bullet.display(screen)

            # move and check if the player caught (then display) the bonuses
            game.random_bonus_drop()
            game.move_bonuses()
            game.remove_offscreen_bonuses()
            game.received_bonus(player)
            for bonus in game.bonuses_dropped:
                bonus.display(screen)

            # for each enemy
            for enemy_line in enemies_grid:
                for enemy in enemy_line:

                    # move and display the enemy's bullets
                    enemy.random_fire()
                    enemy.move_bullets()
                    enemy.remove_offscreen_bullets()
                    for bullet in enemy.bullets_fired:
                        bullet.display(screen)

                    # check if the enemy shot or collided with the player
                    if player.collided_with_bullet(enemy.bullets_fired) or player.collided_with_enemy(enemy):
                        player.lose_life()
                        level_running = False

                    # move the enemy
                    enemy.move()

                    # check if the enemy was shot
                    colliding_bullet = enemy.collided_with_bullet(player.bullets_fired)
                    if colliding_bullet != -1:
                        enemy.hit()
                        player.bullets_fired.pop(colliding_bullet)
                        game.increase_score(enemy.score_value)

                    # display the enemy
                    enemy.display(screen)

                    # trigger FranticEnemies once a number of enemies have been defeated
                    if isinstance(enemy, FranticEnemy) and game.get_cur_level().get_num_enemies_defeated() > 8:
                        enemy.is_frantic = True

            # deploy the splicer
            game.random_splicer_deployment(player.x)

            # check if the player collided with the splicer's laserbeam
            if player.collided_with_bullet(game.splicer.laserbeam_components):
                player.lose_life()
                level_running = False

            # display the splicer and it's laserbeam
            for laserbeam in game.splicer.laserbeam_components:
                laserbeam.display(screen)
            game.splicer.display(screen)

            # update the game screen display
            game.display_data(screen, player.lives)
            clock.tick(75)
            pygame.display.update()

            # check if the level was completed
            level_is_completed = game.is_current_level_completed()
            if level_is_completed:
                level_running = False

        # end level

        # clear bullets and special enemies from screen
        player.bullets_fired.clear()
        for enemy_line in enemies_grid:
            for enemy in enemy_line:
                enemy.bullets_fired.clear()
                if isinstance(enemy, SideswiperEnemy):
                    enemy.move_offscreen()
        game.splicer.move_offscreen()
        game.splicer_deployed = False

        if player.lives == 0:  # game over
            Game.game_over_message(screen)
            game_running = False
        elif game.is_completed():  # game won
            Game.game_completed_message(screen)
            game_running = False
        elif level_is_completed:  # beat level
            game.go_to_next_level(screen)
            enemies_grid = game.get_cur_enemy_setup()
        elif game_running:  # lost life
            Game.resuscitation_message(screen)
            player.recenter()

        pygame.display.update()
        pygame.time.wait(2000)

    # end game


def end_screen():
    screen.fill((0, 0, 0))
    score_records = Game.read_scoreboard(10)

    # display "HIGH SCORE" if one was achieved
    achieved_high_score = len([record[1] for record in score_records if int(record[1]) > game.current_score]) < 10
    if achieved_high_score:
        menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 48)
        score_text = menu_font.render("HIGH SCORE", True, (255, 215, 0))
        screen.blit(score_text, (160, 80))

    # display the player's score
    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 42)
    score_text = menu_font.render("You got:", True, (255, 215, 0))
    screen.blit(score_text, (240, 450))
    score_text = menu_font.render(str(game.current_score).rjust(7, "0"), True, (255, 215, 0))
    screen.blit(score_text, (250, 510))

    # enter the player's initials
    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 24)
    initials_text = menu_font.render("Enter your initials:", True, (255, 255, 255))
    screen.blit(initials_text, (170, 200))
    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 16)
    initials_text = menu_font.render("(three, specifically)", True, (255, 255, 255))
    screen.blit(initials_text, (235, 230))
    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 64)
    initials = ""
    while len(initials) < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.TEXTINPUT:
                initials += event.text.capitalize()
                initial_text = menu_font.render(initials, True, (255, 255, 255))
                screen.blit(initial_text, (300, 310))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    initials = initials[:-1]
                    initial_text = menu_font.render(initials, True, (255, 255, 255))
                    screen.blit(initial_text, (300, 310))
        pygame.display.update()

    # Easter Egg!
    if initials == "WHY":
        menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 24)
        easter_egg_text = menu_font.render("because.", True, (255, 0, 0))
        screen.blit(easter_egg_text, (500, 400))
        pygame.display.update()
        pygame.time.wait(200)

    pygame.time.wait(400)

    # display the scoreboard (top 10)
    screen.fill((0, 0, 0))
    new_score = game.write_scoreboard(initials)
    score_records = Game.read_scoreboard(10)
    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 24)
    y_coord = 100
    for score_record in score_records:
        color = (255, 215, 0) if score_record[1] == new_score[1] else (255, 255, 255)
        score_text = menu_font.render(score_record[0], True, color)
        screen.blit(score_text, (250, y_coord))
        score_text = menu_font.render(str(score_record[1]).rjust(7, "0"), True, color)
        screen.blit(score_text, (380, y_coord))
        y_coord += 36
        pygame.display.update()
        pygame.time.wait(100)
    if not achieved_high_score:
        score_text = menu_font.render(new_score[0], True, (255, 215, 0))
        screen.blit(score_text, (250, 550))
        score_text = menu_font.render(str(new_score[1]).rjust(7, "0"), True, (255, 215, 0))
        screen.blit(score_text, (380, 550))
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                exit()


if __name__ == "__main__":
    begin_screen()
    play_game()
    end_screen()
