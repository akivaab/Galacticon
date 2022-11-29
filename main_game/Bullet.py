import pygame


class Bullet:
    def __init__(self, x, y, image, speed_v, speed_h=0):
        self.x = x
        self.y = y
        self.image = image
        self.speed_v = speed_v
        self.speed_h = speed_h
        self.mask = pygame.mask.from_surface(self.image)

    # Display the bullet on the screen
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # Move the bullet vertically
    def move_vertical(self):
        self.y += self.speed_v

    # Move the bullet horizontally
    def move_horizontal(self):
        self.x += self.speed_h
