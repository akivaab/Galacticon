from Enemy import *


class Boss(Enemy):
    def __init__(self, speed, num_hits):
        boss_img = pygame.image.load("assets/boss.png").convert()
        boss_img.set_colorkey((0, 0, 0))
        super().__init__(320, 10, boss_img)
        self.speed = speed
        self.num_hits = num_hits

    def move(self):
        if not 0 <= self.x + self.speed <= 736:
            self.speed = -self.speed
        self.x += self.speed

    def random_fire(self):
        if random.randint(0, 250) == 42:
            bullet_img = pygame.image.load("assets/enemy_bullet.png").convert()
            bullet_img.set_colorkey((0, 0, 0))
            bullet_img = pygame.transform.scale(bullet_img, (52, 52))
            self.bullets_fired.append(Bullet(self.x - 14, self.y + 32, bullet_img, 4))
            self.bullets_fired.append(Bullet(self.x + 5, self.y + 32, bullet_img, 4))
            self.bullets_fired.append(Bullet(self.x + 24, self.y + 32, bullet_img, 4))

    def hit(self):
        self.num_hits -= 1
        if self.num_hits == 0:
            super().hit()
