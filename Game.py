import pygame
import random
from math import floor
from Level import Level
from Enemies.BossEnemy import BossEnemy
from Enemies.ClassicEnemy import ClassicEnemy
from Enemies.SideswiperEnemy import SideswiperEnemy
from Bonuses.Plus import Plus
from Bonuses.Heart import Heart
from Bonuses.Two import Two
from Bonuses.Three import Three


class Game:
    def __init__(self):
        self.current_level = 1
        enemy_images = []
        for i in range(1, 7):
            enemy_img = pygame.image.load("assets/enemy" + str(i) + ".png").convert()
            enemy_img.set_colorkey((0, 0, 0))
            enemy_images.append(pygame.transform.scale(enemy_img, (54, 54)))
        self.levels = [
            Level(enemy_setup_1(enemy_images[0], ship_speed=1, bullet_speed=2.25, fire_freq=350)),
            Level(enemy_setup_2(enemy_images[0], ship_speed=1, bullet_speed=2.25, fire_freq=350)),
            Level(enemy_setup_3(enemy_images[0], ship_speed=1, bullet_speed=2.25, fire_freq=350)),
            Level(enemy_setup_1(enemy_images[1], ship_speed=1.2, bullet_speed=2.5, fire_freq=325)),
            Level(enemy_setup_2(enemy_images[1], ship_speed=1.2, bullet_speed=2.5, fire_freq=325)),
            Level(enemy_setup_3(enemy_images[1], ship_speed=1.2, bullet_speed=2.5, fire_freq=325)),
            Level(enemy_setup_4(enemy_images[2], ship_speed=1.4, bullet_speed=2.75, fire_freq=300)),
            Level(enemy_setup_2(enemy_images[2], ship_speed=1.4, bullet_speed=2.75, fire_freq=300)),
            Level(enemy_setup_3(enemy_images[2], ship_speed=1.4, bullet_speed=2.75, fire_freq=300)),
            Level(enemy_setup_1(enemy_images[3], ship_speed=1.6, bullet_speed=3, fire_freq=275)),
            Level(enemy_setup_2(enemy_images[3], ship_speed=1.6, bullet_speed=3, fire_freq=275)),
            Level(enemy_setup_3(enemy_images[3], ship_speed=1.6, bullet_speed=3, fire_freq=275)),
            Level(enemy_setup_1(enemy_images[4], ship_speed=1.8, bullet_speed=3.25, fire_freq=250)),
            Level(enemy_setup_5(enemy_images[4], ship_speed=1.8, bullet_speed=3.25, fire_freq=250)),
            Level(enemy_setup_6(enemy_images[4], ship_speed=1.8, bullet_speed=3.25, fire_freq=250)),
            Level(enemy_setup_4(enemy_images[5], ship_speed=2, bullet_speed=3.5, fire_freq=225)),
            Level(enemy_setup_2(enemy_images[5], ship_speed=2, bullet_speed=3.5, fire_freq=225)),
            Level(enemy_setup_6(enemy_images[5], ship_speed=2, bullet_speed=3.5, fire_freq=225)),
        ]
        self.current_score = 0
        self.bonuses_dropped = []

    # Get the enemy setup of the current level
    def get_cur_enemy_setup(self):
        return self.levels[self.current_level - 1].get_enemy_setup()

    # Drop bonuses at random
    def random_bonus_drop(self):
        game_stage = floor(self.current_level / 5)
        rand_bonus = random.randint(0, 3000 + (game_stage * 2000))
        if rand_bonus <= min(game_stage, 3):
            bonus_dict = {
                0: Plus(random.randint(0, 736), 0),
                1: Heart(random.randint(0, 736), 0),
                2: Two(random.randint(0, 736), 0),
                3: Three(random.randint(0, 736), 0)
            }
            self.bonuses_dropped.append(bonus_dict[rand_bonus])

    # Move the bonuses down the screen
    def move_bonuses(self):
        for bonus in self.bonuses_dropped:
            bonus.move_vertical()

    # Remove the bonuses that flew offscreen
    def remove_offscreen_bonuses(self):
        self.bonuses_dropped = list(filter(lambda b: b.y < 600, self.bonuses_dropped))

    # Check if the player received a bonus
    def received_bonus(self, player):
        for i in range(len(self.bonuses_dropped)):
            bonus = self.bonuses_dropped[i]
            dx = bonus.x - player.x
            dy = bonus.y - player.y
            if player.mask.overlap(bonus.mask, (dx, dy)) is not None:
                self.bonuses_dropped.pop(i)
                if isinstance(bonus, Plus):
                    self.increase_score(2500)
                elif isinstance(bonus, Heart):
                    player.lives += 1
                elif isinstance(bonus, Two):
                    player.num_turrets = 2
                elif isinstance(bonus, Three):
                    player.num_turrets = 3
                return

    # Return if the current level has been completed
    def is_current_level_completed(self):
        return self.levels[self.current_level - 1].is_completed()

    # Move on to the next level
    def go_to_next_level(self, screen):
        self.current_level += 1
        next_level_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 32)
        next_level_text = next_level_font.render("Level " + str(self.current_level), True, (255, 255, 255))
        screen.blit(next_level_text, (285, 280))

    # Return if the game has been completed
    def is_completed(self):
        return self.current_level == len(self.levels) and self.is_current_level_completed()

    # Adjust the score
    def increase_score(self, value):
        self.current_score += value

    # Display the lives, level, and score on the screen
    def display_data(self, screen, num_lives):
        font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 16)
        lives = font.render("Lives:" + str(num_lives), True, (255, 255, 255))
        level = font.render("Level:" + str(self.current_level), True, (255, 255, 255))
        score = font.render("Score:" + str(self.current_score), True, (255, 255, 255))
        screen.blit(lives, (0, 584))
        screen.blit(level, (150, 584))
        screen.blit(score, (300, 584))

    # Display a message after the player dies
    @staticmethod
    def resuscitation_message(screen):
        get_ready_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 24)
        get_ready_text = get_ready_font.render("Get Ready To Continue", True, (255, 255, 255))
        screen.blit(get_ready_text, (150, 280))

    # Display a message when the player loses
    @staticmethod
    def game_over_message(screen):
        game_over_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 64)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over_text, (110, 250))

    # Display a message when the player wins
    @staticmethod
    def game_completed_message(screen):
        game_completed_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 64)
        game_completed_text = game_completed_font.render("YOU WIN!!", True, (255, 255, 255))
        screen.blit(game_completed_text, (110, 250))


