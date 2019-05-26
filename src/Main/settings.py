import pygame

class Settings():
    
    def __init__(self):
            #Dimetions
            self.screen_width = 600
            self.screen_height = 600

            #Bullet settings
            self.bullet_speed_factor = 10
            self.bullet_width = 3
            self.bullet_height = 10
            self.bullet_color = (60,60,60)
            self.bullet_limit = 4

            #Score settings
            self.font = pygame.font.Font('freesansbold.ttf',18)
            self.score_bg_color = (0,0,0)
            self.score_text_color = (255,255,255)
            self.score_x = 0
            self.score_y = 5
            
            #Background Color :lightblue color
            #put it multi color?
            self.bg_color = (173,216,230)

            #Ship settings
            self.ship_speed_factor = 5

            #Score
            self.ship_score = 0
            
