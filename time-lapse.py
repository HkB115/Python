#!/usr/bin/python
from datetime import date
from os import system
from time import sleep
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
  wiringpi_installed=False
try:
 wiringpi.wiringPiSetup()
 wiringpi_installed=True
except:
 print("[WARN] WiringPi is required for LED functionality.")

##### Settings #####
delay=5 # Default: 5. Minimum delay between camera triggers in seconds
led_array=True # Enable the LEDBorg module to activate when the camera takes a picture
led_color='red' # Default: 'red'. Choices: 'red', 'green', or 'blue'
frames_max=100
fps_in=10
fps_out=24
####################

if(not(wiringpi_installed)):
 led_array=False
if(led_array):
 if(led_color=='red'):
  led_pin=0
 elif(led_color=='green'):
  led_pin=2
 elif(led_color=='blue'):
  led_pin=3
 else:
  led_pin=0
 wiringpi.pinMode(led_pin, wiringpi.GPIO.OUTPUT)
 pin=wiringpi.digitalWrite
else:
 led_array=False

video_length=float(frames_max/fps_in)
frames=0
while frames<frames_max:
 if(led_array):
  pin(led_pin,1)
 else:
  pin(led_pin,0)
 YMD=date.today()
 ymd=YMD.isoformat()
 frame_num=str(frames).zfill(7)
 with camera as picamera.PiCamera:
  camera.resolution=(1280,720)
  camera.brightness=50
  camera.ISO=800
  camera.capture("frame%s.jpg"%(frame_num))
  #os.system("raspistill -o frame%s.jpg"%(frame_num))
 frames+=1
 sleep(delay)
pin(led_pin,0)
system("avconv -r %s -i frame%s.jpg -r %s -vcodec libx264 -crf 20 -g 15 -vf crop=2592:1458,scale=1280:720 video.mp4"%(fps_in,'%7d',fps_out))
system("rm -f frame*")
