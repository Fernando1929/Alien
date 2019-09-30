import sys
import os
import pygame

from settings import Settings
from tinydb import TinyDB, Query

db = TinyDB('../Main/scores.json')
User = Query()

##verify all of it 

def readScores(ai_settings):
    #input name *Need a method to input the name of the player*

    if(len(db)<5):
        db.insert({'name': '#','Position':db.lenght-1,'score':ai_settings.ship_score})

    elif(db.search(User.score < ai_settings.ship_score)):
        User.name = "New one"
        User.score = ai_settings.ship_score

    elif(db.search(User.score == ai_settings.ship_score)):
        User.name = "New one"
        User.score = ai_settings.ship_score


def showScores(ai_settings, screen):
    #finds the file
    if os.path.isfile('../Main/scores.json'):
        #opens the file
        for i in db:
            print(i)

def scoreChoice(ai_settings):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ai_settings.option = ""



