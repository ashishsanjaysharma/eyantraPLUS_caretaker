'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2014)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Functions
*  Filename: contourImage.py
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
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('test_image1.png')

############################################

############################################
## Do the processing
# Need a binary Image
a=10;
x,y,c= img.shape;
print x;
print y;

m=x/a;
n=y/a;

'''for i in range(0,400):
    cv2.line(img,(i,0),(i,400),(255,0,0),1)
'''
p = 0
while p<y:
    cv2.line(img,(p,0),(p,400),(0,0,255),2)
    cv2.line(img,(0,p),(400,p),(0,0,255),2)
    p += m
############################################

############################################
## Show the image
cv2.imshow('image',img)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
