import pygame
import sys
from pygame.locals import *
# init
pygame.init()
dp = pygame.display.set_mode((800, 600))
pygame.display.set_caption('hello')
error = 0
RED = (255, 0, 0)
rect1 = pygame.Rect(0, 0, 80, 50)
clk = pygame.time.Clock()
pygame.key.set_repeat(1, 10)

# main loop
while not error:
    clk.tick(60)
    for ev in pygame.event.get():
        dp.fill((0, 0, 0))
        # key move the rect1
        if ev.type == pygame.KEYDOWN:
            if ev.key == K_d:
                rect1.right += 10
                rect1.left += 10
            if ev.key == K_a:
                rect1.right -= 10
                rect1.left -= 10
        # draw rect1
        pygame.draw.rect(dp, RED, rect1)

        # quit
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()