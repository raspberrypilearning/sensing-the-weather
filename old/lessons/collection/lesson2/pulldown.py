#!/usr/bin/python
import RPi.GPIO as GPIO
import time

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

while True:
    pin_value = GPIO.input(pin)
    print "HIGH" if pin_value else "LOW"
    time.sleep(0.5)
