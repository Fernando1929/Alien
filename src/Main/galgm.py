import sys
import pygame
import game_functions as gf

sys.path.append('../Entities/')
sys.path.append('../Sound/')
sys.path.append('../States/')
sys.path.append('../SCManager/')

import menu_state as mn
import score_handler as sc
import death_state as dt
import pause_state as pt

from ship import Ship
from enemy import Enemy
from settings import Settings
from pygame.sprite import Group




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
    while (ai_settings.isRunning == True): 

        if(ai_settings.option == "Play"):

                gf.play_music(ai_settings)
                gf.check_events(ai_settings,screen,ship,bullets)
                ship.update()
                gf.update_bullets(bullets)
                gf.update_screen(ai_settings,screen,ship,enemies,bullets)
            
                if ai_settings.ship_lives == 0:
                    ai_settings.option = "Death"

        elif(ai_settings.option == "Score"):
            sc.showScores(ai_settings,screen)
            sc.scoreChoice(ai_settings)

        elif(ai_settings.option == "Restart"):
            gf.restart(ai_settings)
            ai_settings.option = "Play"

        elif(ai_settings.option == "Shut Down"):
            sys.exit()

        elif(ai_settings.option == "Death"):
            #Future testing
            #sc.readScores(ai_settings)
            dt.deathMenu(ai_settings,screen)
            dt.deathChoice(ai_settings)

        elif(ai_settings.option == "Pause"):
            pt.pauseMenu(ai_settings,screen)
            pt.optionMenu(ai_settings)

        else:
            mn.mainMenu(ai_settings, screen)
            mn.choiceMenu(ai_settings)


run_game()
