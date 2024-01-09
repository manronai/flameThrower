import pygame
pygame.init()
ship = pygame.image.load('img.jpg')
ship = pygame.transform.scale(ship, (1280, 400))
#wrigth = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png'),pygame.image.load('L10.png'),pygame.image.load('L11.png'),]
#wleft = [ pygame.image.load('R1.png'), pygame.image.load('R1.png'), pygame.image.load('R1.png'), pygame.image.load('R1.png'), pygame.image.load('R1.png'), pygame.image.load('R1.png'), pygame.image.load('R1.png'), pygame.image.load('R1.png'), pygame.image.load('R1.png'), pygame.image.load('R1.png'), pygame.image.load('R1.png')]
front =  pygame.image.load('standing.png')
win = pygame.display.set_mode((ship.get_width(), ship.get_height()))
run = 1
y = 0
w = 0
vel = 4
j = False
jc = 7
while run:
    pygame.time.delay(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
    key = pygame.key.get_pressed()
    if not(j):
        if key[pygame.K_LEFT]:
            w -= 2

        if key[pygame.K_RIGHT]:
            w += 2
        if key[pygame.K_UP]:
            j = True
    else:
        if jc >= -7:
            neg = 1
            if jc < 0:
                neg = -1
            y-=(jc**2)*1*neg
            jc-= 1
        else:
            jc = 7
            j = False

    win.blit(ship, (0, 0))
    pygame.draw.rect(win, (0, 0, 0), (w, y+300, 69, 39))

    pygame.display.update()

pygame.quit()


