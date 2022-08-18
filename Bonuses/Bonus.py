import pygame


class Bonus:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)

    # Display the bonus on the screen
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # Move the bonus vertically
    def move_vertical(self):
        self.y += self.speed
