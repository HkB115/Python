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
 print("[ERROR] Install package wiringpi2")
 exit(0)
try:
 wiringpi.wiringPiSetup()
except:
 print("[ERROR] Program must be run as root!")
 exit(0)
  
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
camera.contrast=0
camera.saturation=0
camera.sharpness=0
camera.ISO=0
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
led_array=True
frames_max=100
fps_in=10
fps_out=24
delay=6
####################

video_length=float(frames_max/fps_in)
frame_count=0
while frame_count<frames_max:
 if(led_array==True):
  pin(pin_red,1)
 else:
  pin(pin_red,0)
 YMD=datetime.date.today()
 ymd=YMD.isoformat()
 #hour = datetime.now().hour
 #minute = datetime.now().minute
 #second = datetime.now().second
 frame_num=str(frame_count).zfill(7)
 camera.capture("frame%s.jpg"%(frame_num))
 #os.system("raspistill -o frame%s.jpg"%(frame_num))
 frame_count+=1
 time.sleep(delay-6)
pin(pin_red,0)
os.system("avconv -r %s -i frame%s.jpg -r %s -vcodec libx264 -crf 20 -g 15 -vf crop=2592:1458,scale=1280:720 video.mp4"%(fps_in,'%7d',fps_out))
os.system("rm -f frame*")
camera.close()
