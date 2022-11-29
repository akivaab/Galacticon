import pygame
import random
import csv
from math import inf, floor
from Level import Level
from Bonuses.Plus import Plus
from Bonuses.Heart import Heart
from Bonuses.Two import Two
from Bonuses.Three import Three
from Enemies.Splicer import Splicer

ARCADE_FONT = 'assets/misc/PressStart2P-vaV7.ttf'


class Game:
    def __init__(self):
        self.current_level_num = 1
        enemy_images = []
        for i in range(1, 9):
            enemy_img = pygame.image.load("assets/enemies/enemy" + str(i) + ".png").convert()
            enemy_img.set_colorkey((0, 0, 0))
            enemy_images.append(pygame.transform.scale(enemy_img, (54, 54)))

        bullet1_image = pygame.image.load("assets/ammo/enemy_bullet1.png").convert()
        bullet1_image.set_colorkey((0, 0, 0))
        bullet1_image = pygame.transform.scale(bullet1_image, (40, 40))
        bullet2_image = pygame.image.load("assets/ammo/enemy_bullet2.png").convert()
        bullet2_image.set_colorkey((0, 0, 0))

        self.levels = [
            Level(Level.enemy_setup_classic_rows(enemy_images[0], bullet1_image, ship_speed=1, bullet_speed=2.25,
                                                 fire_freq=350)),
            Level(Level.enemy_setup_classic_alt(enemy_images[0], bullet1_image, ship_speed=1, bullet_speed=2.25,
                                                fire_freq=350)),
            Level(Level.enemy_setup_classic_boss(enemy_images[0], bullet1_image, ship_speed=1, bullet_speed=2.25,
                                                 fire_freq=350)),
            Level(Level.enemy_setup_classic_rows_sw(enemy_images[1], bullet1_image, ship_speed=1.2, bullet_speed=2.5,
                                                    fire_freq=325)),
            Level(Level.enemy_setup_classic_alt_sw(enemy_images[1], bullet1_image, ship_speed=1.2, bullet_speed=2.5,
                                                   fire_freq=325)),
            Level(Level.enemy_setup_classic_boss_sw(enemy_images[1], bullet1_image, ship_speed=1.2, bullet_speed=2.5,
                                                    fire_freq=325)),
            Level(Level.enemy_setup_frantic_rows(enemy_images[2], bullet1_image, ship_speed=1.4, bullet_speed=2.75,
                                                 fire_freq=300)),
            Level(Level.enemy_setup_frantic_alt(enemy_images[2], bullet1_image, ship_speed=1.4, bullet_speed=2.75,
                                                fire_freq=300)),
            Level(Level.enemy_setup_frantic_boss(enemy_images[2], bullet1_image, ship_speed=1.4, bullet_speed=2.75,
                                                 fire_freq=300)),
            Level(Level.enemy_setup_frantic_rows_sw(enemy_images[3], bullet1_image, ship_speed=1.6, bullet_speed=3,
                                                    fire_freq=275)),
            Level(Level.enemy_setup_frantic_alt_sw(enemy_images[3], bullet1_image, ship_speed=1.6, bullet_speed=3,
                                                   fire_freq=275)),
            Level(Level.enemy_setup_frantic_boss_sw(enemy_images[3], bullet1_image, ship_speed=1.6, bullet_speed=3,
                                                    fire_freq=275)),
            Level(Level.enemy_setup_classic_rows(enemy_images[4], bullet2_image, ship_speed=1.8, bullet_speed=3.25,
                                                 fire_freq=250)),
            Level(Level.enemy_setup_classic_alt(enemy_images[4], bullet2_image, ship_speed=1.8, bullet_speed=3.25,
                                                fire_freq=250)),
            Level(Level.enemy_setup_classic_boss(enemy_images[4], bullet2_image, ship_speed=1.8, bullet_speed=3.25,
                                                 fire_freq=250)),
            Level(Level.enemy_setup_classic_rows_sw(enemy_images[5], bullet2_image, ship_speed=2, bullet_speed=3.5,
                                                    fire_freq=225)),
            Level(Level.enemy_setup_classic_alt_sw(enemy_images[5], bullet2_image, ship_speed=2, bullet_speed=3.5,
                                                   fire_freq=225)),
            Level(Level.enemy_setup_classic_boss_sw(enemy_images[5], bullet2_image, ship_speed=2, bullet_speed=3.5,
                                                    fire_freq=225)),
            Level(Level.enemy_setup_frantic_rows(enemy_images[6], bullet2_image, ship_speed=2.2, bullet_speed=3.75,
                                                 fire_freq=200)),
            Level(Level.enemy_setup_frantic_alt(enemy_images[6], bullet2_image, ship_speed=2.2, bullet_speed=3.75,
                                                fire_freq=200)),
            Level(Level.enemy_setup_frantic_boss(enemy_images[6], bullet2_image, ship_speed=2.2, bullet_speed=3.75,
                                                 fire_freq=200)),
            Level(Level.enemy_setup_frantic_rows_sw(enemy_images[7], bullet2_image, ship_speed=2.4, bullet_speed=4,
                                                    fire_freq=175)),
            Level(Level.enemy_setup_frantic_alt_sw(enemy_images[7], bullet2_image, ship_speed=2.4, bullet_speed=4,
                                                   fire_freq=175)),
            Level(Level.enemy_setup_frantic_boss_sw(enemy_images[7], bullet2_image, ship_speed=2.4, bullet_speed=4,
                                                    fire_freq=175)),
            Level(Level.enemy_setup_gyga())
        ]
        self.current_score = 0
        self.bonuses_dropped = []
        self.splicer = Splicer()
        self.splicer_deployed = False
        self.is_muted = False

    # Get the current level
    def get_cur_level(self):
        return self.levels[self.current_level_num - 1]

    # Get the enemy setup of the current level
    def get_cur_enemy_setup(self):
        return self.levels[self.current_level_num - 1].get_enemy_setup()

    # Drop bonuses at random
    def random_bonus_drop(self):
        game_stage = floor(self.current_level_num / 5)
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
        remove_bonus_indexes = []
        for i in range(len(self.bonuses_dropped)):
            bonus = self.bonuses_dropped[i]
            dx = bonus.x - player.x
            dy = bonus.y - player.y
            if player.mask.overlap(bonus.mask, (dx, dy)) is not None:
                remove_bonus_indexes.append(i)
                bonus_score = 0
                if isinstance(bonus, Plus):
                    bonus_score = 2000
                elif isinstance(bonus, Heart):
                    player.add_life()
                    bonus_score = 250
                elif isinstance(bonus, Two):
                    player.num_turrets = 2
                    bonus_score = 250
                elif isinstance(bonus, Three):
                    player.num_turrets = 3
                    bonus_score = 250
                self.increase_score(bonus_score)
        for i in remove_bonus_indexes:
            self.bonuses_dropped.pop(i)

    # Randomly deploy the splicer
    def random_splicer_deployment(self, player_x):
        if 13 <= self.current_level_num <= 24 and not self.splicer_deployed:
            self.splicer_deployed = True if random.randint(0, 1250) == 27 else False
        elif self.splicer_deployed:
            deployment_complete = self.splicer.perform_action(player_x)
            self.splicer_deployed = not deployment_complete

    # Return if the current level has been completed
    def is_current_level_completed(self):
        return self.levels[self.current_level_num - 1].is_completed()

    # Move on to the next level
    def go_to_next_level(self, screen):
        self.current_level_num += 1
        display_text(screen, "Level " + str(self.current_level_num), 32, (255, 255, 255), (285, 280))

    # Return if the game has been completed
    def is_completed(self):
        return self.current_level_num == len(self.levels) and self.is_current_level_completed()

    # Adjust the score
    def increase_score(self, value):
        self.current_score += value

    # Display the lives, level, and score on the screen
    def display_data(self, screen, num_lives):
        display_text(screen, "Lives:" + str(num_lives), 12, (255, 255, 255), (0, 588))
        display_text(screen, "Level:" + str(self.current_level_num), 12, (255, 255, 255), (100, 588))
        display_text(screen, "Score:" + str(self.current_score), 12, (255, 255, 255), (210, 588))

    # Display a message after the player dies
    @staticmethod
    def resuscitation_message(screen):
        display_text(screen, "Get Ready To Continue", 24, (255, 255, 255), (150, 280))

    # Display a message when the player loses
    @staticmethod
    def game_over_message(screen):
        display_text(screen, "GAME OVER", 64, (255, 255, 255), (110, 250))

    # Display a message when the player wins
    @staticmethod
    def game_completed_message(screen):
        display_text(screen, "YOU WIN!!", 64, (255, 255, 255), (110, 250))

    # Get some number of the top scores from the scoreboard
    @staticmethod
    def read_scoreboard(num_records=inf):
        rows = []
        with open("scoreboard.csv", 'r') as scoreboard:
            csv_reader = csv.reader(scoreboard)
            for row in csv_reader:
                if csv_reader.line_num > num_records:
                    break
                rows.append(row)
        return rows

    # Add a new high score to the scoreboard
    def write_scoreboard(self, name):
        scores = Game.read_scoreboard()
        new_score = [name, self.current_score]
        scores.append(new_score)
        scores.sort(key=lambda x: int(x[1]), reverse=True)
        with open("scoreboard.csv", 'w', newline='') as scoreboard:
            csv_writer = csv.writer(scoreboard)
            csv_writer.writerows(scores)
        return new_score

    # Mute the game
    def mute(self, screen):
        self.is_muted = not self.is_muted
        pygame.mixer.music.set_volume(0.9921875 - pygame.mixer.music.get_volume())
        if self.is_muted:
            mute_image = pygame.image.load("assets/misc/muted_speaker.png").convert()
            mute_image.set_colorkey((0, 0, 0))
            screen.blit(mute_image, (765, 565))
            pygame.display.set_caption("The world has gone silent! Oh wait, there's still laser sounds.")
        else:
            pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect(765, 565, 32, 32))
            pygame.display.set_caption("Galacticon")
        pygame.display.update(pygame.rect.Rect(765, 565, 32, 32))


# display text onto a given screen
def display_text(screen, text, font_size, text_color, text_coordinates):
    font = pygame.font.Font(ARCADE_FONT, font_size)
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, text_coordinates)
