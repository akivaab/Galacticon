import pygame
import random
from Bullet import *


class Enemy:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.bullets_fired = []
        self.hit_box = pygame.rect.Rect(self.x + 8, self.y + 8, 48, 48)
        self.movement_area = pygame.rect.Rect(self.x, self.y, 128, 128)
        self.movement_stage = 0

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        dx = [0, 2, 0, -2]
        dy = [2, 0, -2, 0]
        new_hit_box = self.hit_box.move(dx[self.movement_stage], dy[self.movement_stage])
        if not self.movement_area.contains(new_hit_box):
            self.movement_stage = (self.movement_stage + 1) % 4
            new_hit_box = self.hit_box.move(dx[self.movement_stage], dy[self.movement_stage])
        self.hit_box = new_hit_box

    def random_fire(self):
        if random.random() > 0.5:
            bullet_img = pygame.image.load("assets/enemy_bullet.png").convert()
            self.bullets_fired.append(Bullet(self.x + 16, self.y + 32, bullet_img, 4))

    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move()
