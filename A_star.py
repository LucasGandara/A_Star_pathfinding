"""
States:
    Open set: nodes that still needs to be evaluated
    closed set: all the nodes that have finished been evaluated
"""
import pygame
from pygame import QUIT
import sys
from math import  hypot
from os import system
pygame.init()

WIDTH = 650
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Algorithm")
clock = pygame.time.Clock()

# How many columns and rows?
cols = 9
rows = 9

#Width and height of each cell of grid
w = (WIDTH - 10) / cols
h = (HEIGHT - 10) / rows
path = []
current = []
class Spot(object):
    def __init__(self, x, y):
        self.f = 0
        self.g = 0
        self.h = 0
        self.x = x # posicion x del punto en el espacio
        self.y = y # Posicion y del punto en el espacio
        self.Neighbors = []
        self.previous = None
        self.obstacle = False

    def addNeighbors(self, spots):
        if self.x >= 1:
            self.Neighbors.append(spots[self.x - 1][self.y])
        if self.x < (cols - 1):
            self.Neighbors.append(spots[self.x + 1][self.y])
        if self.y >= 1:
            self.Neighbors.append(spots[self.x][self.y - 1])
        if self.y < (rows - 1):
            self.Neighbors.append(spots[self.x][self.y + 1])

    def Isover(self):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def heuristic(a, b):
    return hypot(a.x - b.x, a.y - b.y)

def redrawGameWindow(win):
    #pygame.draw.rect(win, (255, 255, 255), (0, 0, WIDTH, HEIGHT))

    #Dibujar la grilla
    for i in range(cols):
        for j in range(rows):
            pygame.draw.rect(win, (0, 0, 255), (spots[i][j].x * w, 1 + spots[i][j].y * h, w, h), 1)

    # Dibujams los openSet con verde
    for i,spot in enumerate(OpenSet):
        pygame.draw.rect(win, (0, 255, 0), (2 + spot.x * w, 3 + spot.y * h, w - 4, h - 4))

    #We draw ClosedSet with red
    for i,spot in enumerate(closedSet):
        pygame.draw.rect(win, (255, 0, 0), (2 + spot.x * w, 3 + spot.y * h, w - 4, h - 4))
   
    # Draw current
    pygame.draw.rect(win, (255, 0, 255), (2 + current.x * w, 3 + current.y * h, w - 4, h - 4))

   # Draw the path in blue
    for spot in path:
        pygame.draw.rect(win, (0, 0, 255), (2 + spot.x * w, 3 + spot.y * h, w - 4, h - 4))

    # Draw Obstacles
    for spot in obstacles:
        pygame.draw.rect(win, (255, 255, 102), (2 + spot.x * w, 3 + spot.y * h, w - 4, h - 4))

    pygame.display.update()

# Create the 2D array
spots = [[Spot(i, j) for j in range(rows)] for i in range(cols)]
for i in range(len(spots)):
    for j in range(len(spots[i])):
        spots[i][j].addNeighbors(spots)

# Definir Obstáculos
obstacles = []
for i in range(1):
    spots[3][1].obstacle = True
    obstacles.append(spots[3][1])

    spots[3][2].obstacle = True
    obstacles.append(spots[3][2])

    spots[4][1].obstacle = True
    obstacles.append(spots[4][1])

    spots[4][2].obstacle = True
    obstacles.append(spots[4][2])

    spots[5][2].obstacle = True
    obstacles.append(spots[5][2])

    spots[5][3].obstacle = True
    obstacles.append(spots[5][3])

    spots[6][2].obstacle = True
    obstacles.append(spots[6][2])

    spots[6][3].obstacle = True
    obstacles.append(spots[6][3])

    spots[2][4].obstacle = True
    obstacles.append(spots[2][4])

    spots[2][5].obstacle = True
    obstacles.append(spots[2][5])

    spots[3][4].obstacle = True
    obstacles.append(spots[3][4])

    spots[3][5].obstacle = True
    obstacles.append(spots[3][5])

    spots[1][6].obstacle = True
    obstacles.append(spots[1][6])

    spots[1][7].obstacle = True
    obstacles.append(spots[1][7])

    spots[2][6].obstacle = True
    obstacles.append(spots[2][6])

    spots[2][7].obstacle = True
    obstacles.append(spots[2][7])

    spots[0][8].obstacle = True
    obstacles.append(spots[0][8])

    spots[5][4].obstacle = True
    obstacles.append(spots[5][4])

    spots[5][5].obstacle = True
    obstacles.append(spots[5][5])

    spots[6][4].obstacle = True
    obstacles.append(spots[6][4])

    spots[6][5].obstacle = True
    obstacles.append(spots[6][5])

OpenSet = []
closedSet = []

start = spots[0][0]
end = spots[-1][-1]
OpenSet.append(start)
current = start

while True:
    clock.tick(30)
    for eventos in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if eventos.type == QUIT:
            sys.exit(0)
    
    # Find the one to evaluate next
    if len(OpenSet) > 0:
        winner = 0

        for i in range(len(OpenSet)):
            if OpenSet[i].f < OpenSet[winner].f:
                winner = i
                
        current = OpenSet[winner] 
        if current == end:
            #Find the path
            path = []
            temp = current
            path.append(temp)
            #As long as the temp has a previous
            while temp.previous:
                current = temp
                path.append(temp.previous)
                temp = temp.previous
            system('cls')
            print('Finish!')
        try:
            OpenSet.remove(current)
        except ValueError as e:
            print(e)
        
        closedSet.append(current)
    
        # Verify Neighbors of the current cell
        neighbors = current.Neighbors
        for neighbor in neighbors:
            if not(neighbor in closedSet)  and not(neighbor.obstacle): # ceck if neighbor is available to visit
                temp = current.g + 1

                if neighbor in OpenSet:
                    if temp < neighbor.g:
                        neighbor.g = temp
                else:
                    neighbor.g = temp
                    OpenSet.append(neighbor)
        
                neighbor.previous = current
            # We aply Heuristics
            neighbor.h = heuristic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h
            
    else:
        # No solution
        pass

    redrawGameWindow(screen)