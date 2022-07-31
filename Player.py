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
        self.bullet_speeds = [3.5, 5, 4]
        self.bullets_fired = []
        self.hit_box = pygame.rect.Rect(self.x, self.y + 8, 64, 48)

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, x_change, y_change, x_lower_limit=0, x_upper_limit=736, y_lower_limit=375, y_upper_limit=436):
        new_x = self.x + x_change
        new_y = self.y + y_change
        if x_lower_limit <= new_x <= x_upper_limit:
            self.x = new_x
        if y_lower_limit <= new_y <= y_upper_limit:
            self.y = new_y
        self.hit_box.update(self.x, self.y, 64, 48)

    def fire(self):
        if len(self.bullets_fired) <= 3:
            bullet_type = self.bullet_types[self.num_turrets]
            bullet_speed = self.bullet_speeds[self.num_turrets]
            self.bullets_fired.append(Bullet(self.x + 16, self.y + 10, bullet_type, bullet_speed))

    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move()
