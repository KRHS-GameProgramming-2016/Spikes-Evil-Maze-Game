import pygame, sys, math, random
from Level import *
from Goal import *  
from Player import *
from Score import *
from Timer import *
from Wall import *
pygame.init()  

clock = pygame.time.Clock()

width = 1200  
height = 1200

width = 1200
height = 700

size = width, height
screen = pygame.display.set_mode(size)  

bgColor = r,g,b = 21, 64, 22

level = Level("level1.lvl")

Goals = [Goal("Resources/Goal.png")
        ]

walls = level.walls

player = level.player

using = "keyboard"

levelNumber = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if using == "keyboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.go("up")
                if event.key == pygame.K_DOWN:
                    player.go("down")
                if event.key == pygame.K_RIGHT:
                    player.go("right")
                if event.key == pygame.K_LEFT:
                    player.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_LEFT:
                    player.go("stop left")

    player.move()
    

    for wall in walls:
        player.bounceWall(wall)
        
    for hitter in Goals:
        for hittie in Goals:
            if hitter != hittie:
                hitter.bounceGoal(hittie)
        if player.bounceGoal(hitter):
            Goals.remove(hitter)
            level.unloadLevel()
            levelNumber += 1
            level.loadLevel("level"+str(levelNumber)+".lvl")
            walls = level.walls

    bgColor = r,g,b

    for Goal in Goals:
        screen.blit(Goal.image, Goal.rect)
    screen.blit(player.image, player.rect)
    screen.blit(player.image, player.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)
