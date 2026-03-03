import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
grovepi.setText("")

full_angle = 1023
max_distance = 517

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)

    # TODO: read threshold from potentiometer
    analogval = grovepi.analogRead(potentiometer)
    thres = round(analogval / full_angle * max_distance)
    
    # TODO: format LCD text according to threshhold
    if (distance < thres):
      grovepi.setText(str(thres) + " cm     OBJ PRES")
    else:
      grovepi.setText(str(thres) + " cm")
    grovepi.setText("\n")
    grovepi.setText(str(distance) + " cm")
    time.sleep(1)
  except IOError:
    print("Error")