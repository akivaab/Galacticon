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


def player():
    screen.blit(playerImg, (playerX, playerY))


# game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
