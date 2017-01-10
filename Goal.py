import pygame, sys, math, random

class Goal():
    def __init__(self, pos=[0,0], tileSize = 50):
        self.image = pygame.image.load("Resources/Goal.png")
        self.image = pygame.transform.scale(self.image, [tileSize,tileSize])
        self.rect = self.image.get_rect(center = pos)
 
