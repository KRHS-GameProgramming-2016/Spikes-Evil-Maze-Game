import pygame, sys, math 

class LevelIndicator():
    def __init__(self, pos, startValue):
        self.value = startValue
        self.image = pygame.image.load("Resources/TextBG.png")
        
        #http://www.1001fonts.com/westmeath-font.html
        self.font = pygame.font.Font("Resources/Fonts/Westmeath/Westmeath Italic.otf", 50)
        self.image.blit(self.font.render("Level: " + str(self.value), True, (255,255,255)), [30,0])
        self.rect = self.image.get_rect(topright = pos)
        print pos, self.rect
    
    def set(self, amount = 1):
        self.value = amount
        self.image = self.font.render("Level: " + str(self.value), True, (255,0,0))
        #self.rect = self.image.get_rect(topright = self.rect.topright)
