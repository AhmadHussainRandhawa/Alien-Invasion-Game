import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('littleShip.png')
        self.rect = self.image.get_rect()
