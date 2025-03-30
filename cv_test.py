import cv2 as cv
import numpy as np
import time
files = ['original.jpg']#, 'test2.jpg']

# cap = cv.VideoCapture("test.avi")

# while(True):
    # ret, frame = cap.read()
    # img = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

start = time.time()
    
for file in files:
    img = cv.imread(file, cv.IMREAD_GRAYSCALE)
    # assert img is not None, "file could not be read, check with os.path.exists()"
    img = cv.resize(img, (640, 480)) 
    # cv.imshow('image',img)
    # cv.imwrite('greyscale.jpg', img)
    cropped = img[100:380,:]
    # cv.imwrite('cropped.jpg', cropped)
    blur = cv.blur(cropped,(5,5))

    ret, thresh = cv.threshold(blur,250,255,cv.THRESH_BINARY)
    # img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
    # img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
    # cv.imwrite('threshold.jpg', thresh)

    # edges = cv.Canny(img,100,200,apertureSize=3)
    # cv.imshow('canny', edges)
    # cv.waitKey(0)

    contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    # img2 = img.copy()
    index = -1
    thickness = 4
    color = (0,0,0)
    cv.drawContours(cropped,contours,index,color,thickness)

    # cv.imwrite('contours.jpg', cropped)
    # cv.imshow('image',cropped)
    # cv.waitKey(0)


    # objects = img.copy()
    # objects = np.zeros([img.shape[0],img.shape[1],3],'uint8')

    for c in contours:
        area = cv.contourArea(c)
        perimeter = cv.arcLength(c,True)
        
        if area>10000 and area<80000:
            print(f"Area:{area}  Perimeter:{perimeter}")
            M = cv.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            # cv.circle(img,(cx,cy+100),10,(0,0,0),-1)
            # cv.imshow('objects', img)
            # cv.imwrite('objects.jpg', img)
            print(f"x pos:{cx}  y pos:{cy}")
            # print(img.shape[0])
            # print(img.shape[1])
            # cv.waitKey(0)
            if cx < (img.shape[1]/2):
                print("right")
            else:
                print("left")


    # cy = int(M['m01']/M['m00'])

    # cv.circle(objects, (cx,cy),4,(0,0,255),-1)



    # cv.imshow('objects', objects)
    # cv.waitKey(0)
    # cv.destroyAllWindows()


end = time.time()

print(end-start)

# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# ret, thresh = cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)
# cv2_imshow(thresh)




# edges = cv2.Canny(img,100,200,apertureSize=3)
# cv2_imshow(edges)





# edge_inv = 255 - edges

# #Use erosion to increase the size of the border
# kernal = np.ones((3,3),'uint8')
#   cy = int(M['m01']/M['m00'])
#   cv2.circle(objects,(cx,cy),4,(255,255,0),-1)

# cv2_imshow(objects)
# erode = cv2.erode(edge_inv,kernal,iterations=1)

# #Combine the two images
# final = cv2.bitwise_and(erode,thresh)

# #identify the contours
# contours,hierarchy = cv2.findContours(final, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# objects=img.copy()

# for c in contours:
#   area = cv2.contourArea(c)
# #If area is less than 300, it is a line segment.
#   if area<300:
#     continue
#   cv2.drawContours(objects,[c],-1,(255,255,255),1)
#   M=cv2.moments(c)
#   cx = int(M['m10']/M['m00'])
#   cy = int(M['m01']/M['m00'])
#   cv2.circle(objects,(cx,cy),4,(255,255,0),-1)

# cv2_imshow(objects)





