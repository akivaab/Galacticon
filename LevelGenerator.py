from Enemy import *


class LevelGenerator:
    def __init__(self):
        self.enemy_images = []
        for i in range(3):           # SHOULD BE HIGHER, ADD MORE PNGs
            enemy_img = pygame.image.load("assets/enemy" + str(int(i / 3) + 1) + ".png").convert()
            enemy_img.set_colorkey((0, 0, 0))
            self.enemy_images.append(pygame.transform.scale(enemy_img, (54, 54)))
        self.enemy_setups = [LevelGenerator.enemy_setup_1, LevelGenerator.enemy_setup_2, LevelGenerator.enemy_setup_3]

    @staticmethod
    def enemy_setup_1(enemy_img):
        line1 = [Enemy(x, 20, enemy_img) for x in range(10, 736, 100)]
        line2 = [Enemy(x, 100, enemy_img) for x in range(10, 736, 100)]
        line3 = [Enemy(x, 180, enemy_img) for x in range(10, 736, 100)]
        return [line1, line2, line3]

    @staticmethod
    def enemy_setup_2(enemy_img):
        line1 = [Enemy(x, 20, enemy_img) for x in range(10, 736, 100)]
        line2 = [Enemy(x, 100, enemy_img) for x in range(64, 736, 100)]
        line3 = [Enemy(x, 180, enemy_img) for x in range(10, 736, 100)]
        return [line1, line2, line3]

    @staticmethod
    def enemy_setup_3(enemy_img):
        # add some boss_line here #
        line1 = [Enemy(x, 20, enemy_img) for x in range(10, 736, 100)]
        line2 = [Enemy(x, 85, enemy_img) for x in range(10, 736, 100)]
        line3 = [Enemy(x, 160, enemy_img) for x in range(10, 736, 100)]
        return [line1, line2, line3]

    def generate_enemy_setup(self, level_num):
        enemy_img = self.enemy_images[(level_num - 1) % 3]
        enemy_setup_function = self.enemy_setups[(level_num - 1) % 3]
        return enemy_setup_function(enemy_img)
