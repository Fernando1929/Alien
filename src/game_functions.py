import sys 
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    #add the ai_settings to set the boundas of the movement
      #watch for mouse and keyboard events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ai_settings,screen,ship,bullets)

            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #respond to keypress
    if event.key == pygame.K_RIGHT:
    #move the ship to the right
        ship.moving_right = True

    if event.key == pygame.K_LEFT:
    #move the ship to the left
        ship.moving_left = True
    
    if event.key == pygame.K_UP:
    #move the ship up
        ship.moving_up = True
    
    if event.key == pygame.K_DOWN:
    # move the ship down
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        #shoot
        Shoot(ai_settings,screen,ship,bullets)
       
      

def check_keyup_events(event,ship):
    #respond to release
    #Stops movement
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    if event.key == pygame.K_LEFT:
        ship.moving_left = False

    if event.key == pygame.K_UP:
        ship.moving_up = False

    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_bullets(bullets):
    bullets.update()
    #Removes bullets
    for bullet in bullets.copy():
      if bullet.rect.bottom <=0:
        bullets.remove(bullet)

def Shoot(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, enemy ,bullets):
    #makes the movements appear
    #Redraw the screen during each pass through  the loop.
    #Redraw bullets
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    enemy.blitme()

    #make the most recently drawn screen visible.
    pygame.display.flip() 