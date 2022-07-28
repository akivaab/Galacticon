
class Bullet:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= self.speed
