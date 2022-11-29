from Bonuses.Bonus import *


class Heart(Bonus):
    def __init__(self, x, y):
        image = pygame.image.load("assets/bonuses/heart.png").convert()
        image.set_colorkey((0, 0, 0))
        image = pygame.transform.scale(image, (24, 24))
        super().__init__(x, y, image)
