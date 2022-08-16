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

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move_vertical()

    def remove_offscreen_bullets(self):
        self.bullets_fired = list(filter(lambda b: b.y >= 0, self.bullets_fired))

    def collided_with_bullet(self, bullets: list):
        for i in range(len(bullets)):
            dx = bullets[i].x - self.x
            dy = bullets[i].y - self.y
            if self.mask.overlap(bullets[i].mask, (dx, dy)) is not None:
                return True, i
        return False, -1

    def hit(self):
        self.y = 2000
        self.alive = False
