import pygame
from pygame.locals import *
from sys import exit
import random
import numpy


pygame.init()


win = pygame.display.set_mode((800,540))

pygame.display.set_caption("Bomb Boom Boom")
backg = pygame.image.load("backg.jpg")
redP = pygame.image.load("redplayer.jpg")
greenP = pygame.image.load("greenplayer.jpg")
blueP = pygame.image.load("blueplayer.jpg")
yellowP = pygame.image.load("yellowplayer.jpg")
bomb = pygame.image.load("bomb.jpg")
boom = pygame.image.load("boom.jpg")

clock = pygame.time.Clock()

class gridColor(object):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        
        self.color = color
    
    def draw(self,win):
        for i in range(0,11):
            for j in range(0,8):
                pygame.draw.rect(win,self.color,(193+i*50,71+j*50,49,49))

    def coloring(self,win):
        #light red:[255,78,77]
        startX = ((self.x-193)/50)*50+193
        startY = ((self.y-71)/50)*50+71
        pygame.draw.rect(win,self.color,(startX,startY,49,49))
        if startX - 50 > 193: 
            pygame.draw.rect(win,self.color,(startX-50,startY,49,49))
        if startX + 50 < 738:
            pygame.draw.rect(win,self.color,(startX+50,startY,49,49))
        if startY - 50 > 71:
            pygame.draw.rect(win,self.color,(startX,startY-50,49,49))
        if startY + 50 < 467:
            pygame.draw.rect(win,self.color,(startX,startY+50,49,49))
        

        
        
        
        
        
class bomb(object):
    def __init__(self,x,y,cover=1):
        self.x = x
        self.y = y
        self.cover = cover
        self.time = 2000

    def update(self,dt):
        self.time -= dt

    def explode(self,win):
        win.blit(boom,self.x,self.y)

    def draw(self,win):
        win.blit(bomb,self.x,self.y)
       
                                   
class playerAutoA(object):
    def __init__(self,x,y,width,height,color,image):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.color = color
 
        self.setBomb = False
        self.image = image

    def draw(self,win):
        win.blit(redP,(self.x-25,self.y-25))
        pygame.time.delay(100)
        self.move()
        #grid1 = gridColor(self.x,self.y,[255,78,77])
        #grid1.coloring(win)
        
    
    def move(self):
        centerColor = []
        nearest = (800,540)
        #create a list to store
        #the unit squares that are not be colored as playerA's color
        for i in range(0,11):
            for j in range(0,8):
                unitColor = pygame.Surface.get_at(win,(218+i*50,96+j*50))[:3]
                centerColor.append((unitColor,(218+i*50,96+j*50)))
        #find the nearest one
        for i in centerColor:
            if i[0] != self.color:
                distance = abs(self.x-i[1][0]) + abs(self.y-i[1][1])
                if distance <= (nearest[0]+nearest[1]):
                    nearest = (self.x-i[1][0],self.y-i[1][1])
       
        #navigate the playerA to the nearest to set bomb
        if nearest[0] <= 0:
            move_x = abs(nearest[0])
            while move_x not in [0,1,2]:
                self.x += self.vel
                move_x -= self.vel
        elif nearest[0] > 0:
            move_x = nearest[0]
            while move_x not in [0,-1,-2]:
                self.x -= self.vel
                move_x -= self.vel

        if nearest[1] <= 0:
            move_y = abs(nearest[1])
            while move_y not in [0,1,2]:
                self.y += self.vel
                move_y -= self.vel
        elif nearest[1] > 0:
            move_y = nearest[0]
            while move_y not in [0,-1,-2]:
                self.y -= self.vel
                move_y -= self.vel
                
            

        
    

            

   

class player(object):
    def __init__(self,x,y,width,height,color):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.setBomb = False
        self.bombCount = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        

    def draw(self,win):

        if self.color == "red":
            colorP = redP
        elif self.color == "green":
            colorP = greenP
        elif self.color == "blue":
            colorP = blueP            
        elif self.color == "yellow":
            colorP = yellowP

        
        win.blit(colorP,(self.x,self.y))


def window():
    win.blit(backg,(0,0))
    gridbg.draw(win)
    player1.draw(win)
    playerAutoA1.draw(win)
    
    pygame.display.update()



#mainloop

player1 = player(708,427,30,40,"green")           
playerAutoA1 = playerAutoA(733,95,30,40,"red",backg)
gridbg = gridColor(0,0,[255,255,255])



run = True


while run:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player1.x > (player1.vel+200):
        #left bound x = 193
        player1.x -= player1.vel
        player1.left = True
        player1.right = False
        player1.up = False
        player1.down = False

    elif keys[pygame.K_RIGHT] and player1.x < (738-player1.width-player1.vel):
        player1.x += player1.vel
        player1.left = False
        player1.right = True
        player1.up = False
        player1.down = False

    elif keys[pygame.K_UP] and player1.y > (player1.vel+73):
        #the top bound is y = 71
        player1.y -= player1.vel
        player1.left = False
        player1.right = False
        player1.up = True
        player1.down = False

    elif keys[pygame.K_DOWN] and player1.y < (467-player1.height-player1.vel):
        player1.y += player1.vel
        player1.left = False
        player1.right = False
        player1.up = True
        player1.down = False

    
    window()

pygame.quit()

