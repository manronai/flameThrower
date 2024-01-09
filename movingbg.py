import pygame
import time
pygame.init()
bg = pygame.image.load('img.jpg')
win = pygame.display.set_mode((bg.get_width(), bg.get_height()))
fps = pygame.time.Clock()
tpl = ()
list = []
strstp = 1
startlisting = 0
keys = []
ballstart = 0
i = 0
x = 0
y = 0
while strstp:

    fps.tick(408)
    keys = pygame.event.get()
    key = pygame.key.get_pressed()

    for event in keys:
        if event.type == pygame.QUIT:
            strstp = 0
    if key[pygame.K_RIGHT]:
        x-=1
        #y+=1
    if key[pygame.K_LEFT]:
        x+=1
        #y-=1
    if x == bg.get_width() or x == -bg.get_width():
        x = 0

    win.blit(bg, (x, y))
    win.blit(bg, (bg.get_width()+x, y))
    win.blit(bg, (-bg.get_width()+x, y))
    pygame.display.update()
    


pygame.quit()