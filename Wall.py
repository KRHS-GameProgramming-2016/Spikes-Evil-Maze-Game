import pygame, sys, math, random

class Wall():
    def __init__(self, image, pos, tileSize=50):
        self.image = pygame.image.load("Resources/WallImages/"+image)
        self.image = pygame.transform.scale(self.image, [tileSize,tileSize])
        self.rect = self.image.get_rect(center = pos) 
