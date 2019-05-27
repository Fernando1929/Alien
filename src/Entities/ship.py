import sys
import pygame
import game_functions as gf
sys.path.append('../Main/')


class Ship():
    
    def __init__(self,ai_settings,screen):
        #init the ship and set starting position
        self.screen = screen
        self.ai_settings = ai_settings

        #load the image
        self.image = pygame.image.load('../images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start new ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom =  self.screen_rect.bottom

        #Saves center var
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #Actions bool - movement
        self.moving_right = False
        self.moving_left =  False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #changes the ship position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.centery > self.screen_rect.top+24:
            self.centery -= self.ai_settings.ship_speed_factor
        
        if self.moving_down and self.centery < self.ai_settings.screen_height-24:
            self.centery += self.ai_settings.ship_speed_factor

        #updates rect object
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        #Draw ship in the current location
        self.screen.blit(self.image , self.rect)

