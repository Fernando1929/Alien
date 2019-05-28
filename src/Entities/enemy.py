import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):

    def __init__(self,ai_settings, screen):
        #set the enemy
        super(Enemy,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load image
        self.image = pygame.image.load('../images/alienspace.png')
        self.rect = self.image.get_rect()

        #starts the enemy ship in the senter of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Stores the x and y position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.enemy_speed

    def update(self):
        #Makes the enemy go down
        self.y += self.speed_factor
        self.rect.y = self.y

    def blitme(self):
        #draw the enemy ship
        self.screen.blit(self.image,self.rect)


