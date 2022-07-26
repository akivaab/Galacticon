import pygame
import random

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# screen window caption and icon
pygame.display.set_caption("Galacticon")
icon = pygame.image.load("assets/logo.png")
pygame.display.set_icon(icon)

# init player
playerImg = pygame.image.load("assets/player.png")
playerX = 370
playerY = 480
playerX_change = 0

# init enemy
enemyImg = pygame.image.load("assets/enemy1.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 40

# init bullet
bulletImg = pygame.image.load("assets/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bulletState = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # arrow keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX < 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX > 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    # bullet movement
    if bulletState == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
