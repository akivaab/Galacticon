import datetime
from Bullet import *


class Splicer:
    def __init__(self):
        self.x = 0
        self.y = 600
        img = pygame.image.load("assets/enemies/splicer.png").convert()
        img.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(img, (54, 54))

        laser_img_h = pygame.image.load("assets/ammo/laser_wave_h.png").convert()
        laser_img_h.set_colorkey((0, 0, 0))
        self.laser_image_horizontal = pygame.transform.scale(laser_img_h, (24, 24))
        laser_img_v = pygame.image.load("assets/ammo/laser_wave_v.png").convert()
        laser_img_v.set_colorkey((0, 0, 0))
        self.laser_image_vertical = pygame.transform.scale(laser_img_v, (24, 24))
        self.laserbeam_components = []

        self.step = 1
        self.laser_end_time = datetime.datetime.now()

    # Display the splicer on the screen
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # Perform some action based on the current step of the splicer procedure
    def perform_action(self, player_x):
        if self.step == 1:  # aim at player
            self.x = player_x
            self.step += 1
        elif self.step == 2:  # move towards the player
            if self.y > 540:
                self.y -= 0.9
            else:
                self.step += 1
                self.laser_end_time = datetime.datetime.now() + datetime.timedelta(seconds=3.5)
        elif self.step == 3:  # fire laser
            if datetime.datetime.now() >= self.laser_end_time:
                self.step += 1
                return False
            self.continuous_laser_fire()
            self.laserbeam_components.append(Bullet(self.x + 16, self.y, self.laser_image_vertical, -10))
        elif self.step == 4:  # finish laser fire
            if len(self.laserbeam_components) == 0:
                self.step += 1
                return False
            self.continuous_laser_fire()
        elif self.step == 5:  # move away from player
            if self.y < 610:
                self.y += 0.9
            else:
                self.step = 1
                return True
        return False

    # Fire the laser in a constant beam
    def continuous_laser_fire(self):
        remove_laser_indexes = []
        for i in range(len(self.laserbeam_components)):
            self.laserbeam_components[i].move_vertical()
            if self.laserbeam_components[i].y < 280:
                remove_laser_indexes.append(i)
        for i in remove_laser_indexes:
            self.laserbeam_components.pop(i)

    # Move the splicer offscreen
    def move_offscreen(self):
        self.x = 0
        self.y = 600
        self.laserbeam_components.clear()
        self.step = 1
