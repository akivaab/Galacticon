import pygame
from Bullet import *


class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/player.png").convert()
        self.x = 370
        self.y = 480
        self.lives = 3
        self.num_turrets = 1
        bullet1 = pygame.image.load("assets/bullet1.png").convert()
        bullet2 = pygame.image.load("assets/bullet2.png").convert()
        bullet3 = pygame.image.load("assets/bullet3.png").convert()
        self.bullet_types = [bullet1, bullet2, bullet3]
        self.bullet_speeds = [0.35, 0.5, 0.4]
        self.bullets_fired = []

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, x_change, y_change):
        self.x = x_change
        self.y = y_change

    def fire(self):
        if self.bullets_fired.count() <= 3:
            bullet_type = self.bullet_types[self.num_turrets]
            bullet_speed = self.bullet_speeds[self.num_turrets]
            self.bullets_fired.append(Bullet(self.x + 16, self.y + 10, bullet_type, bullet_speed))

    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move()
