import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        #creates a bullet at the ship position
        super(Bullet,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #stores yPosition
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        #color of the bullet
        # make it lightgreen like neon
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #Moves the bullet
        self.y -= self.speed_factor
        #Set the bullet movement
        self.rect.y = self.y
    

    def draw_bullet(self):
        #draws the bullet
        pygame.draw.rect(self.screen,self.color,self.rect)








