import pygame, sys, math, random
from Level import *
from Goal import *
#from Player import *
from Score import *
from Timer import *
from Wall import *
pygame.init()  

clock = pygame.time.Clock()

width = 1200  
height = 700
size = width, height
screen = pygame.display.set_mode(size)  

bgColor = r,g,b = 0, 0, 0

level = Level("level1.lvl")

walls = level.walls

levelNumber = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



    bgColor = r,g,b
    screen.fill(bgColor)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)
