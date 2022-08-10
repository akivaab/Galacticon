from Level import *
from Boss import Boss
from ClassicEnemy import ClassicEnemy
from SideswiperEnemy import *


class Game:
    def __init__(self):
        enemy_images = []
        for i in range(1, 7):
            enemy_img = pygame.image.load("assets/enemy" + str(i) + ".png").convert()
            enemy_img.set_colorkey((0, 0, 0))
            enemy_images.append(pygame.transform.scale(enemy_img, (54, 54)))
        self.current_level = 1
        self.levels = [
            Level(enemy_setup_1(enemy_images[0], ship_speed=1, bullet_speed=2, fire_freq=375)),
            Level(enemy_setup_2(enemy_images[0], ship_speed=1, bullet_speed=2, fire_freq=375)),
            Level(enemy_setup_3(enemy_images[0], ship_speed=1, bullet_speed=2, fire_freq=375)),
            Level(enemy_setup_1(enemy_images[1], ship_speed=1.2, bullet_speed=2.25, fire_freq=350)),
            Level(enemy_setup_2(enemy_images[1], ship_speed=1.2, bullet_speed=2.25, fire_freq=350)),
            Level(enemy_setup_3(enemy_images[1], ship_speed=1.2, bullet_speed=2.25, fire_freq=350)),
            Level(enemy_setup_1(enemy_images[2], ship_speed=1.4, bullet_speed=2.5, fire_freq=325)),
            Level(enemy_setup_2(enemy_images[2], ship_speed=1.4, bullet_speed=2.5, fire_freq=325)),
            Level(enemy_setup_3(enemy_images[2], ship_speed=1.4, bullet_speed=2.5, fire_freq=325)),
            Level(enemy_setup_1(enemy_images[3], ship_speed=1.6, bullet_speed=2.75, fire_freq=300)),
            Level(enemy_setup_2(enemy_images[3], ship_speed=1.6, bullet_speed=2.75, fire_freq=300)),
            Level(enemy_setup_3(enemy_images[3], ship_speed=1.6, bullet_speed=2.75, fire_freq=300)),
            Level(enemy_setup_1(enemy_images[4], ship_speed=1.8, bullet_speed=3, fire_freq=275)),
            Level(enemy_setup_2(enemy_images[4], ship_speed=1.8, bullet_speed=3, fire_freq=275)),
            Level(enemy_setup_3(enemy_images[4], ship_speed=1.8, bullet_speed=3, fire_freq=275)),
            Level(enemy_setup_1(enemy_images[5], ship_speed=2, bullet_speed=3.25, fire_freq=250)),
            Level(enemy_setup_2(enemy_images[5], ship_speed=2, bullet_speed=3.25, fire_freq=250)),
            Level(enemy_setup_3(enemy_images[5], ship_speed=2, bullet_speed=3.25, fire_freq=250)),
        ]

    def get_cur_enemy_setup(self):
        return self.levels[self.current_level - 1].get_enemy_setup()

    def go_to_next_level(self):
        self.current_level += 1


# enemies are aligned in straight columns
def enemy_setup_1(enemy_img, ship_speed, bullet_speed, fire_freq):
    line1 = [ClassicEnemy(x, 20, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    line2 = [ClassicEnemy(x, 100, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    line3 = [ClassicEnemy(x, 180, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    return [line1, line2, line3]


# in each row, enemies alternate columns
def enemy_setup_2(enemy_img, ship_speed, bullet_speed, fire_freq):
    line1 = [ClassicEnemy(x, 20, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    line2 = [ClassicEnemy(x, 100, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(70, 726, 95)]
    line3 = [ClassicEnemy(x, 180, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    return [line1, line2, line3]


# two condensed rows of enemies with a boss on top
def enemy_setup_3(enemy_img, ship_speed, bullet_speed, fire_freq):
    line1 = [Boss(3)]
    line2 = [ClassicEnemy(x, 85, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(45, 690, 60)]
    line3 = [ClassicEnemy(x, 160, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(45, 690, 60)]
    return [line1, line2, line3]
