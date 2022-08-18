from Bullet import *
from Enemies.Enemy import Enemy


class Player:
    def __init__(self):
        original_player_img = pygame.image.load("assets/player.png").convert()
        original_player_img.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(original_player_img, (54, 54))
        self.x = 370
        self.y = 480
        self.lives = 3
        self.num_turrets = 1
        bullet1 = pygame.image.load("assets/bullet1.png").convert()
        bullet1.set_colorkey((0, 0, 0))
        bullet2 = pygame.image.load("assets/bullet2.png").convert()
        bullet2.set_colorkey((0, 0, 0))
        bullet3 = pygame.image.load("assets/bullet3.png").convert()
        bullet3.set_colorkey((0, 0, 0))
        self.bullet_types = [bullet1, bullet2, bullet3]
        self.bullet_speeds = [5, 6.5, 5.5]
        self.bullets_fired = []
        self.mask = pygame.mask.from_surface(self.image)

    # Display the player on the screen
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # Move the player along both axes
    def move(self, x_change, y_change, x_lower_limit=0, x_upper_limit=746, y_lower_limit=350, y_upper_limit=500):
        new_x = self.x + x_change
        new_y = self.y + y_change
        if x_lower_limit <= new_x <= x_upper_limit:
            self.x = new_x
        if y_lower_limit <= new_y <= y_upper_limit:
            self.y = new_y

    # Fire a bullet
    def fire(self):
        if len(self.bullets_fired) < 5 * self.num_turrets:
            bullet_type = self.bullet_types[self.num_turrets - 1]
            bullet_speed = self.bullet_speeds[self.num_turrets - 1]
            if self.num_turrets == 1:
                self.bullets_fired.append(Bullet(self.x + 11, self.y - 15, bullet_type, -bullet_speed))
            elif self.num_turrets == 2:
                self.bullets_fired.append(Bullet(self.x - 12, self.y + 20, bullet_type, -bullet_speed))
                self.bullets_fired.append(Bullet(self.x + 35, self.y + 20, bullet_type, -bullet_speed))
            elif self.num_turrets == 3:
                self.bullets_fired.append(Bullet(self.x + 11, self.y - 15, bullet_type, -bullet_speed))
                self.bullets_fired.append(Bullet(self.x - 12, self.y + 20, bullet_type, -bullet_speed))
                self.bullets_fired.append(Bullet(self.x + 35, self.y + 20, bullet_type, -bullet_speed))
            pygame.mixer.Sound("assets/laser.wav").play()

    # Move all the fired bullets (upwards)
    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move_vertical()

    # Remove all bullets that flew offscreen
    def remove_offscreen_bullets(self):
        self.bullets_fired = list(filter(lambda b: b.y >= 0, self.bullets_fired))

    # Check if the player collided with an enemy bullet
    def collided_with_bullet(self, bullets: list):
        for i in range(len(bullets)):
            dx = bullets[i].x - self.x
            dy = bullets[i].y - self.y
            if self.mask.overlap(bullets[i].mask, (dx, dy)) is not None:
                return True
        return False

    # Check if the player collided with an enemy
    def collided_with_enemy(self, enemy: Enemy):
        dx = enemy.x - self.x
        dy = enemy.y - self.y
        if self.mask.overlap(enemy.mask, (dx, dy)) is not None:
            return True
        return False

    # Deduct a life and move the player offscreen
    def lose_life(self):
        pygame.mixer.Sound("assets/explosion.wav").play(0, 800)
        self.y = 2500
        self.lives -= 1

    # Reset the player to its default position
    def recenter(self):
        self.x = 370
        self.y = 480
        self.num_turrets = 1
