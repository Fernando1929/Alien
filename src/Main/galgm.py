import sys
import pygame
sys.path.append('../Entities/')

from ship import Ship
from enemy import Enemy
from settings import Settings
from pygame.sprite import Group
import game_functions as gf



def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Gal Game")

    #things
    ship = Ship(ai_settings,screen)

    #make a group to store them
    bullets = Group()
    enemys = Group()

    #creates enemys
    gf.create_army(ai_settings,screen,enemys)

    #Start the main loop for the game
    while True:
            gf.check_events(ai_settings,screen,ship,bullets)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_screen(ai_settings,screen,ship,enemys,bullets)

run_game()
