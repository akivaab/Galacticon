import pygame
from Bullet import *
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

score_value = 0


def show_score():
    font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 16)
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (0, 584))


def game_over():
    game_over_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 64)
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (110, 250))


def enemy_line_setup(enemy_img):
    line1 = [Enemy(x, 20, enemy_img) for x in range(0, 736, 80)]
    line2 = [Enemy(x, 100, enemy_img) for x in range(0, 736, 80)]
    line3 = [Enemy(x, 180, enemy_img) for x in range(0, 736, 80)]
    return [line1, line2, line3]


def main():
    player = Player()
    enemies = enemy_line_setup()

    # game loop
    running = True
    while running:
        screen.fill((0, 0, 0))

        player_x_change = 0
        player_y_change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # arrow keystrokes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -0.2
                if event.key == pygame.K_RIGHT:
                    player_x_change = 0.2
                if event.key == pygame.K_UP:
                    player_y_change = -0.2
                if event.key == pygame.K_DOWN:
                    player_y_change = 0.2
                if event.key == pygame.K_SPACE:
                    player.fire()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_y_change = 0
        player.move(player_x_change, player_y_change, 0, 736, 375, 436)

        # UP TO HERE

        for i in range(num_enemies):

            # game over
            if enemyY[i] > 440:
                for j in range(num_enemies):
                    enemyY[j] = 2000
                game_over()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] < 0:
                enemyX_change[i] = 0.2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] > 736:
                enemyX_change[i] = -0.2
                enemyY[i] += enemyY_change[i]

            # collision
            enemyRect = pygame.rect.Rect(enemyX[i] + 8, enemyY[i] + 8, 48, 48)
            bulletRect = pygame.rect.Rect(bulletX + 28, bulletY, 8, 32)
            collision = enemyRect.colliderect(bulletRect)
            if collision:
                bulletY = 480
                bulletState = "ready"
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)
                score_value += 1

            enemy(enemyX[i], enemyY[i], i)

        # bullet movement
        if bulletY < 0:
            bulletY = 480
            bulletState = "ready"
        if bulletState == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score()
        pygame.display.update()
