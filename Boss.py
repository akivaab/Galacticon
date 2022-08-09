import random
from Enemy import *
from Bullet import *


class Boss(Enemy):
    def __init__(self, num_hits, ship_speed=1.5, bullet_speed=4, fire_freq=250):
        boss_img = pygame.image.load("assets/boss.png").convert()
        boss_img.set_colorkey((0, 0, 0))
        super().__init__(320, 10, boss_img, ship_speed, bullet_speed, fire_freq)
        self.direction = 1
        self.num_hits = num_hits
        self.score_value = 500

    def move(self):
        move_distance = self.direction * self.ship_speed
        if not 0 <= self.x + move_distance <= 736:
            self.direction = -self.direction
            move_distance = -move_distance
        self.x += move_distance

    def random_fire(self):
        if random.randint(0, self.fire_freq) == 42:
            bullet_img = pygame.image.load("assets/enemy_bullet.png").convert()
            bullet_img.set_colorkey((0, 0, 0))
            bullet_img = pygame.transform.scale(bullet_img, (52, 52))
            self.bullets_fired.append(Bullet(self.x - 14, self.y + 32, bullet_img, self.bullet_speed))
            self.bullets_fired.append(Bullet(self.x + 5, self.y + 32, bullet_img, self.bullet_speed))
            self.bullets_fired.append(Bullet(self.x + 24, self.y + 32, bullet_img, self.bullet_speed))

    def hit(self):
        pygame.mixer.Sound("assets/explosion.wav").play()
        self.num_hits -= 1
        if self.num_hits == 0:
            super().hit()
