from Player import *
from Enemy import *

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# screen window caption and icon
pygame.display.set_caption("Galacticon")
icon = pygame.image.load("assets/logo.png").convert()
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


def show_game_data(score_value, lives_value):
    font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 16)
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    lives = font.render("Lives:" + str(lives_value), True, (255, 255, 255))
    screen.blit(score, (0, 584))
    screen.blit(lives, (140, 584))


def get_ready():
    get_ready_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 24)
    get_ready_text = get_ready_font.render("You Died! Get Ready To Continue", True, (255, 255, 255))
    screen.blit(get_ready_text, (30, 250))


def game_over():
    game_over_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 64)
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (110, 250))


def enemy_line_setup(enemy_img):
    line1 = [Enemy(x, 20, enemy_img) for x in range(10, 736, 100)]
    line2 = [Enemy(x, 100, enemy_img) for x in range(10, 736, 100)]
    line3 = [Enemy(x, 180, enemy_img) for x in range(10, 736, 100)]
    return [line1, line2, line3]


def is_collision(ship, bullet_list):
    for i in range(len(bullet_list)):
        dx = bullet_list[i].x - ship.x
        dy = bullet_list[i].y - ship.y
        if ship.mask.overlap(bullet_list[i].mask, (dx, dy)) is not None:
            return True, i
    return False, -1


def main():
    player = Player()
    original_enemy_img = pygame.image.load("assets/enemy1.png").convert()
    original_enemy_img.set_colorkey((0, 0, 0))
    enemies_grid = enemy_line_setup(pygame.transform.scale(original_enemy_img, (54, 54)))
    score_value = 0

    # game loop
    game_running = True
    while game_running:
        player_x_change = 0
        player_y_change = 0

        level_running = True
        while level_running:
            screen.fill((0, 0, 0))

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
                    # player loses life
                    if is_collision(player, enemy.bullets_fired)[0]:
                        player.lose_life()
                        level_running = False
                    enemy.move()
                    # enemy shot
                    (collided, colliding_bullet) = is_collision(enemy, player.bullets_fired)
                    if collided:
                        enemy.explode()
                        player.bullets_fired.pop(colliding_bullet)
                        score_value += 1
                    enemy.display(screen)

                    # enemy bullet movement
                    enemy.random_fire()
                    enemy.move_bullets()
                    enemy.bullets_fired = list(filter(lambda b: b.y >= 0, enemy.bullets_fired))
                    for bullet in enemy.bullets_fired:
                        bullet.display(screen)

            show_game_data(score_value, player.lives)
            clock.tick(75)
            pygame.display.update()

        # level stopped
        player.bullets_fired.clear()
        for enemy_line in enemies_grid:
            for enemy in enemy_line:
                enemy.bullets_fired.clear()

        # player lost life
        if player.lives == 0:
            game_over()
            game_running = False
        elif game_running:
            get_ready()
            player.recenter()

        pygame.display.update()
        pygame.time.wait(1000)


main()
