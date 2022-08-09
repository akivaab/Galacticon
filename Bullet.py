import pygame


class Bullet:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move_vertical(self):
        self.y += self.speed

    def move_horizontal(self):
        self.x += self.speed
