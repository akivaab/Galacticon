import pygame


class Bonus:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.speed = 0.5
        self.rect = pygame.mask.from_surface(self.image).get_rect()

    # Display the bonus on the screen
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # Move the bonus vertically
    def move_vertical(self):
        self.y += self.speed
