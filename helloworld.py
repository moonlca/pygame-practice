import pygame
import sys
from pygame.locals import *
# init

pygame.init()
dp = pygame.display.set_mode((800, 600))
pygame.display.set_caption('hello')
error = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
rect1 = pygame.Rect(0, 550, 80, 50)
clk = pygame.time.Clock()
pygame.key.set_repeat(1, 10)
speed = 0
lock = 1
diry = -1
dirx = 0
barx = 0
cx = 20
cy = 530
shotspeed = 1
xspeed = 0
hitx = 0
GAMEOVER = 0


def gameover():
    myfont = pygame.font.SysFont("monospace", 50)
    label1 = myfont.render("GAMEOVER!", 2, (255, 255, 0))
    label2 = myfont.render("press space to retry", 2, (255, 255, 0))

    dp.blit(label1, (250, 200))
    dp.blit(label2, (100, 250))



# main loop
while not error:
    clk.tick(60)

    # event
    for ev in pygame.event.get():
            # quit
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()

        if not GAMEOVER:
            dp.fill((0, 0, 0))
            # key move the rect1
            if ev.type == pygame.KEYDOWN:
                if ev.key == K_d:
                    speed += 1
                    barx = 1
                    rect1.right += (barx * speed)
                    rect1.left += (barx * speed)
                if ev.key == K_a:
                    speed += 1
                    barx = -1
                    rect1.right += (barx * speed)
                    rect1.left += (barx * speed)
                if ev.key == K_SPACE:
                    cx = rect1.centerx
                    lock = 0
                    dirx = barx
                    xspeed = speed
            if ev.type == pygame.KEYUP:
                speed = 0

    # unlocked
    if lock:
        cx = rect1.centerx
        shotspeed = 0
    elif not GAMEOVER:
        dp.fill((0, 0, 0))
        shotspeed += 1
    cy += (diry * shotspeed)
    cx += (dirx * xspeed)

    # stop
    if rect1.left < 0:
        rect1.left = 0
        rect1.right = 80
    if rect1.right > 800:
        rect1.left = 730
        rect1.right = 800
    if cy < 10:
        cy = 10
        shotspeed = 0
        diry = 1
    if cy > 530:
        hitx = cx
        cy = 530
        shotspeed = 0
        diry = -1
        if (hitx < rect1.left or hitx > rect1.right):
            GAMEOVER = 1
            gameover()
            diry = 0
            dirx = 0

    if cx < 10:
        cx = 10
        dirx = 1
    if cx > 790:
        cx = 790
        dirx = -1

    # draw
    pygame.draw.rect(dp, RED, rect1)
    pygame.draw.circle(dp, BLUE, (cx, cy), 20, 0)
    pygame.display.update()
