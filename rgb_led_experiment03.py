#! /usr/bin/env python
import RPi.GPIO as GPIO
import sys
import time
 
# Set RGB LED pins
pinRed = 17
pinGreen = 27
pinBlue = 22
 
# GPIO setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
# Set GPIO pins as output
GPIO.setup(pinRed, GPIO.OUT)
GPIO.setup(pinGreen, GPIO.OUT)
GPIO.setup(pinBlue, GPIO.OUT)
 
# Use PWM
RED = GPIO.PWM(pinRed, 1000)
GREEN = GPIO.PWM(pinGreen, 1000)
BLUE = GPIO.PWM(pinBlue, 1000)
RED.start(0)
GREEN.start(0)
BLUE.start(0)

# t = time
t=0.5

#s = step
s=5

try:
    while True:

        redlevel = 100
        greenlevel = 0
        RED.ChangeDutyCycle(redlevel)
        time.sleep(t)
            
        while (greenlevel < 100):
               
            redlevel = redlevel -s
            greenlevel = greenlevel +s
            RED.ChangeDutyCycle(redlevel)
            GREEN.ChangeDutyCycle(greenlevel)
            time.sleep(t)

        RED.ChangeDutyCycle(0)

        greenlevel = 100
        bluelevel = 0
        GREEN.ChangeDutyCycle(greenlevel)
        time.sleep(t)
            
        while (bluelevel < 100):
               
            greenlevel = greenlevel -s
            bluelevel = bluelevel +s
            GREEN.ChangeDutyCycle(greenlevel)
            BLUE.ChangeDutyCycle(bluelevel)
            time.sleep(t)

        GREEN.ChangeDutyCycle(0)

        bluelevel = 100
        redlevel = 0
        BLUE.ChangeDutyCycle(bluelevel)
        time.sleep(t)
            
        while (redlevel < 100):
               
            bluelevel = bluelevel -s
            redlevel = redlevel +s
            BLUE.ChangeDutyCycle(bluelevel)
            RED.ChangeDutyCycle(redlevel)
            time.sleep(t)

        BLUE.ChangeDutyCycle(0)
    

except KeyboardInterrupt:
    GPIO.cleanup()
  



