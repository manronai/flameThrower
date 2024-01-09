import pygame
import time
pygame.init()
win = pygame.display.set_mode((499, 399))
fps = pygame.time.Clock()
tpl = ()
list = []
strstp = 1
startlisting = 0
keys = []
ballstart = 0
i = 0
while strstp:

    fps.tick(408)
    keys = pygame.event.get()
    key = pygame.key.get_pressed()

    #pointlist.append(pygame.mouse.get_pos())

    for event in keys:
        if event.type == pygame.QUIT:
            strstp = 0
        else:
            pass

    if key[pygame.K_UP]:
        print('started')
        startlisting = 1
    if startlisting == 1:
        x, y = pygame.mouse.get_pos()
        list.append((x, y))
        lines = pygame.draw.line(win, (244, 34, 234), (x - 1, y - 1), (x, y), 19)
    if key[pygame.K_DOWN]:
        startlisting = 0
    if list and key[pygame.K_SPACE]:
        ballstart = 1
    if key[pygame.K_LEFT]:
        ballstart = 0
    if ballstart == 1 and i < len(list):

        a, b = list[i]
        i = i + 1
        pygame.draw.rect(win, (33, 39, 30), (a, b, 39, 39), 3)

    #line = pygame.draw.lines(win, (244, 34, 234), (0, 0), pointlist, 1)
    pygame.display.update()
    if ballstart:
        win.fill((0, 0, 0))

pygame.quit()