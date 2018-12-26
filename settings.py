import pygame

class Settings():
    # A class to store the settings for the game
    def __init__(self):
        # Initialize the game settings
        # Screen Settings
        self.screen_width = 960
        self.screen_height = 640
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
