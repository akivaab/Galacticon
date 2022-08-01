import pygame
from Bullet import *


class Player:
    def __init__(self):
        original_player_img = pygame.image.load("assets/player.png").convert()
        original_player_img.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(original_player_img, (54, 54))
        self.x = 370
        self.y = 480
        self.lives = 3
        self.num_turrets = 1
        bullet1 = pygame.image.load("assets/bullet1.png").convert()
        bullet1.set_colorkey((0, 0, 0))
        bullet2 = pygame.image.load("assets/bullet2.png").convert()
        bullet2.set_colorkey((0, 0, 0))
        bullet3 = pygame.image.load("assets/bullet3.png").convert()
        bullet3.set_colorkey((0, 0, 0))
        self.bullet_types = [bullet1, bullet2, bullet3]
        self.bullet_speeds = [5, 6.5, 5.5]
        self.bullets_fired = []
        self.hit_box = pygame.rect.Rect(self.x, self.y + 8, 64, 48)

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, x_change, y_change, x_lower_limit=0, x_upper_limit=746, y_lower_limit=350, y_upper_limit=500):
        new_x = self.x + x_change
        new_y = self.y + y_change
        if x_lower_limit <= new_x <= x_upper_limit:
            self.x = new_x
        if y_lower_limit <= new_y <= y_upper_limit:
            self.y = new_y
        self.hit_box.update(self.x, self.y, 64, 48)

    def fire(self):
        if len(self.bullets_fired) < 3:
            bullet_type = self.bullet_types[self.num_turrets - 1]
            bullet_speed = self.bullet_speeds[self.num_turrets - 1]
            self.bullets_fired.append(Bullet(self.x + 11, self.y - 15, bullet_type, -bullet_speed))

    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move()

    def lose_life(self):
        self.y = 2000
        self.hit_box.update(0, self.y, 0, 0)
        self.lives -= 1

    def recenter(self):
        self.x = 370
        self.y = 480
        self.num_turrets = 1
        self.hit_box.update(self.x, self.y + 8, 64, 48)
