import pygame, sys, math

#https://github.com/KRHS-GameProgramming-2016/Spoonghetti-Man/blob/master/AIPlayer.py
class Player():
    def __init__(self, pos=[0,0], tileSize = 50):
        tileSize = tileSize - 6
        self.imageUp = pygame.image.load('Resources/PlayerImages/PlayerU.png')
        self.imageDown = pygame.image.load('Resources/PlayerImages/PlayerD.png')
        self.imageRight = pygame.image.load('Resources/PlayerImages/PlayerR.png')
        self.imageLeft = pygame.image.load('Resources/PlayerImages/PlayerL.png')
        self.imageUp = pygame.transform.scale(self.imageUp, [tileSize,tileSize])
        self.imageDown = pygame.transform.scale(self.imageDown, [tileSize,tileSize])
        self.imageRight = pygame.transform.scale(self.imageRight, [tileSize,tileSize])
        self.imageLeft = pygame.transform.scale(self.imageLeft, [tileSize,tileSize])
        self.image = self.imageLeft
        self.rect = self.image.get_rect(center = pos)
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.maxSpeed = 5
        self.startPos = pos

    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeed
            self.image = self.imageUp
        if direction == "down":
            self.speedy = self.maxSpeed
            self.image = self.imageDown
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.image = self.imageLeft
        if direction == "right":
            self.speedx = self.maxSpeed 
            self.image = self.imageRight
        if direction == "stop up":
            self.speedy = 0
        if direction == "stop down":
            self.speedy = 0
        if direction == "stop left":
            self.speedx = 0
        if direction == "stop right":
            self.speedx = 0
        
    def bounceScreen(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
            self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
            self.didBounceY = True
            
    def bounceWall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.move()
                self.speedx = 0
                self.didBounceX = True
                self.speedy = 0
                self.didBounceY = True
                
    def bounceEnemy(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.rect.center = self.startPos

    
    def bounceGoal(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                return True
        return False
        
    #def enemyCollide(self, enemy):
         #if self.rect.right > enemy.rect.left and self.rect.left < enemy.rect.right:
            #if self.rect.bottom > enemy.rect.top and self.rect.top < enemy.rect.bottom:
                #self.player.
