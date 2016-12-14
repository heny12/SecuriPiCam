# This script is meant for the raspberry pi and uses the camera and PIR motion sensor
# module to create a basic motion activated security camera

import picamera
import io
import RPi.GPIO as GPIO
import time

# behavior preferences
output_path = '/home/pi/picam/'
no_motion_wait_time = 2
motion_pre_wait_time = 1
motion_post_wait_time = 10
gpio_input = 04

# set up motion sensor
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_input, GPIO.IN)

# set up camera
camera = picamera.PiCamera()
camera.vflip = True
camera.resolution = (1024, 768)


while True:
	input = GPIO.input(gpio_input)
	
	# no motion detected, check again in 2 seconds
	if input == 0:
		time.sleep(no_motion_wait_time)
	# motion detected, take a photo then check for motion again in 10 seconds
	if input == 1:
		time.sleep(motion_pre_wait_time)
		timestr = time.strftime("%Y%m%d-%H%M%S")
		camera.capture(output_path + timestr + '.jpg')
		time.sleep(motion_post_wait_time)

