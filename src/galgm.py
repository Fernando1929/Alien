import pygame
from settings import Settings
from ship import Ship
from enemy import Enemy
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    #Initializa game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Gal Game")

    #things
    ship = Ship(ai_settings,screen)
    #make a group to store them
    bullets = Group()
    enemy = Enemy(screen)

    #Start the main loop for the game
    while True:
            gf.check_events(ai_settings,screen,ship,bullets)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_screen(ai_settings,screen,ship,enemy,bullets)

run_game()
