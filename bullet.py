import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Create a bullet Rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.midtop = ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.ai_settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.ai_settings.bullet_color, self.rect)
