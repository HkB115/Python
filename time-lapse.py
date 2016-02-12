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
try:
 wiringpi.wiringPiSetup()
 wiringpi=True
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

##### Camera Settings #####
camera.resolution=(1280,720)
camera.brightness=50
camera.contrast=0
camera.saturation=0
camera.sharpness=0
camera.ISO=800
camera.video_stabilization=False
camera.exposure_compensation=0
camera.exposure_mode='auto'
camera.meter_mode='average'
camera.awb_mode='auto'
camera.image_effect='none'
camera.color_effects=None
camera.hflip=False
camera.vflip=False
camera.rotation=0
camera.crop=(0.0, 0.0, 1.0, 1.0)
###########################

if(wiringpi!=True):
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
 YMD=datetime.date.today()
 ymd=YMD.isoformat()
 #hour = datetime.now().hour
 #minute = datetime.now().minute
 #second = datetime.now().second
 frame_num=str(frames).zfill(7)
 with camera as picamera.PiCamera:
  camera.capture("frame%s.jpg"%(frame_num))
  #os.system("raspistill -o frame%s.jpg"%(frame_num))
 frames+=1
 time.sleep(delay)
pin(led_pin,0)
os.system("avconv -r %s -i frame%s.jpg -r %s -vcodec libx264 -crf 20 -g 15 -vf crop=2592:1458,scale=1280:720 video.mp4"%(fps_in,'%7d',fps_out))
os.system("rm -f frame*")
