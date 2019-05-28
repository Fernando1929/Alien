import sys 
import pygame
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

    elif event.key ==pygame.K_q:
        #close
        sys.exit()
       
   
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

def shoot(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        
def die(enemys,bullets,ship,ai_settings):
    #Checks for collisions of the ships and the bullets
    #Deletes ships
    for enemy_number in enemys:
        for bullet_number in bullets: 
         if enemy_number.x  <= bullet_number.x and enemy_number.x + ship.rect.width+(ship.rect.width/2)+5 >= bullet_number.x:
            if enemy_number.y <= bullet_number.y and enemy_number.y + ship.rect.height >= bullet_number.y:
                enemys.remove(enemy_number)
                bullets.remove(bullet_number)
                ai_settings.ship_score += 20

def collision(enemys,ship,ai_settings):
    #Checks if the ship crashes with the enemy
    if ai_settings.ship_lives ==0:
        #Add here to throw the game over thing
        sys.exit()

    else:
        for enemy_number in enemys:
            if enemy_number.x  <= ship.rect.x and enemy_number.x + ship.rect.width+(ship.rect.width/2) >= ship.rect.x:
                if enemy_number.y <= ship.rect.y and enemy_number.y + ship.rect.height >= ship.rect.y:
                    if ai_settings.ship_lives >0:
                        enemys.remove(enemy_number)
                        ai_settings.ship_lives -= 1

def play_music(ai_settings):
    #plays music
    if ai_settings.mis_playing == False:
        pygame.mixer.music.play()
        ai_settings.mis_playing = True

def create_army(ai_settings,screen,enemys):
    #creates enemy
    enemy = Enemy(ai_settings,screen)
    enemy_width = enemy.rect.width

    #calculate how much can fit in the screen
    available_space_h = ai_settings.screen_width - (1 * enemy_width)
    number_enemys_h = int(available_space_h / (1 * enemy_width))
    
    for enemy_number in range(number_enemys_h):
        enemy = Enemy(ai_settings,screen)
        enemy.x = enemy_width + 1 * enemy_width * enemy_number
        enemy.rect.x = enemy.x
        enemys.add(enemy)

def update_screen(ai_settings, screen, ship, enemys ,bullets):
    #makes the movements appear
    #Redraw the screen during each pass through  the loop.

    #Paints the background
    screen.fill(ai_settings.bg_color)

    #Make the score appear
    numScore = 'Score : '+ str(ai_settings.ship_score) + ' '
    textScore = ai_settings.sFont.render(numScore, True, ai_settings.score_text_color,ai_settings.score_bg_color)
    scoreRect = textScore.get_rect()
    scoreRect.x = ai_settings.score_x
    scoreRect.y = ai_settings.score_y

    #Make ship lives appear
    numLives = 'lives : '+ str(ai_settings.ship_lives) + ' '
    textLives = ai_settings.lFont.render(numLives,True,ai_settings.lives_text_color,ai_settings.lives_bg_color)
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
    enemys.draw(screen)
    die(enemys, bullets,ship,ai_settings)
    collision(enemys,ship,ai_settings)

    #make the most recently drawn screen visible.
    pygame.display.flip() 