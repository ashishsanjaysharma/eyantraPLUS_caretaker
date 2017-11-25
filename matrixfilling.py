############################################
## Import OpenCV
import numpy as np
import cv2
# Initialize camera
cap = cv2.VideoCapture(0)
############################################
ret, frame = cap.read()
img =cv2.imread('output_image.png')
rowsp = 3 # rows for provison array
colsp = 3 # column for provison array
p=[]      # array for grid map
for row in xrange(rowsp): p += [[0]*colsp]
p=[(128,80,2),(128,232,3),(128,370,1)]


rowspt = 3 # rows for patient array
colspt = 3 # column for patient array
pt=[]      # array for grid map
for row in xrange(rowspt): pt += [[0]*colspt]
pt=[(529,80,1),(529,232,3),(529,370,2)]


rowsob = 8 # rows for obstacle array
colsob = 2 # column for provison array
ob=[]     # array for grid map
for row in xrange(rowsob): ob += [[0]*colsob]
ob=[(225,68),(225,187),(225,307),(225,417),(351,68),(351,187),(351,307),(351,417)]
#red=1
#yellow=2
#blue=3

############################################
## Video Loop
def fillmatrix(img):
    for i in range(0,3):
        for j in range(0,1):
            r=p[i][j]
            c=p[i][j+1]
            print r,c
            r,g,b=img[128][80]
            print r,g,b
       
fillmatrix(img)           
   

## Show the image


############################################

############################################
## Close and exit
cap.release()
cv2.destroyAllWindows()
############################################
