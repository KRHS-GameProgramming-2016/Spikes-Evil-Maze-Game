import sys, pygame
pygame.init() 

PlayerBase = pygame.image.load("Player.png")
PlayerBaserect = PlayerBase.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

