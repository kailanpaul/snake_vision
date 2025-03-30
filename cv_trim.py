import cv2 as cv
import numpy as np
from picamera2 import Picamera2
import time 

camera = Picamera2()
camera.resolution = (640, 480)
camera.framerate = 32
# config = camera.create_preview_configuration({'format': 'BGR888'})
camera.start()

time.sleep(0.1)

while(1):
    img = camera.capture_array()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # img = cv.resize(img, (1000, 1000)) 
    blur = cv.medianBlur(img,5)

    ret, thresh = cv.threshold(blur,100,255,cv.THRESH_BINARY)

    contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv.contourArea(c)
        perimeter = cv.arcLength(c,True)
        
        if area>10000 and area<80000:
            M = cv.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.circle(img,(cx,cy),10,(255,255,255),-1)
            # cv.imshow('objects', img)
            print(f"Object pos (x,y):  ({cx},{cy})")

            if cx > (img.shape[1]/2):
                print("go right")
            else:
                print("go left")
