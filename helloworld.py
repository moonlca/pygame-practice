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
cx = 20
cy = 530
shotspeed = 1


# main loop
while not error:
    clk.tick(60)
    dp.fill((0, 0, 0))

    # event
    for ev in pygame.event.get():
        # quit
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()
        # key move the rect1
        if ev.type == pygame.KEYDOWN:
            speed += 1
            if ev.key == K_d:
                rect1.right += speed
                rect1.left += speed
            if ev.key == K_a:
                rect1.right -= speed
                rect1.left -= speed
            if ev.key == K_SPACE:
                cx = rect1.centerx
                lock = 0
        if ev.type == pygame.KEYUP:
            speed = 0

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
        cy = 530
        shotspeed = 0
        diry = -1
    if lock:
        cx = rect1.centerx
        shotspeed = 0
    else:
        shotspeed += 1
    cy += (diry * shotspeed)

    # draw
    pygame.draw.rect(dp, RED, rect1)
    pygame.draw.circle(dp, BLUE, (cx, cy), 20, 0)

    pygame.display.update()
