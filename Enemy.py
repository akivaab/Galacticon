import random
from Bullet import *


class Enemy:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.bullets_fired = []
        self.mask = pygame.mask.from_surface(self.image)
        self.box = self.mask.get_rect().move(self.x, self.y)
        self.movement_area = pygame.rect.Rect(self.x, self.y, 90, 90)
        self.movement_stage = 0

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        new_box = self.box.move(dx[self.movement_stage], dy[self.movement_stage])
        if not self.movement_area.contains(new_box):
            self.movement_stage = (self.movement_stage + 1) % 4
            new_box = self.box.move(dx[self.movement_stage], dy[self.movement_stage])
        self.x += dx[self.movement_stage]
        self.y += dy[self.movement_stage]
        self.box = new_box

    def random_fire(self):
        if random.randint(0, 375) == 42:
            bullet_img = pygame.image.load("assets/enemy_bullet.png").convert()
            bullet_img.set_colorkey((0, 0, 0))
            bullet_img = pygame.transform.scale(bullet_img, (40, 40))
            self.bullets_fired.append(Bullet(self.x + 16, self.y + 32, bullet_img, 2))

    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move()

    def explode(self):
        self.y = 2000
