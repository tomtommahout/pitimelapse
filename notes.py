camera.resolution = (3280, 2464) #maximum resolution v2cam
camera.framerate = 15 #Required to set maximum resolution
camera.start_preview()
sleep(5)  #Allow time to adjust for brightness
camera.capture('/home/pi/Desktop/Lapse/image.jpg')
camera.stop_preview()



# Closes camera between shots
import picamera
import time

for i in range(60):
    with picamera.PiCamera() as camera:
        camera.resolution = (3280, 2464)
        time.sleep(2) # Camera warm-up time
        filename = 'img{timestamp:%Y-%m-%d-%H-%M}.jpg'
        camera.capture(filename)
        print('Captured %s' % filename)
    # Capture one image a minute
    time.sleep(59)
    
    
    
    
#shots on the hour
from time import sleep
from picamera import PiCamera
from datetime import datetime, timedelta

def wait():
    # Calculate the delay to the start of the next hour
    next_hour = (datetime.now() + timedelta(hour=1)).replace(
        minute=0, second=0, microsecond=0)
    delay = (next_hour - datetime.now()).seconds
    sleep(delay)

camera = PiCamera()
camera.start_preview()
wait()
for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    wait()
