import pygame
import random
pygame.init()
ship = pygame.image.load('img.jpg')
ship = pygame.transform.scale(ship, (1280, 400))
wrigth = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'), pygame.image.load('L9.png')]
wleft = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
front =  pygame.image.load('standing.png')
front = pygame.transform.scale(front, (100, 100))
win = pygame.display.set_mode((ship.get_width(), ship.get_height()))
rok = [pygame.image.load('rock1.png'), pygame.image.load('rock2.png'), pygame.image.load('rock3.png'),pygame.image.load('rock4.png'),pygame.image.load('rock5.png')]
rokkk = [pygame.image.load('rok1.png'), pygame.image.load('rok2.png'), pygame.image.load('rok3.png'),pygame.image.load('rok4.png'),pygame.image.load('rok5.png')]
powerball = pygame.image.load('pwr2.png')
powerball = pygame.transform.scale(powerball, (150, 100))
broken = pygame.image.load('b.png')
run = 1
for i in range(0, 9):
    wrigth[i] = pygame.transform.scale(wrigth[i], (100, 100))
    wleft[i] = pygame.transform.scale(wleft[i], (100, 100))
y = 0
w = 0
vel = 4
b = 0
j = False
h = 0
jc = 7
wc = 0
wl = 0
print(ship.get_height())
rit = False
lft = False
xx = 0
xx1 = 0
xx2 = 0
xx3 =0
xx4 = 0
rockc = 0
gulx = 0
guly = wrigth[1].get_height()
print(guly)
rokk = []
for i in range(0, 5):
    rokk.append(pygame.transform.scale(rokkk[i], (100, 100)))
rokkdu = []
for i in range(0, 5):
    rokkdu.append(pygame.transform.scale(rokkk[i], (100, 100)))
print(rokkdu)
yy = random.randint(0, ship.get_width())
yy1 = random.randint(0, ship.get_width())
yy2 = random.randint(0, ship.get_width())
yy3 = random.randint(0, ship.get_width())
yy4 = random.randint(0, ship.get_width())
while run:
    pygame.time.delay(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        w -=9
        lft = True
        rit = False
    elif key[pygame.K_RIGHT]:
        w += 9
        rit = True
        lft = False
    if not(j):

        if key[pygame.K_UP]:
            j = True
            rit = True
            lft = True
    else:
        if jc >= -7:
            neg = 1
            if jc < 0:
                neg = -1
            y-=(jc**2)*2*neg/2
            jc-= 1
        else:
            jc = 7
            j = False

    win.blit(ship, (0, 0))
    if lft & (rit== False):

        wc = 0
        win.blit(wrigth[wl], (w, y + 250))
        if wl < 8:
            wl += 1
        else:
            wl = 0

    elif rit & (lft == False) :

        wl = 0
        win.blit(wleft[wc], (w, y + 250))
        if wc < 8:
            wc += 1
        else:
            wc = 0
    elif rit & lft:
        wc = 0
        wl = 0
        win.blit(front, (w, y + 250))
    elif  (rit == False )& (lft == False) :
        wc = 0
        wl = 0
        win.blit(front, (w, y+250))

    if xx1 == ship.get_height():
        yy1 = random.randint(0, ship.get_width())
        xx1 = 0
    if xx == ship.get_height():
        yy = random.randint(0, ship.get_width())
        xx = 0
    if xx2 == ship.get_height():
        yy2 = random.randint(0, ship.get_width())
        xx2 = 0
    if xx3 == ship.get_height():
        yy3 = random.randint(0, ship.get_width())
        xx3 = 0
    if xx4 == ship.get_height():
        yy4 = random.randint(0, ship.get_width())
        xx4 = 0
    xx3 += 8
    xx += 1
    xx1 += 2
    xx2 += 4
    xx4 += 10
    win.blit(rokk[int(0)], (yy, xx))
    win.blit(rokk[int(1)], (yy1, xx1))
    win.blit(rokk[int(2)], (yy2, xx2))
    win.blit(rokk[int(3)], (yy3, xx3))
    win.blit(rokk[int(4)], (yy4, xx4))
    if key[pygame.K_SPACE]:
        gulx = w
        guly = y
        h = 1
    gulx += 10
    if h:
        win.blit(powerball, (gulx - 50, guly + 200))
    if gulx == ship.get_width():
        h = 0
    if ((yy<w and yy+39>w) and (xx< y+287 and xx + 39> y+287)) or ((yy1<w and yy1+39>w) and (xx1< y+287 and xx1 + 39> y+287)) or ((yy2<w and yy2+39>y+287) and (xx2< y+287 and xx2 + 39> y+287)) or ((yy3<w and yy3+39>w) and (xx3< y+287 and xx3 + 39> y+287)) or ((yy4<w and yy4+39>w) and (xx4< y+287 and xx4 + 39> y+287)):
        if ((yy < w and yy + 39 > w) and (xx< y+287 and xx + 39> y+287)):
            rokk[0]= broken
        if ((yy1 < w and yy1 + 39 > w) and (xx1< y+287 and xx1 + 39> y+287)):
            rokk[1]= broken
        if ((yy2 < w and yy2 + 39 > w) and (xx2< y+287 and xx2 + 39> y+287)):
            rokk[2]= broken
        if ((yy3 < w and yy3 + 39 > w) and (xx3< y+287 and xx3 + 39> y+287)):
            rokk[3]= broken
        if ((yy4 < w and yy4 + 39 > w) and (xx4< y+287 and xx4 + 39> y+287)):
            rokk[4]= broken

        b = b+1
    if xx == ship.get_height() - 1:
        rokk[0] = rokkdu[0]
    if xx1 == ship.get_height() - 2:
        rokk[1] = rokkdu[1]
    if xx2 == ship.get_height() - 4:
        rokk[2] = rokkdu[2]
    if xx3 == ship.get_height() - 8:
        rokk[3] = rokkdu[3]
    if xx4 == ship.get_height() - 10:
        rokk[4] = rokkdu[4]
    txt = pygame.font.SysFont('Cosmicsans', 30, True, True).render(f'Score = {b}', 1, (244, 245, 222))
    wid = ship.get_width()
    win.blit(txt, ((wid - 340), 0))
    pygame.display.update()
pygame.quit()