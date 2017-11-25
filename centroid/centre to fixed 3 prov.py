#Written by the pathos filled hack: C. Thomas Brittain

import cv2
import numpy as np
import threading
import math 
from math import atan2, degrees, pi 
import random


#Holds the frame index
global iFrame
iFrame = 0



while(1):
    #Create video capture
    cap = cv2.VideoCapture(0)
    
    #Globalizing variables
    global cxAvg  #<----I can't remember why...
    global cxFound 
    global iFrame 
    global intRx
    global rx
    global tranx
    
    #Flag for getting a new target.
    newTarget = "Yes"
    
    #Dot counter. He's a hungry hippo...
    dots = 0
    
    #This holds the bot's centroid X & Y average
    cxAvg = 0
    cyAvg = 0

    #Stores old position for movement assessment.
    xOld = 0
    yOld = 0
    

          
    while(1):
        

        
        #Incrementing frame index
        iFrame = iFrame + 1
            
        #Read the frames
        _,frame = cap.read()
    
        #Smooth it
        frame = cv2.blur(frame,(3,3))
    
        #Convert to hsv and find range of colors
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv,np.array((8, 60, 80)), np.array((25, 220, 160)))
        thresh2 = thresh.copy()
        
        #Find contours in the threshold image
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
        #Finding contour with maximum area and store it as best_cnt
        max_area = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > max_area:
                max_area = area
                best_cnt = cnt

        #Finding centroids of best_cnt and draw a circle there
        M = cv2.moments(best_cnt)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        cv2.circle(frame,(cx,cy),10,255,-1)
    
        #After 150 frames, it compares the bot's X and X average,
        #if they are the same + or - 5, it assumes the bot is being tracked.
        if iFrame >= 150:
            if cxAvg < (cx + 5) and cxAvg > (cx - 5):
                xOld == cxAvg
                stringXOk = "X Lock"
            if cyAvg < (cy + 5) and cyAvg > (cy - 5):
                yOld == cyAvg
                stringYOk = "Y Lock"          
            
        #This is finding the average of the X cordinate.  Used for establishing
        #a visual link with the robot.
        #X
        cxAvg = cxAvg + cx
        cxAvg = cxAvg / 2
        #Y
        cyAvg = cyAvg + cy
        cyAvg = cyAvg / 2
        
        #//Finding the Target Angle/////////////////////////////////////
        
        #Target cordinates.
        #Randomizing target.
        if newTarget == "Yes":
            tX = random.randrange(200, 400, 1)
            tY = random.randrange(150, 350, 1)
            newTarget = "No"
        
        if iFrame >= 170:
            if tX > cxAvg -45 and tX < cxAvg + 45:
                print "Made it through the X"
                if tY > cyAvg -45 and tY < cyAvg + 45:
                    print "Made it through the Y"
                    newTarget = "Yes"
                    dots=dots+1
        
        #Slope
        dx = cxAvg - tX
        dy = cyAvg - tY
        
        #Quad I -- Good
        if tX >= cxAvg and tY <= cyAvg:
            rads = atan2(dy,dx)
            degs = degrees(rads)
            degs = degs - 90
        #Quad II -- Good
        elif tX >= cxAvg and tY >= cyAvg:
            rads = atan2(dx,dy)
            degs = degrees(rads)
            degs = (degs * -1)
        #Quad III
        elif tX <= cxAvg and tY >= cyAvg:
            rads = atan2(dx,-dy)
            degs = degrees(rads)
            degs = degs + 180
            #degs = 3
        elif tX <= cxAvg and tY <= cyAvg:
            rads = atan2(dx,-dy)
            degs = degrees(rads) + 180
            #degs = 4
        
        #Convert float to int
        targetDegs = int(math.floor(degs))
        
        #Variable to print the degrees offset from target angle.
        strTargetDegs = " "
        
        #Put the target angle into a string to printed.
        strTargetDegs = str(math.floor(degs))
               
        #///End Finding Target Angle////////////////////////////////////


        #////////CV Dawing//////////////////////////////
        
        #Target circle
        cv2.circle(frame, (127, 232), 10, (0, 0, 255), thickness=-1)
        
        #ser.write(botXY)
        
        #Background for text.
        cv2.rectangle(frame, (18,2), (170,160), (255,255,255), -1)

        #Target angle.
        cv2.line(frame, (127,232), (cxAvg,cyAvg),(0,255,0), 1)
        cv2.line(frame, (128,80), (cxAvg,cyAvg),(0,255,0), 1)
        cv2.line(frame, (128,360), (cxAvg,cyAvg),(0,255,0), 1)
        cv2.line(frame, (cxAvg+30,cyAvg+60), (cxAvg,cyAvg),(0,0,255), 5)
        #Bot's X and Y is written to image
        #cv2.putText(frame,str(cx)+" cx, "+str(cy)+" cy",(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))

        print cx,cy

        #Bot's X and Y averages are written to image
        #cv2.putText(frame,str(cxAvg)+" cxA, "+str(cyAvg)+" cyA",(20,40),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))

        #"Ok" is written to the screen if the X&Y are close to X&Y Avg for several iterations.
        #cv2.putText(frame,stringXOk,(20,60),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
        #cv2.putText(frame,stringYOk,(20,80),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))


        
        #Dots eaten.
        #cv2.putText(frame,"Dots Ate: "+ str(dots),(20,140),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
                
        #After the frame has been modified to hell, show it.
        cv2.imshow('frame',frame) #Color image
        cv2.imshow('thresh',thresh2) #Black-n-White Threshold image
        
        #/// End CV Draw //////////////////////////////////////

        
        if cv2.waitKey(33)== 27:
            # Clean up everything before leaving
            cv2.destroyAllWindows()
            cap.release()
          
            break






