import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
#img = cv2.imread('output_image.png')
cv2.namedWindow('frame',cv2.CV_WINDOW_AUTOSIZE)
# Make the trackbar used for HSV masking    
cv2.createTrackbar('HSV1l','frame',0,179,nothing)

cv2.createTrackbar('HSV1u','frame',0,179,nothing)

cv2.createTrackbar('HSV2l','frame',0,255,nothing)

cv2.createTrackbar('HSV2u','frame',0,255,nothing)

cv2.createTrackbar('HSV3l','frame',0,255,nothing)

cv2.createTrackbar('HSV3u','frame',0,255,nothing)


while(True):

    # Make a window for the video feed  
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Make the trackbar used for HSV masking    
    i=cv2.getTrackbarPos('HSV1l','frame')
    
    # Name the variable used for mask bounds
    j = cv2.getTrackbarPos('HSV2l','frame')

    k=cv2.getTrackbarPos('HSV3l','frame')

    l=cv2.getTrackbarPos('HSV1u','frame')
    
    # Name the variable used for mask bounds
    m = cv2.getTrackbarPos('HSV2u','frame')

    n=cv2.getTrackbarPos('HSV3u','frame')

    
    
   
    # Convert BGR to HSV

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    # define range of color in HSV
    lower = np.array([i,j,k])
    upper = np.array([l,m,n])
    # Threshold the HSV image to get only selected color
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask the original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    #lower = np.array(param1)    ## Convert the parameters into a form that OpenCV can understand
    #upper = np.array(param2)
    mask1  = cv2.inRange(hsv, lower, upper)
    #res   = cv2.bitwise_and(frame, frame, mask= mask)
    ## Show the image
    #cv2.imshow('image',frame)
    #cv2.imshow('mask',mask1)
    #cv2.imshow('res',res)

    '''
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,0,(0,255,0),3)
   
    
    M = cv2.moments(contours[0])
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print "Centroid = ", cx, ", ", cy
    cv2.circle(frame,(cx,cy), 15, (100,100,255), -1)'''
    # Display the resulting frame
    cv2.imshow('frame',res)
    
    # Press q to quit
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
