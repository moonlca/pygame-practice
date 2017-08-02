import pygame
import sys
from pygame.locals import *
# init
# git practice
pygame.init()
dp = pygame.display.set_mode((800, 600))
pygame.display.set_caption('hello')
error = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
rect1 = pygame.Rect(0, 550, 250, 50)
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
jumpout = 0
scoreCounter = 0


def gameover():
    myfont = pygame.font.SysFont("monospace", 50)
    label1 = myfont.render("GAMEOVER!", 2, (255, 255, 0))
    label2 = myfont.render("press enter to retry", 2, (255, 255, 0))

    dp.blit(label1, (250, 200))
    dp.blit(label2, (100, 250))


def retry():
    global speed, lock, diry, dirx, barx, cx, cy, shotspeed, xspeed, hitx, GAMEOVER, jumpout, scoreCounter
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
    jumpout = 0
    scoreCounter = 0


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
                    speed = 10
                    barx = 1
                    rect1.right += (barx * speed)
                    rect1.left += (barx * speed)
                if ev.key == K_a:
                    speed = 10
                    barx = -1
                    rect1.right += (barx * speed)
                    rect1.left += (barx * speed)
                if ev.key == K_SPACE:
                    if lock:
                        cx = rect1.centerx
                        xspeed = 15
                        dirx = barx
                    xspeed = 15
                    lock = 0
            if ev.type == pygame.KEYUP:
                speed = 0
        if GAMEOVER:
            if ev.type == pygame.KEYDOWN:
                if ev.key == K_RETURN:
                    retry()
# unlocked
    if lock:
        cx = rect1.centerx
        shotspeed = 0
    elif not GAMEOVER:
        dp.fill((0, 0, 0))
        shotspeed = 10
    cy += (diry * shotspeed)
    cx += (dirx * xspeed)

    # stop
    if rect1.left < 0:
        rect1.left = 0
        rect1.right = 250
    if rect1.right > 800:
        rect1.left = 550
        rect1.right = 800
    if cy < 10:
        cy = 10
        shotspeed = 0
        diry = 1
# hit the board or gameover
    if cy > 530:

        hitx = cx
        cy = 530
        shotspeed = 0
        diry = -1

        if (hitx < (rect1.left - 20) or hitx > (rect1.right + 20)) and not jumpout:
            GAMEOVER = 1
            gameover()
            diry = 0
            dirx = 0
            jumpout = 1
        elif (hitx < rect1.centerx):
            dirx = -1
            xspeed = int(xspeed + int((rect1.centerx - hitx) / 12) / 2)
            scoreCounter += 1
        elif (hitx > rect1.centerx):
            dirx = 1
            xspeed = int(xspeed + int((hitx - rect1.centerx) / 12) / 2)
            scoreCounter += 1
        elif(hitx == rect1.centerx):
            dirx = -1 * dirx
            scoreCounter += 1

    if cx < 10:
        cx = 10
        dirx = 1
    if cx > 790:
        cx = 790
        dirx = -1

    # draw
    myfont = pygame.font.SysFont("monospace", 50)
    label3 = myfont.render("SCORE: " + str(scoreCounter), 2, (255, 255, 0))
    dp.blit(label3, (250, 30))

    pygame.draw.rect(dp, RED, rect1)
    pygame.draw.circle(dp, BLUE, (cx, cy), 20, 0)
    pygame.display.update()
