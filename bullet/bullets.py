import pygame
from os import path


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        BLACK = (0, 0, 0)
        img_dir = path.join('img')
        bullet_img = pygame.image.load(
            path.join(img_dir, "laserRed16.png")).convert()
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
