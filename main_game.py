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

pygame.mixer.music.load("assets/deltarune_knock_you_down.wav")
pygame.mixer.music.play(-1)


def is_collision(obj1, obj2):
    if isinstance(obj2, list):
        for i in range(len(obj2)):
            dx = obj2[i].x - obj1.x
            dy = obj2[i].y - obj1.y
            if obj1.mask.overlap(obj2[i].mask, (dx, dy)) is not None:
                return True, i
        return False, -1
    else:
        dx = obj2.x - obj1.x
        dy = obj2.y - obj1.y
        if obj1.mask.overlap(obj2.mask, (dx, dy)) is not None:
            return True
        return False


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

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.set_caption("You DARE quit Galacticon?!! YOU SHALL REGRET THIS!!")
                    level_running = False
                    game_running = False
                # arrow keystrokes
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
            player.move(player_x_change, player_y_change)

            # player bullet movement
            player.move_bullets()
            player.bullets_fired = list(filter(lambda b: b.y >= 0, player.bullets_fired))
            for bullet in player.bullets_fired:
                bullet.display(screen)

            player.display(screen)

            for enemy_line in enemies_grid:
                for enemy in enemy_line:

                    # enemy bullet movement
                    enemy.random_fire()
                    enemy.move_bullets()
                    enemy.bullets_fired = list(filter(lambda b: b.y >= 0, enemy.bullets_fired))
                    for bullet in enemy.bullets_fired:
                        bullet.display(screen)

                    # player loses life
                    if is_collision(player, enemy.bullets_fired)[0]:  # or is_collision(player, enemy)
                        player.lose_life()
                        level_running = False
                    enemy.move()
                    # enemy shot
                    (collided, colliding_bullet) = is_collision(enemy, player.bullets_fired)
                    if collided:
                        enemy.hit()
                        player.bullets_fired.pop(colliding_bullet)
                        game.increase_score(enemy.score_value)
                    enemy.display(screen)

            game.display_data(screen, player.lives)
            clock.tick(75)
            pygame.display.update()

            # level completed
            level_is_completed = game.is_current_level_completed()
            if level_is_completed:
                level_running = False

        # level stopped
        player.bullets_fired.clear()
        for enemy_line in enemies_grid:
            for enemy in enemy_line:
                enemy.bullets_fired.clear()
                if isinstance(enemy, SideswiperEnemy):
                    enemy.move_offscreen()

        if player.lives == 0:
            Game.game_over_message(screen)
            game_running = False
        elif level_is_completed:
            game.go_to_next_level(screen)
            enemies_grid = game.get_cur_enemy_setup()
        # player lost life
        elif game_running:
            Game.resuscitation_message(screen)
            player.recenter()

        pygame.display.update()
        pygame.time.wait(1500)


main()
