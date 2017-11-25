# -*- coding: cp1252 -*-
'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2014)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Functions
*  Filename: contourVid.py
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
cap = cv2.VideoCapture(0)
############################################
scale_down = 1
############################################
## Video Loop
while(1):
    ## Read the image
    ret, frame = cap.read()
    
    ## Do the processing
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((67,169,107)), np.array((107,209,147)))#green
    gray = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,100,255,0)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    max_area = 0
    largest_contour = None
    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        '''if area > max_area:
          max_area = area
          largest_contour = contour
    if not largest_contour == None:'''
        largest_contour = contour

        moment = cv2.moments(largest_contour)
	
	
        if moment["m00"] > 1000 / scale_down:
              #rect = cv2.minAreaRect(largest_contour)
              #rect = ((rect[0][0] * scale_down, rect[0][1] * scale_down), (rect[1][0] * scale_down, rect[1][1] * scale_down), rect[2])
              #box = cv2.cv.BoxPoints(rect)
              #box = np.int0(box)
              #cv2.drawContours(frame,[box], 0, (0, 0, 255), 2)
              cx,cy = int(moment['m10']/moment['m00']), int(moment['m01']/moment['m00'])
              cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

    
    

    '''    
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,255,0),3)
    M = cv2.moments(contours[-1])
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print "Centroid = ", cx, ", ", cy
    cv2.circle(frame,(cx,cy), 3, (0,0,255), -1)'''
    ## Show the image
    cv2.imshow('image',frame)

    ## End the video loop
    if cv2.waitKey(1) == 27:  ## 27 - ASCII for escape key
        break
############################################

############################################
## Close and exit
cap.release()
cv2.destroyAllWindows()
############################################
