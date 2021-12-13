import RPi.GPIO as GPIO
import time

# for 1st Motor on ENA
#ENA = 33
IN1 = 35
IN2 = 37
IN3 = 36
IN4 = 38

# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# initialize EnA, In1 and In2
#GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)



# Forward
def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(1)

# Stop
def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(1)
    

# Backward
def backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(1)
    
#left
def left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(1)
    
#RIGHT
def right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(1)

forward()
stop()
backward()
stop()
left()
stop()
right()
stop()
    

GPIO.cleanup()