# Enemies are aligned in straight columns
def enemy_setup_1(enemy_img, ship_speed, bullet_speed, fire_freq):
    line1 = [ClassicEnemy(x, 20, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    line2 = [ClassicEnemy(x, 100, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    line3 = [ClassicEnemy(x, 180, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    return [line1, line2, line3]


# In each row, enemies alternate columns
def enemy_setup_2(enemy_img, ship_speed, bullet_speed, fire_freq):
    line1 = [ClassicEnemy(x, 20, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    line2 = [ClassicEnemy(x, 100, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(70, 726, 95)]
    line3 = [ClassicEnemy(x, 180, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    return [line1, line2, line3]


# Two condensed rows of enemies with a boss on top
def enemy_setup_3(enemy_img, ship_speed, bullet_speed, fire_freq):
    line1 = [BossEnemy(5)]
    line2 = [ClassicEnemy(x, 85, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(45, 690, 60)]
    line3 = [ClassicEnemy(x, 160, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(45, 690, 60)]
    return [line1, line2, line3]


# Enemies are aligned in straight columns, plus there is a sideswiper
def enemy_setup_4(enemy_img, ship_speed, bullet_speed, fire_freq):
    line1 = [ClassicEnemy(x, 20, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    line2 = [ClassicEnemy(x, 100, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    line3 = [ClassicEnemy(x, 180, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    sideswiper = [SideswiperEnemy(2, 4)]
    return [line1, line2, line3, sideswiper]


# In each row, enemies alternate columns, plus there is a sideswiper
def enemy_setup_5(enemy_img, ship_speed, bullet_speed, fire_freq):
    line1 = [ClassicEnemy(x, 20, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    line2 = [ClassicEnemy(x, 100, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(70, 726, 95)]
    line3 = [ClassicEnemy(x, 180, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(15, 736, 95)]
    sideswiper = [SideswiperEnemy(3, 5)]
    return [line1, line2, line3, sideswiper]


# Two condensed rows of enemies with a boss on top, plus there is a sideswiper
def enemy_setup_6(enemy_img, ship_speed, bullet_speed, fire_freq):
    line1 = [BossEnemy(10)]
    line2 = [ClassicEnemy(x, 85, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(45, 690, 60)]
    line3 = [ClassicEnemy(x, 160, enemy_img, ship_speed, bullet_speed, fire_freq) for x in range(45, 690, 60)]
    sideswiper = [SideswiperEnemy(3, 5)]
    return [line1, line2, line3, sideswiper]
