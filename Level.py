from Enemies.BossEnemy import BossEnemy
from Enemies.ClassicEnemy import ClassicEnemy
from Enemies.FranticEnemy import FranticEnemy
from Enemies.SideswiperEnemy import SideswiperEnemy
from Enemies.Gyga import Gyga


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
    def enemy_setup_classic_rows(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [ClassicEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [ClassicEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line3 = [ClassicEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        return [line1, line2, line3]

    # In each row, enemies alternate columns
    @staticmethod
    def enemy_setup_classic_alt(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [ClassicEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [ClassicEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(70, 726, 95)]
        line3 = [ClassicEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        return [line1, line2, line3]

    # Two condensed rows of enemies with a boss on top
    @staticmethod
    def enemy_setup_classic_boss(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [BossEnemy(num_hits=3, ship_speed=2.5, bullet_speed=4, fire_freq=225)]
        line2 = [ClassicEnemy(x, 85, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        line3 = [ClassicEnemy(x, 160, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        return [line1, line2, line3]

    # Enemies are aligned in straight columns, plus there is a sideswiper
    @staticmethod
    def enemy_setup_classic_rows_sw(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
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
    def enemy_setup_classic_alt_sw(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [ClassicEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [ClassicEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(70, 726, 95)]
        line3 = [ClassicEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        sideswiper = [SideswiperEnemy(2, 4)]
        return [line1, line2, line3, sideswiper]

    # Two condensed rows of enemies with a boss on top, plus there is a sideswiper
    @staticmethod
    def enemy_setup_classic_boss_sw(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [BossEnemy(num_hits=3, ship_speed=3, bullet_speed=4.5, fire_freq=225)]
        line2 = [ClassicEnemy(x, 85, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        line3 = [ClassicEnemy(x, 160, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        sideswiper = [SideswiperEnemy(2, 4)]
        return [line1, line2, line3, sideswiper]

    # Enemies are aligned in straight columns, and will go frantic
    @staticmethod
    def enemy_setup_frantic_rows(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [FranticEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [FranticEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line3 = [FranticEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        return [line1, line2, line3]

    # In each row, enemies alternate columns, and will go frantic
    @staticmethod
    def enemy_setup_frantic_alt(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [FranticEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [FranticEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(70, 726, 95)]
        line3 = [FranticEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        return [line1, line2, line3]

    # Two condensed rows of enemies with a boss on top, and will go frantic
    @staticmethod
    def enemy_setup_frantic_boss(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [BossEnemy(num_hits=5, ship_speed=4, bullet_speed=5.5, fire_freq=200)]
        line2 = [FranticEnemy(x, 85, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        line3 = [FranticEnemy(x, 160, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        return [line1, line2, line3]

    # Enemies are aligned in straight columns, and will go frantic, plus there is a sideswiper
    @staticmethod
    def enemy_setup_frantic_rows_sw(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [FranticEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [FranticEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line3 = [FranticEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        sideswiper = [SideswiperEnemy(3, 5.5)]
        return [line1, line2, line3, sideswiper]

    # In each row, enemies alternate columns, and will go frantic, plus there is a sideswiper
    @staticmethod
    def enemy_setup_frantic_alt_sw(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [FranticEnemy(x, 20, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        line2 = [FranticEnemy(x, 100, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(70, 726, 95)]
        line3 = [FranticEnemy(x, 180, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(15, 736, 95)]
        sideswiper = [SideswiperEnemy(3, 5.5)]
        return [line1, line2, line3, sideswiper]

    # Two condensed rows of enemies with a boss on top, and will go frantic, plus there is a sideswiper
    @staticmethod
    def enemy_setup_frantic_boss_sw(enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq):
        line1 = [BossEnemy(num_hits=5, ship_speed=4.5, bullet_speed=6, fire_freq=200)]
        line2 = [FranticEnemy(x, 85, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        line3 = [FranticEnemy(x, 160, enemy_img, bullet_img, ship_speed, bullet_speed, fire_freq) for x in
                 range(45, 690, 60)]
        sideswiper = [SideswiperEnemy(3, 5.5)]
        return [line1, line2, line3, sideswiper]

    @staticmethod
    def enemy_setup_gyga():
        return [[Gyga()]]
