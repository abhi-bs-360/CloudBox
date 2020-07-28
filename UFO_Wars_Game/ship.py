import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        #Initialize the ship and its starting position

        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load ship image and similar stuffs
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        #Flag line to enable continuos motion in future
        self.moving_right = False
        self.moving_left = False


    def update(self):
        '''Update ship's position(co-ord) based on flag value'''
        if self.moving_right and  self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        '''Draw ship at the curr-location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
