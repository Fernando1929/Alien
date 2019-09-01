import sys
import pygame
sys.path.append('../Entities/')
sys.path.append('../Sound/')

from ship import Ship
from enemy import Enemy
from settings import Settings
from pygame.sprite import Group
import game_functions as gf



def run_game():

    #Initialize game and create a screen object
    #pygame.mixer.pre_init(44100, 16, 2, 4096) (Unused code for testing)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Gal Game")

    #Entity
    ship = Ship(ai_settings,screen)

    #make a group to store them
    bullets = Group()
    enemies = Group()

    #creates enemys
    gf.create_army(ai_settings,screen,enemies)

    #Start the main loop for the game
    while True: 
            gf.play_music(ai_settings)
            gf.check_events(ai_settings,screen,ship,bullets)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_screen(ai_settings,screen,ship,enemies,bullets)
          


run_game()
