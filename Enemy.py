import pygame, sys, math, random



class Enemy():
    def __init__(self, speed=0, pos=[0,0], size=32):
        self.size = size
        self.imageLeft = pygame.image.load("Resources/Enemy/Left1.png")
        self.imageRight = pygame.image.load("Resources/Enemy/Right1.png")
        self.imageUp = pygame.image.load("Resources/Enemy/Up1.png")
        self.imageDown = pygame.image.load("Resources/Enemy/Down1.png")

        self.imageLeft = pygame.transform.scale(self.imageLeft, [self.size,self.size])
        self.imageRight = pygame.transform.scale(self.imageRight, [self.size,self.size])
        self.imageUp = pygame.transform.scale(self.imageUp, [self.size,self.size])
        self.imageDown = pygame.transform.scale(self.imageDown, [self.size,self.size])

        self.image = self.imageRight
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = speed

        self.kind = "normal"

        self.decideDirection()


        self.didBounceX = False
        self.didBounceY = False
        self.inflationTime = 0
        self.inflationLevel = 0

        self.state = "right"
        self.prevState = "right"

        #self.frame = 0
        #self.maxFrame = len(self.images) - 1
        #self.animationTimer = 0
        #self.animationTimerMax = .3 * 60 #seconds * 60 fps


    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        if self.speedx != 0:     #moving left/right
            if self.rect.left % self.size == 0:
                #print "left/right", self.rect.center[0]
                self.decideDirection()
        else:     #moving up/down
            if self.rect.top % self.size == 0:
            #print "left/right", self.rect.center[1]
                self.decideDirection()
        self.animate()

    def decideDirection(self):
        d = random.randint(0,2)
        if d == 0: #up
            self.speedx = 0
            self.speedy = -self.maxSpeed
            self.state = "up"
        elif d == 1: #right
            self.speedx = self.maxSpeed
            self.speedy = 0
            self.state = "right"
        elif d == 2: #down
            self.speedx = 0
            self.speedy = self.maxSpeed
            self.state = "down"
        elif d == 3: #left
            self.speedx = -self.maxSpeed
            self.speedy = 0
            self.state = "left"

    def animate(self):
        if self.prevState != self.state:
            self.prevState = self.state
            if self.state == "right":
                self.image = self.imageRight
            elif self.state == "left":
                self.image = self.imageLeft
            elif self.state == "up":
                self.image = self.imageUp
            elif self.state == "down":
                self.image = self.imageDown

    def bounceWall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.didBounceX = True
                self.didBounceY = True
                self.move()

    def screenCollide(self, screenSize):
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        if self.rect.top < 0 or self.rect.bottom > screenHeight:
            self.speedy = -self.speedy
        if self.rect.center[0] > screenWidth:
            self.rect.center = [0, self.rect.center[1]]
        elif self.rect.center[0] < 0:
            self.rect.center = [screenWidth, self.rect.center[1]]



    def dist(self, pt):
        x = pt[0] - self.rect.right
        y = pt[1] - self.rect.bottom
        if x < 0:
            x += -64
            x += x
        if y < 0:
            y += -64
            y += y
        return [x, y]
        return math.sqrt(xDiff**2 + yDiff**2)
