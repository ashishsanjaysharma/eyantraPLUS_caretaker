'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2014)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Functions
*  Filename: objectDetect.py
*  Version: 1.0.0  
*  Date: November 3, 2014
*  
*  Author: Arun Mukundan, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
'''

############################################
## Import OpenCV
import numpy as np
import cv2
# Initialize camera

############################################

# Sample Pixel --> A - [213,154,150] , B - [113,154,150]
param1 = [10,100,0]  #lower  pink  [100,0,0]  [255,255,255]
param2 = [255,255,255] # [10,100,0] [255,255,255]

############################################
## Video Loop
frame=cv2.imread('test_image1.png')
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
## Do the processing
lower = np.array(param1)    ## Convert the parameters into a form that OpenCV can understand
upper = np.array(param2)
mask  = cv2.inRange(hsv, lower, upper)
res   = cv2.bitwise_and(frame, frame, mask= mask)
## Show the image
#cv2.imshow('image',frame)
#cv2.imshow('mask',mask)
cv2.imshow('res',res)
    

## End the video loop
############################################

############################################
## Close and exit
cv2.waitKey(0);
cv2.destroyAllWindows()
############################################
