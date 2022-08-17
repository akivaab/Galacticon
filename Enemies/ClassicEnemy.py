import random
from Enemies.Enemy import *
from Bullet import Bullet


class ClassicEnemy(Enemy):
    def __init__(self, x, y, image, ship_speed=1, bullet_speed=2, fire_freq=375):
        super().__init__(x, y, image, ship_speed, bullet_speed, fire_freq)
        self.box = self.mask.get_rect().move(self.x, self.y)
        self.movement_area = pygame.rect.Rect(self.x, self.y, 90, 90)
        self.movement_stage = 0
        self.score_value = 100

    # Move the enemy around a track (a rectangle perimeter)
    def move(self):
        if self.alive:
            dx = [0, self.ship_speed, 0, -self.ship_speed]
            dy = [self.ship_speed, 0, -self.ship_speed, 0]
            new_box = self.box.move(dx[self.movement_stage], dy[self.movement_stage])
            if not self.movement_area.contains(new_box):
                self.movement_stage = (self.movement_stage + 1) % 4
                new_box = self.box.move(dx[self.movement_stage], dy[self.movement_stage])
            self.x += dx[self.movement_stage]
            self.y += dy[self.movement_stage]
            self.box = new_box

    # Fire a bullet at random
    def random_fire(self):
        if random.randint(0, self.fire_freq) == 42:
            bullet_img = pygame.image.load("assets/enemy_bullet.png").convert()
            bullet_img.set_colorkey((0, 0, 0))
            bullet_img = pygame.transform.scale(bullet_img, (40, 40))
            self.bullets_fired.append(Bullet(self.x + 16, self.y + 32, bullet_img, self.bullet_speed))
