import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #alternative GPIO.BOARD

signal = 21

GPIO.setup(signal, GPIO.IN)

try:
    while 1: # True = 1
        val = GPIO.input(signal) # read FC-51 out pin
        print(val)
        time.sleep(0.5)
except KeyboardInterrupt:  # Stop program with Ctrl+C
    # clean up GPIO pint to ennsure that all inputs/outputs are reset
    print ("Setting all GPIO pins to default")
    GPIO.cleanup() #set all GPIO pint to default state
    print("exiting program")