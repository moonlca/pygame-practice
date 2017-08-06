import time
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
pin2 = [32, 36, 38, 40]

GPIO.output(16, True)
GPIO.output(18, True)
GPIO.output(22, True)
for i in pin2:
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.output(pin2, 0)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.IN)
pwm = GPIO.PWM(12, 50)
forward_sq = ['1000', '1100', '0100', '0110', '0010', '0011', '0001', '1001']
number = ['11111001', '00001001', '10110111', '10011111', '01001111',
          '11011110', '11111110', '11001001', '11111111', '11011111']
temp = 1
pwm.start(11.5)


def set_moter2(step):
    for i in range(4):
        GPIO.output(pin2[i], step[i] == '1')
        time.sleep(0.0003)


def right(b):
    for i in range(10):
        GPIO.output(35, False)
        GPIO.output(37, True)
        time.sleep(0.001)
        GPIO.output(37, False)
        time.sleep(0.001)
    press(b)


def left(b):
    for i in range(10):
        GPIO.output(35, True)
        GPIO.output(37, True)
        time.sleep(0.001)
        GPIO.output(37, False)
        time.sleep(0.001)
    press(b)


def up(b):
    for a in forward_sq:
        set_moter2(a)
    press(b)


def down(b):
    for a in reversed(forward_sq):
        set_moter2(a)
    press(b)


def press(kb):
    input = GPIO.input(7)
    if(not kb):
        pwm.ChangeDutyCycle(11.5)
        time.sleep(0)
    if(kb):
        pwm.ChangeDutyCycle(12.5)
        time.sleep(0)


def draw(ch):
    if('0' <= ch <= '9'):
        a = int(ch)
	print(ch)
        for i in range(96):
            right(int(number[a][0]))
        for i in range(270):
            up(int(number[a][1]))
        for i in range(200):
            up(int(number[a][2]))
        for i in range(96):
            left(int(number[a][3]))
        for i in range(270):
            down(int(number[a][4]))
        for i in range(96):
            right(int(number[a][5]))
        for i in range(100):
            left(int(number[a][6]))
        for i in range(210):
            down(int(number[a][7]))


try:
	set_moter2('0000')
        ch = sys.argv[1]
        for i in ch:
            draw(i)
            for i in range(40):
                left(0)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
