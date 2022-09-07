from Enemies.BossEnemy import *


class Gyga(BossEnemy):
    def __init__(self):
        gyga_img = pygame.image.load("assets/enemies/gyga.png").convert()
        gyga_img.set_colorkey((0, 0, 0))
        super().__init__(num_hits=90, x=272, y=10, boss_img=gyga_img, ship_speed=4, bullet_speed=7, fire_freq=100)
        self.score_value = 5000

        tracker_img = pygame.image.load("assets/ammo/gyga_tracker.png").convert()
        tracker_img.set_colorkey((0, 0, 0))
        self.tracker_image = tracker_img
        laser_img = pygame.image.load("assets/ammo/gyga_bullet.png").convert()
        laser_img.set_colorkey((0, 0, 0))
        self.laser_image = laser_img

    # Fire at random (gotta figure this out)
    def random_fire(self):
        if random.randint(0, self.fire_freq) == 42:
            self.bullets_fired.append(Bullet(self.x - 14, self.y + 32, self.bullet_image, self.bullet_speed, horiz_speed))
            self.bullets_fired.append(Bullet(self.x + 5, self.y + 32, self.bullet_image, self.bullet_speed, horiz_speed))
            self.bullets_fired.append(Bullet(self.x + 24, self.y + 32, self.bullet_image, self.bullet_speed, horiz_speed))

    # Move all the fired bullets (downwards/diagonally)
    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move_vertical()
            bullet.move_horizontal()

    # Remove all bullets that flew offscreen
    def remove_offscreen_bullets(self):
        self.bullets_fired = list(filter(lambda b: b.y < 600 and 0 <= b.x <= 800, self.bullets_fired))
