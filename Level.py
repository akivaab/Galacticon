from Enemies.BossEnemy import BossEnemy
from Enemies.ClassicEnemy import ClassicEnemy
from Enemies.FranticEnemy import FranticEnemy
from Enemies.SideswiperEnemy import SideswiperEnemy


class Level:
    def __init__(self, enemy_setup):
        self.enemy_setup = enemy_setup

    # Get the level's enemy setup (list of lists)
    def get_enemy_setup(self):
        return self.enemy_setup

    # get the number of enemies defeated so far
    def get_num_enemies_defeated(self):
        num_enemies_defeated = 0
        for enemy_line in self.enemy_setup:
            for enemy in enemy_line:
                if enemy.alive is False:
                    num_enemies_defeated += 1
        return num_enemies_defeated

    # Check if the level has been completed
    def is_completed(self):
        for enemy_line in self.enemy_setup:
            for enemy in enemy_line:
                if enemy.alive is True:
                    return False
        return True

    # Enemies are aligned in straight columns
    @staticmethod
    def enemy_setup_1(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [ClassicEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [ClassicEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line3 = [ClassicEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        return [line1, line2, line3]

    # In each row, enemies alternate columns
    @staticmethod
    def enemy_setup_2(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [ClassicEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [ClassicEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(70, 726, 95)]
        line3 = [ClassicEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        return [line1, line2, line3]

    # Two condensed rows of enemies with a boss on top
    @staticmethod
    def enemy_setup_3(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [BossEnemy(5)]
        line2 = [ClassicEnemy(x, 85, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        line3 = [ClassicEnemy(x, 160, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        return [line1, line2, line3]

    # Enemies are aligned in straight columns, plus there is a sideswiper
    @staticmethod
    def enemy_setup_4(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [ClassicEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [ClassicEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line3 = [ClassicEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        sideswiper = [SideswiperEnemy(2, 4)]
        return [line1, line2, line3, sideswiper]

    # In each row, enemies alternate columns, plus there is a sideswiper
    @staticmethod
    def enemy_setup_5(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [ClassicEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [ClassicEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(70, 726, 95)]
        line3 = [ClassicEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        sideswiper = [SideswiperEnemy(3, 5)]
        return [line1, line2, line3, sideswiper]

    # Two condensed rows of enemies with a boss on top, plus there is a sideswiper
    @staticmethod
    def enemy_setup_6(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [BossEnemy(10, 5)]
        line2 = [ClassicEnemy(x, 85, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        line3 = [ClassicEnemy(x, 160, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        sideswiper = [SideswiperEnemy(3, 5)]
        return [line1, line2, line3, sideswiper]

    # Enemies are aligned in straight columns, and will go frantic
    @staticmethod
    def enemy_setup_7(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [FranticEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [FranticEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line3 = [FranticEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        return [line1, line2, line3]

    # In each row, enemies alternate columns, and will go frantic
    @staticmethod
    def enemy_setup_8(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [FranticEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [FranticEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(70, 726, 95)]
        line3 = [FranticEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        return [line1, line2, line3]

    # Two condensed rows of enemies with a boss on top, and will go frantic
    @staticmethod
    def enemy_setup_9(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [BossEnemy(5, 4)]
        line2 = [FranticEnemy(x, 85, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        line3 = [FranticEnemy(x, 160, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        return [line1, line2, line3]
