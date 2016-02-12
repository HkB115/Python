#!/usr/bin/python3
import os
import datetime, time
sleep=time.sleep
try:
 import picamera
except:
 print("[ERROR] Install package python3-picamera")
 exit(0)
try:
 import wiringpi2 as wiringpi
except:
 try:
  import wiringpi
 except:
  print("[WARN] WiringPi is required for LED functionality.")
try:
 wiringpi.wiringPiSetup()
except:
 print("[ERROR] Program must be run as root!")
 exit(0)
from PIL import Image

pin_red=0
pin_green=2
pin_blue=3
wiringpi.pinMode(pin_red, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(pin_green, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(pin_blue, wiringpi.GPIO.OUTPUT)
camera=picamera.PiCamera()
pin=wiringpi.digitalWrite

##### Settings #####
camera.brightness=50
camera.ISO=800
led_array=1
color_offset=25
delay=6
scan=True
trigger_threshold=2
####################

images=[]
while(scan):
 stream=io.BytesIO()
 with picamera.PiCamera() as comparator:
  comparator.resolution=(64,36)
  comparator.ISO=800
  comparator.capture(stream,format='jpeg')
 stream.seek(0)
 if(len(images)!=2):
  images.append(Image.open(stream))
 else:
  images[0]=Image.open(stream)
 diff=0
 if(len(images)!=1):
  x=0
  while(x<images[0].size[0]):
   y=0
   while(y<images[0].size[1]):
    img0=images[0].getpixel((x,y))
    val0=img0[0]+img0[1]+img0[2]
    img1=images[1].getpixel((x,y))
    val1=img1[0]+img1[1]+img1[2]
    if(abs(val1>val0)>color_offset):
     diff+=1
    y+=1
   x+=1
  change=(diff*100)/(images[0].size[0]*images[0].size[1])
  print(str(change)+"% changed.")
  if(change>trigger_threshold):
   if(led_array==True):
    pin(pin_red,1)
   else:
    pin(pin_red,0)
   with picamera.PiCamera() as comparator:
    camera.resolution=(1280,720)
    camera.brightness=50
    camera.ISO=800
    camera.capture(capture00000000,format='jpeg')
   pin(pin_red,0)
  images[1]=images[0]
