import pygame, sys, math 

class Score():
    def __init__(self, pos):
        self.value = 0
        #http://www.1001fonts.com/westmeath-font.html
        self.font = pygame.font.Font("Resources/Fonts/Westmeath/Westmeath Italic.otf", 50)
        self.image = self.font.render("Score: " + str(self.value), True, (255,0,0))
        self.rect = self.image.get_rect(center = pos)
    
    def change(self, amount = 1):
        self.value += amount
        if self.value <= 0:
            self.value = 0
        self.image = self.font.render("Score: " + str(self.value), True, (255,0,0))
        self.rect = self.image.get_rect(center = self.rect.center)

