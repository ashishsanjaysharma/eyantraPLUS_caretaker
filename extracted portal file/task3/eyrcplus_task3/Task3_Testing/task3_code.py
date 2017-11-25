############################################
## Import OpenCV
import numpy as np
import cv2
def get_perspective_image(frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lower = np.array([0, 0, 0]) #black color mask
    upper = np.array([120, 120, 120])
    mask = cv2.inRange(frame, lower, upper)
    
    ret,thresh1 = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,(0,255,0),3)
    biggest = 0
    max_area = 0
    min_size = thresh1.size/4
    index1 = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 10000:
            peri = cv2.arcLength(i,True)
        if area > max_area: 
            biggest = index1
            max_area = area
        index1 = index1 + 1
    approx = cv2.approxPolyDP(contours[biggest],0.05*peri,True)
    #drawing the biggest polyline
    cv2.polylines(frame, [approx], True, (0,255,0), 3)
    x1 = approx[0][0][0]
    y1 = approx[0][0][1]
    x2 = approx[1][0][0]
    y2 = approx[1][0][1]
    x3 = approx[3][0][0]
    y3 = approx[3][0][1]
    x4 = approx[2][0][0]
    y4 = approx[2][0][1]

    print x1, y1
    print x2, y2
    print x3, y3
    print x4, y4
    
    #points remapped from source image from camera
    #to cropped image try to match x1, y1,.... to the respective near values
    pts1 = np.float32([[x2,y2],[x4,y4],[x1,y1],[x3,y3]]) 
    pts2 = np.float32([[0,0],[0,480],[540,0],[540,480]])
    persM = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(frame,persM,(540,480))
    return dst



cap = cv2.VideoCapture(1)
ret, src = cap.read()
cv2.imshow('src', src)
cv2.imwrite("input_image.jpg", src)

##getting the perspective image
img_src= get_perspective_image(src)

cv2.imwrite("output_image.jpg", img_src)

cv2.imshow('dst', img_src)
cv2.waitKey(0)

## Close and exit
cap.release()
cv2.destroyAllWindows()
############################################
