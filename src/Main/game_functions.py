import sys 
import pygame
import random
import array

sys.path.append('../Entities')

from bullet import Bullet
from enemy import Enemy
from settings import Settings


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
        shoot(ai_settings,screen,ship,bullets)

    elif event.key == pygame.K_q:
        #close - debug key
        sys.exit()    
   
    elif event.key == pygame.K_ESCAPE:
        ai_settings.option = "Pause"

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


def shoot(ai_settings,screen,ship,bullets):
    #Make bullets
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    bullets.update()
    #Removes bullets
    for bullet in bullets.copy():
      if bullet.rect.bottom <=0:
        bullets.remove(bullet)


def collision(enemies,ship,ai_settings):
    #Checks if the ship crashes with the enemy
        for enemy_number in enemies:
            if enemy_number.x  <= ship.rect.x and enemy_number.x + ship.rect.width+(ship.rect.width/2) >= ship.rect.x:
                if enemy_number.y <= ship.rect.y and enemy_number.y + ship.rect.height >= ship.rect.y:
                    if ai_settings.ship_lives >0:
                        enemies.remove(enemy_number)
                        ai_settings.ship_lives -= 1


def create_army(ai_settings,screen,enemies):
    #creates enemy
    enemy = Enemy(ai_settings,screen)
    enemy_width = enemy.rect.width

    #calculate how much can fit in the screen
    available_space_h = ai_settings.screen_width - (1 * enemy_width)
    ai_settings.num_enemies = int(available_space_h / (1 * enemy_width))-random.randint(1,4)
    ####################### Needs more work
    for enemy_number in range(ai_settings.num_enemies):
        enemy = Enemy(ai_settings,screen)
        enemy.x = (enemy_width * enemy_number) + 20*enemy_number
        enemy.rect.x = enemy.x
        enemies.add(enemy)


def update_enemies(enemies,ai_settings):
    #make enemies move
    enemies.update()
    for enemy in enemies.copy():
        if enemy.rect.top > ai_settings.screen_height:
            enemies.remove(enemy)

def restart(ai_settings):
    #reset everything
    ai_settings.ship_lives = 3
    ai_settings.num_enemies = 0
    ai_settings.ship_score = 0
    ai_settings.retry = None
    ai_settings.option = ""

def die(enemies,bullets,ship,ai_settings):
    #Checks for collisions of the ships and the bullets
    #Deletes ships
    for enemy_number in enemies:
        for bullet_number in bullets: 
         if enemy_number.x  <= bullet_number.x and enemy_number.x + ship.rect.width+(ship.rect.width/2)+5 >= bullet_number.x:
            if enemy_number.y <= bullet_number.y and enemy_number.y + ship.rect.height >= bullet_number.y:
                enemies.remove(enemy_number)
                bullets.remove(bullet_number)
                ai_settings.ship_score += 20


def play_music(ai_settings):
    #plays music
    if ai_settings.mis_playing == False:
        pygame.mixer.music.play()
        ai_settings.mis_playing = True


def update_screen(ai_settings, screen, ship, enemies ,bullets):
    #makes the movements appear
    #Redraw the screen during each pass through  the loop.

    #Paints the background
    screen.fill(ai_settings.bg_color)

    #Make the score appear
    numScore = 'Score : '+ str(ai_settings.ship_score) + ' '
    textScore = ai_settings.scoreFont.render(numScore, True, ai_settings.text_color,ai_settings.bg_color)
    scoreRect = textScore.get_rect()
    scoreRect.x = ai_settings.score_x
    scoreRect.y = ai_settings.score_y

    #Make ship lives appear
    numLives = 'lives : '+ str(ai_settings.ship_lives) + ' '
    textLives = ai_settings.livesFont.render(numLives,True,ai_settings.text_color,ai_settings.bg_color)
    livesRect = textLives.get_rect()
    livesRect.x = ai_settings.lives_x
    livesRect.y = ai_settings.lives_y
    
    #Redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    #renders everything
    screen.blit(textScore,scoreRect)
    screen.blit(textLives,livesRect)
    ship.blitme()
    enemies.draw(screen)
    die(enemies, bullets,ship,ai_settings)
    collision(enemies,ship,ai_settings)
    update_enemies(enemies,ai_settings)

    #make constant enemies
    if len(enemies) == 0:
        create_army(ai_settings,screen,enemies)

    #make the most recently drawn screen visible.
    pygame.display.flip() 