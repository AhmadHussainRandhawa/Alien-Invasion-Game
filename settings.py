import pygame.image


class Settings:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 680
        self.bg_color = 54, 69, 79
        self.game_name = "Alien Invasion"
        self.game_icon = pygame.image.load("icon.png")

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 12
        self.bullet_color = 0, 0, 0
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # How quickly yhe game speeds up
        self.speedup_scale = 1.3
        self.score_scale = 1.6
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.fleet_speed = 1
        self.alien_points = 5

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fleet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
