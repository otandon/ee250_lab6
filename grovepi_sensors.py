import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
grovepi.pinMode(ultrasonic_ranger,"INPUT")
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

full_angle = 1023.0
max_distance = 517.0

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)

    # TODO: read threshold from potentiometer
    analogval = grovepi.analogRead(potentiometer)
    print(analogval)
    thres = (float) ((analogval / full_angle) * max_distance)
    threshold = round(thres, 2)
    
    # TODO: format LCD text according to threshhold
    if (distance < thres):
      setText(str(threshold) + " cm OBJ PRES\n"+ str(distance) + " cm")
      # print(str(threshold) + " cm OBJ PRES\n"+ str(distance) + " cm")
    else:
      setText(str(threshold) + " cm\n" + str(distance) + " cm")
      # print(str(threshold) + " cm\n" + str(distance) + " cm")
    time.sleep(1)
  except IOError:
    print("Error")
