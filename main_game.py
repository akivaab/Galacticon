from Game import *
from Player import *
from ClassicEnemy import *

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# screen window caption and icon
pygame.display.set_caption("Galacticon")
icon = pygame.image.load("assets/logo.png").convert_alpha()
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# start game music
pygame.mixer.music.load("assets/deltarune_knock_you_down.wav")
pygame.mixer.music.play(-1)


def main():
    game = Game()
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
                    pygame.display.set_caption("You DARE quit Galacticon?!! YOU SHALL REGRET THIS!!")
                    level_running = False
                    game_running = False
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

            # move the player
            player.move(player_x_change, player_y_change)

            # move and display the player's bullets
            player.move_bullets()
            player.remove_offscreen_bullets()
            for bullet in player.bullets_fired:
                bullet.display(screen)

            # for each enemy
            for enemy_line in enemies_grid:
                for enemy in enemy_line:

                    # move and display the enemy's bullets
                    enemy.random_fire()
                    enemy.move_bullets()
                    enemy.remove_offscreen_bullets()
                    for bullet in enemy.bullets_fired:
                        bullet.display(screen)

                    # check if the enemy shot the player
                    if player.collided_with_bullet(enemy.bullets_fired):  # or is_collision(player, enemy)
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

            # display the player
            player.display(screen)

            # update the game screen display
            game.display_data(screen, player.lives)
            clock.tick(75)
            pygame.display.update()

            # check if the level was completed
            level_is_completed = game.is_current_level_completed()
            if level_is_completed:
                level_running = False

        # end level

        # clear bullets from screen
        player.bullets_fired.clear()
        for enemy_line in enemies_grid:
            for enemy in enemy_line:
                enemy.bullets_fired.clear()
                if isinstance(enemy, SideswiperEnemy):
                    enemy.move_offscreen()

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
        pygame.time.wait(1500)

    # end game


main()
