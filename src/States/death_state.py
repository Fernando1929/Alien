import sys
import pygame
    

def deathMenu(ai_settings, screen):

        screen.fill(ai_settings.bg_color)

        textp = 'Wanna try Again?'
        text1 = ai_settings.text_font.render(textp,True,ai_settings.text_color,ai_settings.bg_color)
        t1Rect = text1.get_rect()
        t1Rect.x = 300
        t1Rect.y = 100

        texts = 'Y'
        text2 = ai_settings.text_font.render(texts, True, ai_settings.text_color,ai_settings.bg_color)
        t2Rect = text2.get_rect()
        t2Rect.x = 275
        t2Rect.y = 200

        textq = 'N'
        text3 = ai_settings.text_font.render(textq, True, ai_settings.text_color,ai_settings.bg_color)
        t3Rect = text3.get_rect()
        t3Rect.x = 325
        t3Rect.y = 200

        textm = 'too bad'
        text4 = ai_settings.text_font.render(textm,True,ai_settings.text_color,ai_settings.bg_color)
        t4Rect = text4.get_rect()
        t4Rect.x = 300
        t4Rect.y = 0

        textl =  'You Died'
        text5 = ai_settings.text_font.render(textl,True,ai_settings.text_color,ai_settings.bg_color)
        t5Rect = text5.get_rect()
        t5Rect.x = 300
        t5Rect.y = 50

        screen.blit(text1,t1Rect)
        screen.blit(text2,t2Rect)
        screen.blit(text3,t3Rect)
        screen.blit(text4,t4Rect)
        screen.blit(text5,t5Rect)

        pygame.display.flip() 

def deathChoice(ai_settings):
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ai_settings.option = ""

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_y :
            ai_settings.option = "Restart"
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            ai_settings.option = "Shut Down"
          
        


