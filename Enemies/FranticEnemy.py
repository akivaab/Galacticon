import datetime
from Enemies.ClassicEnemy import *


class FranticEnemy(ClassicEnemy):
    def __init__(self, x, y, image, bullet_image, ship_speed=1, bullet_speed=2, fire_freq=375):
        super().__init__(x, y, image, bullet_image, ship_speed, bullet_speed, fire_freq)
        self.is_frantic = False
        self.pattern_shift_time = datetime.datetime.now()
        self.x_direction = 1 if random.random() < 0.5 else -1
        self.y_direction = 1 if random.random() < 0.5 else -1

    # Move the enemy around a track or randomly
    def move(self):
        if not self.is_frantic:
            super().move()
        else:
            if datetime.datetime.now() >= self.pattern_shift_time:
                self.pattern_shift_time = datetime.datetime.now() + datetime.timedelta(seconds=0.3)
                self.x_direction = 1 if random.random() < 0.5 else -1
                self.y_direction = 1 if random.random() < 0.5 else -1
            x_move_distance = self.x_direction * self.ship_speed
            y_move_distance = self.y_direction * self.ship_speed
            if not 0 <= self.x + x_move_distance <= 736:
                self.x_direction = -self.x_direction
                x_move_distance = -x_move_distance
            if not 0 <= self.y + y_move_distance <= 200:
                self.y_direction = -self.y_direction
                y_move_distance = -y_move_distance
            self.x += x_move_distance
            self.y += y_move_distance
