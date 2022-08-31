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
                        score_text = menu_font.render(score_record[1], True, (255, 255, 255))
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

    # Ask for 3-letter name, temporarily TNT

    score_records = game.write_scoreboard("TNT")
    menu_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 32)
    y_coord = 150
    for score_record in score_records:
        score_text = menu_font.render(score_record[0], True, (255, 255, 255))
        screen.blit(score_text, (290, y_coord))
        score_text = menu_font.render(score_record[1], True, (255, 255, 255))
        screen.blit(score_text, (390, y_coord))
        y_coord += 30

    pygame.display.update()
    pygame.time.wait(5000)


if __name__ == "__main__":
    begin_screen()
    play_game()
    end_screen()
