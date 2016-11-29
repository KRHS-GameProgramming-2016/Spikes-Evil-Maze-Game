import pygame, sys, math, random
from Level import *
from Goal import *
from Player import *
from Score import *
from Timer import *
from Wall import *
pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height
screen = pygame.display.set_mode(size)  

bgColor = r,g,b = 0, 0, 0


bgColor = r,g,b
screen.fill(bgColor)
pygame.display.flip()
clock.tick(60)
