from Level import *
from Boss import *
from ClassicEnemy import *


class Game:
    def __init__(self):
        self.enemy_images = []
        for i in range(1, 7):
            enemy_img = pygame.image.load("assets/enemy" + str(i) + ".png").convert()
            enemy_img.set_colorkey((0, 0, 0))
            self.enemy_images.append(pygame.transform.scale(enemy_img, (54, 54)))
        self.enemy_setups = [Game.enemy_setup_1, Game.enemy_setup_2, Game.enemy_setup_3]
        self.current_level = 1
        self.levels = []
        for i in range(1, 19):
            enemy_img = self.enemy_images[int((i - 1) / 3)]
            enemy_setup_function = self.enemy_setups[(i - 1) % 3]
            self.levels.append(Level(enemy_img, enemy_setup_function(enemy_img)))

    def get_cur_enemy_setup(self):
        return self.levels[self.current_level - 1].get_enemy_setup()
        # enemy_img = self.enemy_images[int((level_num - 1) / 3)]
        # enemy_setup_function = self.enemy_setups[(level_num - 1) % 3]
        # return enemy_setup_function(enemy_img, int((level_num - 1) / 3))

    def go_to_next_level(self):
        self.current_level += 1

    @staticmethod
    def enemy_setup_1(enemy_img):
        line1 = [ClassicEnemy(x, 20, enemy_img) for x in range(15, 736, 95)]
        line2 = [ClassicEnemy(x, 100, enemy_img) for x in range(15, 736, 95)]
        line3 = [ClassicEnemy(x, 180, enemy_img) for x in range(15, 736, 95)]
        return [line1, line2, line3]

    @staticmethod
    def enemy_setup_2(enemy_img):
        line1 = [ClassicEnemy(x, 20, enemy_img) for x in range(15, 736, 95)]
        line2 = [ClassicEnemy(x, 100, enemy_img) for x in range(70, 726, 95)]
        line3 = [ClassicEnemy(x, 180, enemy_img) for x in range(15, 736, 95)]
        return [line1, line2, line3]

    @staticmethod
    def enemy_setup_3(enemy_img):
        line1 = [Boss(3)]
        line2 = [ClassicEnemy(x, 85, enemy_img) for x in range(45, 690, 60)]
        line3 = [ClassicEnemy(x, 160, enemy_img) for x in range(45, 690, 60)]
        return [line1, line2, line3]
