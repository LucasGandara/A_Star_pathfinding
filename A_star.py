import pygame
from pygame import QUIT
import sys
pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Algorithm")

# How many columns and rows?
cols = 5
rows = 5

#Width and height of each cell of grid
w = (WIDTH - 10) / cols
h = (HEIGHT - 10) / rows


def redrawGameWindow(win):
    #Dibujar la grilla
    for i in range(cols):
        for j in range(rows):
            pygame.draw.rect(win, (255, 0, 0), (cols + i * w, rows + j * h, w, h), 1)

    pygame.display.update()

while True:
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
    
    redrawGameWindow(screen)