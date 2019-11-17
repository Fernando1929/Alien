import sys
import pygame
    

def mainMenu(ai_settings, screen):
        screen.fill(ai_settings.bg_color)

        title = 'Main Menu'
        text4 = ai_settings.text_font.render(title,True,ai_settings.text_color,ai_settings.bg_color)
        t4Rect = text4.get_rect()
        t4Rect.x = 250
        t4Rect.y = 20

        textp = '1.Play'
        text1 = ai_settings.text_font.render(textp,True,ai_settings.text_color,ai_settings.bg_color)
        t1Rect = text1.get_rect()
        t1Rect.x = 300
        t1Rect.y = 100

        texts = '2.Score'
        text2 = ai_settings.text_font.render(texts, True, ai_settings.text_color,ai_settings.bg_color)
        t2Rect = text2.get_rect()
        t2Rect.x = 300
        t2Rect.y = 200

        textq = '3.Quit'
        text3 = ai_settings.text_font.render(textq, True, ai_settings.text_color,ai_settings.bg_color)
        t3Rect = text3.get_rect()
        t3Rect.x = 300
        t3Rect.y = 300

        #renders everything
        screen.blit(text1,t1Rect)
        screen.blit(text2,t2Rect)
        screen.blit(text3,t3Rect)
        screen.blit(text4,t4Rect)

        pygame.display.flip() 

def choiceMenu(ai_settings):
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
                sys.exit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ai_settings.option = ""

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_1 :
            ai_settings.option = "Play"

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            ai_settings.option = "Score"

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            ai_settings.isRunning = False
          
        


