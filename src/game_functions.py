import sys 
import pygame

 

def check_events(ship):
    #add the ai_settings to set the boundas of the movement
      #watch for mouse and keyboard events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    #move the ship to the right
                     ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    #move the ship to the left
                      ship.moving_left = True

            elif event.type == pygame.KEYUP:
                #Stops movement
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False

                if event.key == pygame.K_LEFT:
                    ship.moving_left = False


def update_screen(ai_settings, screen, ship, enemy):
    #makes the movements appear
    #Redraw the screen during each pass through  the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        enemy.blitme()

      #make the most recently drawn screen visible.
        pygame.display.flip() 