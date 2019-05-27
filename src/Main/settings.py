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
            self.sFont = pygame.font.Font('freesansbold.ttf',18)
            self.score_bg_color = (173,216,230)
            self.score_text_color = (255,255,255)
            self.score_x = 0
            self.score_y = 5
            
            #Lives counter
            self.lFont = pygame.font.Font('freesansbold.ttf',18)
            self.lives_bg_color = (173,216,230)
            self.lives_text_color = (255,255,255)
            self.lives_x = 500
            self.lives_y = 5

            
            #Background Color :lightblue color
            self.bg_color = (173,216,230)

            #Ship settings
            self.ship_speed_factor = 5
            self.ship_lives = 3

            #Enemys lives
            self.enemy_lives = 1

            #Boss lives - lvl
            self.boss_lives_l1 = 3
            self.boss_lives_l2 = 6
            self.boss_lives_l3 = 9
            self.boss_lives_ult = 12

            #Score
            self.ship_score = 0

            
