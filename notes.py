camera.resolution = (3280, 2464) #maximum resolution v2cam
camera.framerate = 15 #Required to set maximum resolution
camera.start_preview()
sleep(5)  #Allow time to adjust for brightness
camera.capture('/home/pi/Desktop/Lapse/image.jpg')
camera.stop_preview()
