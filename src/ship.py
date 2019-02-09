import pygame

class Ship():
    
    def __init__(self,ai_settings,screen):
        #init the ship and set starting position
        self.screen = screen
        self.ai_settings = ai_settings

        #load the image
        self.image = pygame.image.load('./images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start new Ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom =  self.screen_rect.bottom

        #Saves center var
        self.center = float(self.rect.centerx)
        #Movement bool
        self.moving_right = False
        self.moving_left =  False

    def update(self):
        #changes the ship pos.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #updates rect object
        self.rect.centerx = self.center

    def blitme(self):
        #Draw ship in the current location
        self.screen.blit(self.image , self.rect)

