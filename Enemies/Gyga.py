import datetime
from enum import Enum
from Enemies.BossEnemy import *


class AttackPattern(Enum):
    FIRE_SPREAD = 1
    TRACK_AND_BEAM = 2


class Gyga(BossEnemy):
    def __init__(self):
        gyga_img = pygame.image.load("assets/enemies/gyga.png").convert()
        gyga_img.set_colorkey((0, 0, 0))
        super().__init__(num_hits=90, x=272, y=10, boss_img=gyga_img, ship_speed=4, bullet_speed=6, fire_freq=100)
        self.score_value = 5000

        tracker_img = pygame.image.load("assets/ammo/gyga_tracker.png").convert()
        tracker_img.set_colorkey((0, 0, 0))
        self.tracker_image = tracker_img
        laser_img = pygame.image.load("assets/ammo/gyga_bullet.png").convert()
        laser_img.set_colorkey((0, 0, 0))
        self.laser_image = laser_img

        self.step = 0
        self.attack_pattern = AttackPattern.FIRE_SPREAD
        self.full_attack_timer = None
        self.attack_section_timer = None
        self.is_tracking = False
        self.is_locked = False

    # Display the gyga on the screen
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.is_tracking:
            screen.blit(self.tracker_image, (self.x, self.y + 128))
        elif self.is_locked:
            screen.blit(self.tracker_image, (0, 700))  # offscreen

    def track(self, player_x):
        if self.is_tracking:
            if self.x + 96 - player_x > 0 <= self.x - self.ship_speed <= 544:  # Gyga is to the right of player
                self.x -= self.ship_speed
            elif self.x + 96 - player_x < 0 <= self.x + self.ship_speed <= 544:  # Gyga is to the left of player
                self.x += self.ship_speed
        elif not self.is_locked:
            move_distance = self.direction * self.ship_speed
            if not 0 <= self.x + move_distance <= 544:
                self.direction = -self.direction
                move_distance = -move_distance
            self.x += move_distance

    # Fire at random (gotta figure this out)
    def random_fire(self):
        if self.step == 0:
            if random.randint(0, self.fire_freq) == 42:
                current_time = datetime.datetime.now()
                self.attack_section_timer = current_time
                self.full_attack_timer = current_time
                self.step += 1
        elif self.attack_pattern == AttackPattern.FIRE_SPREAD:
            self.perform_fire_spread()
        elif self.attack_pattern == AttackPattern.TRACK_AND_BEAM:
            self.perform_track_and_beam()

    def perform_fire_spread(self):
        if self.step == 1 and datetime.datetime.now() < self.full_attack_timer + datetime.timedelta(seconds=4):
            if datetime.datetime.now() > self.attack_section_timer + datetime.timedelta(seconds=0.4):
                self.bullets_fired.append(Bullet(self.x - 33, self.y + 32, self.bullet_image, self.bullet_speed, -5))
                self.bullets_fired.append(Bullet(self.x - 14, self.y + 32, self.bullet_image, self.bullet_speed, -2.5))
                self.bullets_fired.append(Bullet(self.x + 5, self.y + 32, self.bullet_image, self.bullet_speed, 0))
                self.bullets_fired.append(Bullet(self.x + 24, self.y + 32, self.bullet_image, self.bullet_speed, 2.5))
                self.bullets_fired.append(Bullet(self.x + 33, self.y + 32, self.bullet_image, self.bullet_speed, 5))
                self.attack_section_timer = datetime.datetime.now()
        else:
            self.step = 0
            self.attack_pattern = AttackPattern.TRACK_AND_BEAM

    def perform_track_and_beam(self):
        if self.step == 1:
            self.is_tracking = True
            if datetime.datetime.now() > self.attack_section_timer + datetime.timedelta(seconds=3.5):
                self.is_tracking = False
                self.attack_section_timer = datetime.datetime.now()
                self.step += 1
        elif self.step == 2:
            self.is_locked = True
            if datetime.datetime.now() > self.attack_section_timer + datetime.timedelta(seconds=0.5):
                self.attack_section_timer = datetime.datetime.now()
                self.step += 1
        elif self.step == 3:
            self.bullets_fired.append(Bullet(self.x - 54, self.y + 148, self.laser_image, self.bullet_speed))
            self.bullets_fired.append(Bullet(self.x - 27, self.y + 148, self.laser_image, self.bullet_speed))
            self.bullets_fired.append(Bullet(self.x, self.y + 148, self.laser_image, self.bullet_speed))
            self.bullets_fired.append(Bullet(self.x + 27, self.y + 148, self.laser_image, self.bullet_speed))
            self.bullets_fired.append(Bullet(self.x + 54, self.y + 148, self.laser_image, self.bullet_speed))
            if datetime.datetime.now() > self.attack_section_timer + datetime.timedelta(seconds=3):
                self.is_locked = False
                self.attack_section_timer = datetime.datetime.now()
                self.step += 1
        else:
            self.step = 0
            self.attack_pattern = AttackPattern.FIRE_SPREAD

    # Move all the fired bullets (downwards/diagonally)
    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move_vertical()
            bullet.move_horizontal()

    # Remove all bullets that flew offscreen
    def remove_offscreen_bullets(self):
        self.bullets_fired = list(filter(lambda b: b.y < 600 and 0 <= b.x <= 800, self.bullets_fired))
