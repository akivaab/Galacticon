import pygame

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
enemyX = 370
enemyY = 100
enemyX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
