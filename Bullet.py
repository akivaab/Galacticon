import pygame


class Bullet:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.hit_box = pygame.rect.Rect(self.x + 28, self.y, 8, 32)

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += self.speed
        self.hit_box.move_ip(0, self.speed)
