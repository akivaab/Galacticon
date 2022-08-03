import random
from Bullet import *


class Enemy:
    def __init__(self, x, y, image, level_grouping):
        self.x = x
        self.y = y
        self.image = image
        self.bullets_fired = []
        self.alive = True
        self.mask = pygame.mask.from_surface(self.image)
        self.box = self.mask.get_rect().move(self.x, self.y)
        self.movement_area = pygame.rect.Rect(self.x, self.y, 90, 90)
        self.movement_stage = 0
        self.level_grouping = level_grouping

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        difficulty_increment = self.level_grouping / 5
        dx = [0, difficulty_increment + 1, 0, -(difficulty_increment + 1)]
        dy = [difficulty_increment + 1, 0, -(difficulty_increment + 1), 0]
        new_box = self.box.move(dx[self.movement_stage], dy[self.movement_stage])
        if not self.movement_area.contains(new_box):
            self.movement_stage = (self.movement_stage + 1) % 4
            new_box = self.box.move(dx[self.movement_stage], dy[self.movement_stage])
        self.x += dx[self.movement_stage]
        self.y += dy[self.movement_stage]
        self.box = new_box

    def random_fire(self):
        if random.randint(0, 375 - (25 * self.level_grouping)) == 42:
            bullet_img = pygame.image.load("assets/enemy_bullet.png").convert()
            bullet_img.set_colorkey((0, 0, 0))
            bullet_img = pygame.transform.scale(bullet_img, (40, 40))
            self.bullets_fired.append(Bullet(self.x + 16, self.y + 32, bullet_img, 2 + (self.level_grouping / 5)))

    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move()

    def hit(self):
        self.y = 2000
        self.alive = False
