import sys
import pygame
from sys import platform
sys.path.append('../Sound')

class Settings():
    
    def __init__(self):
            #Dimetions
            self.screen_width = 600
            self.screen_height = 600

            #Bullet settings
            if platform == "win32":
                self.bullet_speed_factor = 1
            elif platform == "darwin" or platform == "linux" or platform == "linux2" :
                self.bullet_speed_factor = 10
            
            self.bullet_width = 3
            self.bullet_height = 10
            #self.bullet_color = (60,60,60)
            self.bullet_color = (255,255,255)
            self.bullet_limit = 4

            #Score settings
            self.sFont = pygame.font.Font('freesansbold.ttf',18)
            self.score_x = 0
            self.score_y = 5
            
            #Lives counter
            self.lFont = pygame.font.Font('freesansbold.ttf',18)
            self.lives_x = 530
            self.lives_y = 5

            #Color Settings
            #background
            #lightblue  self.lives_text_color = (255,255,255)
            self.bg_color = (0,0,0)
            #text
            self.text_color = (255,255,255)

            #Ship settings
            #checks operating systems
            if platform == "win32":
                self.ship_speed_factor = 0.4
            elif platform == "darwin" or platform == "linux" or platform == "linux2" :
                self.ship_speed_factor = 5
            self.ship_lives = 3

            #Enemy settings
            self.enemy_lives = 1
            self.num_enemies = 0
            if platform == "win32":
                self.enemy_speed = 0.10
            elif platform == "darwin" or platform == "linux" or platform == "linux2" :
                self.enemy_speed = 10

            #Boss lives - lvl
            self.boss_lives_l1 = 3
            self.boss_lives_l2 = 6
            self.boss_lives_l3 = 9
            self.boss_lives_ult = 12

            #Score
            self.ship_score = 0

            #Music Settings 
            self.mis_playing = False
            pygame.mixer.music.load('../Sound/454884__razor5__alien-song.mp3')
            #pygame.mixer.music.load('../Sound/epic-orchestra-loop.wav') (Unused code for testing)
