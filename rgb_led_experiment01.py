#! /usr/bin/env python
import RPi.GPIO as GPIO
import sys
import time
 
# RGB LED configure pins
pinRed = 17
pinGreen = 27
pinBlue = 22
 
# GPIO setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
# Configure GPIO pins as output
GPIO.setup(pinRed, GPIO.OUT)
GPIO.setup(pinGreen, GPIO.OUT)
GPIO.setup(pinBlue, GPIO.OUT)
 
# Configure PWM 
RED = GPIO.PWM(pinRed, 1000)
GREEN = GPIO.PWM(pinGreen, 1000)
BLUE = GPIO.PWM(pinBlue, 1000)
RED.start(0)
GREEN.start(0)
BLUE.start(0)
 
redlevel = 0
t=0.2    

while (redlevel < 100):

    redlevel = redlevel + 10
    RED.ChangeDutyCycle(redlevel)
    print redlevel
    time.sleep(t)

time.sleep(t)
RED.stop()

greenlevel = 0

while (greenlevel < 100):

    greenlevel = greenlevel + 10
    GREEN.ChangeDutyCycle(greenlevel)
    print greenlevel
    time.sleep(t)

time.sleep(t)
GREEN.stop()

bluelevel = 0

while (bluelevel < 100):

    bluelevel = bluelevel + 10
    BLUE.ChangeDutyCycle(bluelevel)
    print bluelevel
    time.sleep(t)

time.sleep(t)

BLUE.stop()
 
GPIO.cleanup()
  



