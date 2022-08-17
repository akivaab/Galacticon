import pygame


class Enemy:
    def __init__(self, x, y, image, ship_speed, bullet_speed, fire_freq):
        self.x = x
        self.y = y
        self.image = image
        self.alive = True
        self.ship_speed = ship_speed
        self.bullet_speed = bullet_speed
        self.fire_freq = fire_freq
        self.bullets_fired = []
        self.mask = pygame.mask.from_surface(self.image)

    # Display the enemy on the screen
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # Move the enemy on a predetermined track (implement in subclasses)
    def move(self):
        pass

    # Fire a bullet at random (implement in subclasses)
    def random_fire(self):
        pass

    # Move all the fired bullets (downwards)
    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move_vertical()

    # Remove all bullets that flew offscreen
    def remove_offscreen_bullets(self):
        self.bullets_fired = list(filter(lambda b: b.y < 800, self.bullets_fired))

    # Check if the enemy collided with the player's bullets
    def collided_with_bullet(self, bullets: list):
        for i in range(len(bullets)):
            dx = bullets[i].x - self.x
            dy = bullets[i].y - self.y
            if self.mask.overlap(bullets[i].mask, (dx, dy)) is not None:
                return i
        return -1

    # Move the enemy offscreen upon it being hit
    def hit(self):
        self.y = 2000
        self.alive = False
