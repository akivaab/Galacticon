import random
from Bullet import *
from Enemy import *


class SideswiperEnemy(Enemy):
    def __init__(self, num_hits, ship_speed=3, bullet_speed=5, fire_freq=200):
        swiper_img = pygame.image.load("assets/sideswiper.png").convert()
        swiper_img.set_colorkey((0, 0, 0))
        swiper_img = pygame.transform.scale(swiper_img, (48, 48))
        swiper_img = pygame.transform.rotate(swiper_img, 90)
        super().__init__(1000, 500, swiper_img, ship_speed, bullet_speed, fire_freq)
        self.direction = 1
        self.num_hits = num_hits
        self.score_value = 1000

    def move(self):
        if self.alive:
            move_distance = self.direction * self.ship_speed
            if not -500 <= self.x + move_distance <= 1500:
                self.image = pygame.transform.flip(self.image, True, False)
                self.y = random.randint(350, 500)
                self.direction = -self.direction
                move_distance = -move_distance
                self.bullet_speed = -self.bullet_speed
            self.x += move_distance
            self.y += move_distance / 20

    def random_fire(self):
        if random.randint(0, self.fire_freq) == 42:
            bullet_img = pygame.image.load("assets/sideswiper_bullet.png").convert()
            bullet_img.set_colorkey((0, 0, 0))
            bullet_img = pygame.transform.scale(bullet_img, (44, 44))
            self.bullets_fired.append(Bullet(self.x, self.y, bullet_img, self.bullet_speed))

    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move_horizontal()

    def hit(self):
        pygame.mixer.Sound("assets/explosion.wav").play()
        self.num_hits -= 1
        if self.num_hits == 0:
            super().hit()

    def move_offscreen(self):
        self.x = 1000
