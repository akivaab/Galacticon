import pygame


class Gyga:
    def __init__(self):
        self.x = 272
        self.y = 0
        img = pygame.image.load("assets/enemies/gyga.png").convert()
        img.set_colorkey((0, 0, 0))
        self.image = img

    # Display the gyga on the screen
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
