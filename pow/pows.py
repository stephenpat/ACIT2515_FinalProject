import pygame
import random
from os import path
img_dir = path.join('img')


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        powerup_images = {}
        powerup_images['shield'] = pygame.image.load(
            path.join(img_dir, 'shield_gold.png')).convert()
        powerup_images['gun'] = pygame.image.load(
            path.join(img_dir, 'bolt_gold.png')).convert()
        self.image = powerup_images[self.type]
        BLACK = (0, 0, 0)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        HEIGHT = 600
        if self.rect.top > HEIGHT:
            self.kill()
