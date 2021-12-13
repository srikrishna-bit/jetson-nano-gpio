import RPi.GPIO as GPIO
import time

class Robot:
    def __init__(self):
        self.IN1=35
        self.IN2=37
        self.IN3=36
        self.IN4=38
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW)
       
    def forward(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        time.sleep(1)
       
    def backward(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        time.sleep(1)
       
    def left(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        time.sleep(1)
       
    def right(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        time.sleep(1)
   
    def stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        time.sleep(1)
       
GPIO.cleanup()      