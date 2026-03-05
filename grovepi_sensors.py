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
max_distance = 1023.0

adc_ref = 5
grove_vcc = 5


while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)

    # TODO: read threshold from potentiometer
    analogval = grovepi.analogRead(potentiometer)
    print(analogval)
    thres_temp = (float) ((analogval / full_angle) * max_distance)
    thres = (int) (thres_temp)
    
    # TODO: format LCD text according to threshhold
    if (distance < thres):
      text1 = str(thres) + "cm OBJ PRES"
      text1 = ('{: <16}'.format(text1))
      print(str(thres) + " cm OBJ PRES\n"+ str(distance) + " cm")
    else:
      text1 = str(thres) + " cm"
      text1 = ('{: <16}'.format(text1))
    
    text2 = str(distance) + " cm"
    text2 = ('{: <16}'.format(text2))
    setText_norefresh(text1 + "\n" + text2)
    print(text1 + "\n" + text2)
  except IOError:
    print("Error")
