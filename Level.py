import pygame, sys, math
from Player  import *
from Wall import *
class Level():
    def __init__(self, levelFile, tileSize=25):
        self.walls = []
        self.tileSize = tileSize
        self.player = None
        self.loadLevel(levelFile)
    
    def unloadLevel(self):
        self.walls = []
      
               
    def loadLevel(self, levelFile):        
        f = open("Resources/levels/"+levelFile, 'r')
        lines = f.readlines()
        f.close()
        
        """
        print lines
        print "________________________"
        
        for line in lines:
            print line
        print "________________________"
        """
        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]
            
        lines = newlines
        
        for line in lines:
            print line
        print "________________________"
        
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c == '#':
                    self.walls += [Wall("wall.png",
                                        [x*self.tileSize + self.tileSize/2,
                                         y*self.tileSize + self.tileSize/2],
                                        self.tileSize)
                                  ]
                if c == "@":
                    self.player = Player([x*self.tileSize + self.tileSize/2,
                                          y*self.tileSize + self.tileSize/2],
                                          self.tileSize)

        
#Level("level1.lvl")
