import pygame
import sys
import random
from pygame.locals import *
pygame.init()
dp = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Get the Ball in the Hoop to Score')
error = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 155, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)
highScore = 0
myfont = pygame.font.SysFont("monospace", 50)
font1 = pygame.font.SysFont("monospace", 50)
font2 = pygame.font.SysFont("monospace", 20)
font3 = pygame.font.SysFont("monospace", 35)
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
scoreCounter = -1
restart = False

#creates the new randomly located hoop when called
def newHoop():
    global x, y, length, height, scoreCounter
    x = int(random.randint(0, 700))
    y = int(random.randint(0, 450))
    length = 100
    height = 100
    scoreCounter += 1
    drawHoop()

#draws the hoop everytime its called
def drawHoop():
    rect2 = pygame.Rect(x, y, length, height-40)
    rect3 = pygame.Rect(x + 5, y + 5, length - 10, height - 50)
    rect4 = pygame.Rect(x + 10, y + 10, length - 20, height - 60)
    rect5 = pygame.Rect(x + 30, y + 20, length - 60, height - 75)
    rect6 = pygame.Rect(x + 30, y + 55, length - 60, height/2 - 60)
    rect7 = pygame.Rect(x + 30, y + 55, length - 60, height - 55)
    #rect8 = pygame.Rect(x, y, length, height)
    #pygame.draw.rect(dp, RED, rect8)
    pygame.draw.rect(dp, WHITE, rect2)
    pygame.draw.rect(dp, BLACK, rect3)
    pygame.draw.rect(dp, WHITE, rect4)
    pygame.draw.rect(dp, BLACK, rect5)
    pygame.draw.rect(dp, ORANGE, rect6)
    pygame.draw.rect(dp, GREY, rect7)


#checks for ball collision with hoop
def hoopCollide():
    if ((cx+20 >= x) and (cx-20 <= x + length)):
        if ((cy+20 >= y) and (cy-20 <= y + height)):
            newHoop()

#shows gameover screen and updates highscore
def gameover():
    global restart
    dp.fill((0, 0, 0))
    label1 = font1.render("GAMEOVER!", 2, WHITE)
    label2 = font3.render("Your Score is: " + str(scoreCounter), 2, WHITE)
    label3 = font3.render("Press Enter to Restart", 2, WHITE)
    dp.blit(label1, (270, 80))
    dp.blit(label2, (220, 130))
    dp.blit(label3, (170, 170))
    if(highScoreUpdater() or restart):
        restart = True
        label4 = font1.render("YOU BEAT THE HIGHSCORE!", 2, WHITE)
        dp.blit(label4, (60, 210))

#prints the gameover screen on repeat
def printGameOver():
    if(GAMEOVER == 1):
        gameover()

#checks then updates high schore if neccasary
def highScoreUpdater():
    scoreChange = False
    global highScore, scoreCounter
    if(scoreCounter > highScore):
        highScore = scoreCounter
        scoreChange = True
    return scoreChange

#draws the score on the board
def drawScore():
    global scoreCounter
    label3 = font2.render("SCORE: " + str(scoreCounter), 2, WHITE)
    dp.blit(label3, (0, 25))

#draws the highscore on the baord
def highScoreWriter():
    #scoreNumber = 10
    global highScore
    highScoreText = font2.render("HIGH SCORE: " + str(highScore), 2, WHITE)
    dp.blit(highScoreText, (0, 0))

#draws the rect and circl
def drawObjects():
    pygame.draw.rect(dp, RED, rect1)
    pygame.draw.circle(dp, ORANGE, (cx, cy), 20, 0)

#resets the points and location after the game has ended
def retry():
    global speed, lock, diry, dirx, barx, cx, cy, shotspeed, xspeed, hitx, GAMEOVER, jumpout, scoreCounter, highScore, restart
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
    scoreCounter = -1
    restart = False
    newHoop()

#bounces the ball of the wall
def keepBallOnTheBoard():
    global cx, dirx
    if cx < 10:
        cx = 10
        dirx = 1
    if cx > 790:
        cx = 790
        dirx = -1

def ballHit():
    global cy, cx, shotspeed, GAMEOVER, diry, dirx, jumpout, xspeed
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
            xspeed = int(xspeed + int((rect1.centerx - hitx) / 15) / 2)
            #scoreCounter += 1
        elif (hitx > rect1.centerx):
            dirx = 1
            xspeed = int(xspeed + int((hitx - rect1.centerx) / 15) / 2)
            #scoreCounter += 1
        elif(hitx == rect1.centerx):
            dirx = -1 * dirx
            #scoreCounter += 1

def lockedBall():
    global cy, cx, dirx, diry, shotspeed, xspeedb
    if lock:
        cx = rect1.centerx
        shotspeed = 0
    elif not GAMEOVER:
        dp.fill((0, 0, 0))
        shotspeed = 10
    cy += (diry * shotspeed)
    cx += (dirx * xspeed)

def blockWalls():
    global cy, shotspeed, diry
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
#creates the first hoop before game starts
newHoop()
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
                    speed = 12
                    barx = 1
                    rect1.right += (barx * speed)
                    rect1.left += (barx * speed)
                if ev.key == K_a:
                    speed = 12
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

    lockedBall()
    # stop
    blockWalls()
    # hit the board or gameover
    ballHit()
    #keeps the ball between the walls
    keepBallOnTheBoard()
    #draws everything every turn
    drawHoop()
    drawScore()
    drawObjects()
    #checks for hoop collision
    hoopCollide()
    #prints the text
    highScoreWriter()
    printGameOver()
    pygame.display.update()
