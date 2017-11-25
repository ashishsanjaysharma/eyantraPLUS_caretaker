
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
import numpy as np
import cv2
############################################
def fun1(x,y):
    return(x+1,y);

def fun2(x,y):
    return(x,y+1);
'step 1 : take image'
############################################
## Read the image
img = cv2.imread('test_image1.png')


'''green = np.uint8([[[255,133,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green'''


############################################
'step 2 : green and pink dandi paramter '
paramg1 = [100,0,0]   #lower  pink
paramg2 = [255,255,255]     #upper

paramp1 = [10,100,0]   #lower orange
paramp2 = [255,255,255]   #upper

'step 3 : extract green '

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

## Do the processing
lowerg = np.array(paramg1)    ## Convert the parameters into a form that OpenCV can understand
upperg = np.array(paramg2)
maskg  = cv2.inRange(hsv, lowerg, upperg)
resg   = cv2.bitwise_and(img, img, mask= maskg)
## Show the image
#cv2.imshow('image',frame)
#cv2.imshow('maskg',maskg)
cv2.imshow('resg',resg)

'step 4 : extract pink '
#hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
## Do the processing
lowerp = np.array(paramp1)    ## Convert the parameters into a form that OpenCV can understand
upperp = np.array(paramp2)
maskp  = cv2.inRange(hsv, lowerp, upperp)
resp   = cv2.bitwise_and(img, img, mask= maskp)
## Show the image
#cv2.imshow('image',frame)
#cv2.imshow('maskp',maskp)
cv2.imshow('resp',resp)

'step 5 contour to green '

#grayg = cv2.cvtColor(resg,cv2.COLOR_BGR2GRAY)
resg,threshg = cv2.threshold(maskg,127,255,0)
contours, hierarchy = cv2.findContours(threshg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(threshg,contours,-1,(255,0,255),1)

Mg = cv2.moments(contours[-1])
cxg = int(Mg['m10']/Mg['m00'])
cyg = int(Mg['m01']/Mg['m00'])
print "Centroid for  pink end= ", cxg, ", ", cyg
cv2.circle(resg,(cxg,cyg), 3, (0,0,255), -1)


'step 6 contour to pink '

#grayp = cv2.cvtColor(resp,cv2.COLOR_BGR2GRAY)
resp,threshp = cv2.threshold(maskp,127,255,0)
contours, hierarchy = cv2.findContours(threshp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(threshp,contours,-1,(255,0,255),1)

Mp = cv2.moments(contours[-1])
cxp = int(Mp['m10']/Mp['m00'])
cyp = int(Mp['m01']/Mp['m00'])
print "Centroid for orange start = ", cxp, ", ", cyp
cv2.circle(resg,(cxp,cyp), 3, (0,0,255), -1)
d={}
m=1;
for j in xrange(m):
    for i in xrange(m):

        d[i] = fun1(i,j);
        # d[i+1]=fun2()
  









############################################
## Show the image
cv2.imshow('image',img)
############################################




############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
