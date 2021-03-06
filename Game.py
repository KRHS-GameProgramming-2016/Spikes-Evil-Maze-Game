import pygame, sys, math, random

from Level import *
from Goal import *
from Player import *
from Wall import *
from Timer import *
from Score import *
from LevelIndicator import *
from Enemy import *

pygame.init()  

clock = pygame.time.Clock()
  
width = 1200
height = 700
    
size = width, height
screen = pygame.display.set_mode(size)  

bgColor = r,g,b = 21, 64, 22

level = Level("level1.lvl")

walls = level.walls
enemies = level.enemies
player = level.player
goal = level.goal
print goal.rect
 
using = "keyboard"

levelNumber = 1
levelIndicator = LevelIndicator([width-10, 10], levelNumber)

enemies = level.enemies
print len(enemies)



timer = Timer([width/2, 50])
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
    for enemy in enemies:
        enemy.move()  
    
    for wall in walls:
        player.bounceWall(wall)
        
    
    for enemy in enemies:
        enemy.move()
        for wall in walls:
            enemy.bounceWall(wall)
        player.bounceEnemy(enemy)
        
    
    if player.bounceGoal(goal):
        level.unloadLevel()
        levelNumber += 1
        level.loadLevel("level"+str(levelNumber)+".lvl")
        walls = level.walls
        player = level.player
        enemies = level.enemies
        goal = level.goal
        levelIndicator.set(levelNumber)

    timer.update()
    #print levelIndicator.value, levelIndicator.rect

    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(goal.image, goal.rect)
    screen.blit(player.image, player.rect)
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    screen.blit(timer.image, timer.rect)
    screen.blit(levelIndicator.image, levelIndicator.rect)
    pygame.display.flip()
    clock.tick(60)
