#!/usr/bin/env python3
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import os, time

def button_callback(channel):
    print("Button was pushed!")
    os.system('mpg123 /home/pi/minute_courte.mp3 &')

def button_callback2(channel):
    print("Button was pushed!")
    os.system('mpg123  -g100 /home/pi/paw_patrol_courte.mp3 &')


os.system('mpg123  -g100 /home/pi/paw_patrol_courte.mp3 &')
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback,bouncetime=4000) # Setup event on pin 10 rising edge


GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(13,GPIO.RISING,callback=button_callback2,bouncetime=4000) # Setup event on pin 10 rising edge
while True:
    time.sleep(100000)
GPIO.cleanup() # Clean up
