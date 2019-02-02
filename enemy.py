import pygame

class Enemy():

    def __init__(self, screen):
        #set the enemy
        self.screen = screen

        #load image
        self.image = pygame.image.load('./images/alienspace.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #starts the enemy ship in the senter of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        #draw the enemy ship
        self.screen.blit(self.image,self.rect)


