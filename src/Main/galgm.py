import sys
import pygame
sys.path.append('../Entities/')
sys.path.append('../Sound/')

from ship import Ship
from enemy import Enemy
from settings import Settings
from pygame.sprite import Group

import game_functions as gf
import menu_state as mn


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
    while (not ship.is_dead): 

        if(ai_settings.option == "Play"):
                gf.play_music(ai_settings)
                gf.check_events(ai_settings,screen,ship,bullets)
                ship.update()
                gf.update_bullets(bullets)
                gf.update_screen(ai_settings,screen,ship,enemies,bullets)
                        

                if ai_settings.ship_lives == 0 and ai_settings.retry:
                    ship.is_dead = True

                if ai_settings.ship_lives == 0 and (not ai_settings.retry):
                    sys.exit()

        else:
            mn.mainMenu(ai_settings, screen)
            mn.choiceMenu(ai_settings)


run_game()
