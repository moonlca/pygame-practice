import time,sys,tty,termios
import RPi.GPIO as GPIO
old_settings=termios.tcgetattr(sys.stdin)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
pin2=[32,36,38,40]

GPIO.output(16, True)
GPIO.output(18, True)
GPIO.output(22, True)
for i in pin2:
        GPIO.setup(pin2,GPIO.OUT)
        GPIO.output(pin2,0)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(7,GPIO.IN)
pwm = GPIO.PWM(12,50)
forward_sq=['1000','1100','0100','0110','0010','0011','0001','1001']
number= ['11111001','00001001','10110111','10011111','01001111','11011110','11111110','11001001','11111111','11011111']
temp=1
pwm.start(10.5)
pen = 0
dc = 0
uc = 0
lc = 0
rc = 0
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
        	GPIO.output(35,True)
        	GPIO.output(37, True)
        	time.sleep(0.001)
        	GPIO.output(37, False)
        	time.sleep(0.001)
        press(b) 
def set_moter2(step):
	for i in range(4):
		GPIO.output(pin2[i],step[i]=='1')
		time.sleep(0.0003)
def up(b):
	for a in forward_sq:
		set_moter2(a)
	press(b) 
def down(b):
        for a in reversed(forward_sq):
                set_moter2(a)
	press(b)
def press(kb):
#	global temp
	input=GPIO.input(7)
        if(not kb):
                pwm.ChangeDutyCycle(10.5)
		time.sleep(0)
	if(kb):
		pwm.ChangeDutyCycle(12.5)
		time.sleep(0)

"""	if((not temp)and input):
                pwm.ChangeDutyCycle(11.5)
        if((not input)and temp):
                pwm.ChangeDutyCycle(12.5)
        temp=kb	
"""

try:
	tty.setcbreak(sys.stdin)	
	while True:
		set_moter2('0000')
		ch=sys.stdin.read(1)
		press(0)
		if  '0' <= ch <= '9':
			a = int(ch)

			for i in range(96):
				right(int(number[a][0]))			
			for i in range(270) :
                                up(int(number[a][1]))
			for i in range(200) :
                                up(int(number[a][2]))
			for i in range(96) :
                                left(int(number[a][3]))
			for i in range(270) :
                                down(int(number[a][4]))
			for i in range(96) :
                                right(int(number[a][5]))
			for i in range(100) :
                                left(int(number[a][6]))
			for i in range(210) :
                                down(int(number[a][7]))
		elif ch=='q':
			press(0)
		elif ch=='e':
			press(1) 

		elif ch=='s':
			dc+=1
			print(dc)
			down(0)
			time.sleep(0.00)
		elif ch=='w':
			uc+=1
			print (uc)
			up(0)
			time.sleep(0.00)  
		elif ch=='a':
			lc+=1
			print(lc)
                        left(0)
                        time.sleep(0.00)
		elif ch=='d':
			rc+=1
			print(rc)
                        right(0)
                        time.sleep(0.00)
		elif ch==' ':
			press(0)
			time.sleep(0.1)
			press(1)
			
except KeyboardInterrupt:
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)	
	pwm.stop()
	GPIO.cleanup()
