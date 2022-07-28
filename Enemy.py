import pygame
import random
from Bullet import *


class Enemy:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.bullets_fired = []

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, x_change, y_change):
        self.x = x_change
        self.y = y_change

    def random_fire(self):
        if random.random() > 0.5:
            bullet_img = pygame.image.load("assets/enemy_bullet.png").convert()
            self.bullets_fired.append(Bullet(self.x + 16, self.y + 32, bullet_img, 0.4))

    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move()
