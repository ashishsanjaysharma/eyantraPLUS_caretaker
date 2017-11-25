#Written by the pathos filled hack: C. Thomas Brittain

import cv2
import numpy as np

from time import sleep
import threading
import math 
from math import atan2, degrees, pi 
rowsp = 3 # rows for grid map array
colsp = 2 # column for grid map array

p=[]      # array for grid map

for row in xrange(rowsp): p += [[0]*colsp] # define array g with all element zero 
p=[(127,378),(127, 232),(127,92)]

global startl,startu

startl=(50,147,146)
startu=(90,187,186)

targetX=127
targetY=378
#Open COM port to tether the bot.
#ser = serial.Serial(port='COM14', baudrate = '9600')

#For getting information from the Arduino (tx was taken by Target X :P)



#Holds the frame index
global iFrame
iFrame = 0
global t
t=0

def maxItemLength(a):
        maxLen = 0
        rows = len(a)
        cols = len(a[0])
        for row in xrange(rows):
            for col in xrange(cols):
                maxLen = max(maxLen, len(str(a[row][col])))
        return maxLen


''' function to print array sytematically as specified in theor question '''

def printList(a):
        if (a == []):
            # So we don't crash accessing a[0]
            print []
            return
        rows = len(a)
        cols = len(a[0])
        fieldWidth = maxItemLength(a)
    
        print "[ ",
        for row in xrange(rows):
            if (row > 0): print "\n  ",
            print "[ ",
            for col in xrange(cols):
                if (col > 0): print ",",
                # The next 2 lines print a[row][col] with the given fieldWidth
                format = "%" + str(fieldWidth) + "s"
                print format % str(a[row][col]),
            print "]",
        print "]"

def OpenCV():
    #Create video capture
    cap = cv2.VideoCapture(0)
    
    #Globalizing variables
    global cxAvg  #<----I can't remember why...
    global cxFound 
    global iFrame 
    global intRx
    global rx
    global tranx
    global t #variable for maximum 
    
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
    
    #Clearing the serial send string.
    printRx = " "
          
    while(1):
        
        #"printRx" is separate in case I want to parse out other sensor data
        #from the bot
        #printRx = str(intRx)
        #Bot heading, unmodified
        #headingDeg = printRx
        #Making it a number so we can play with it.
        #intHeadingDeg = int(headingDeg)
       
        #headingDeg = str(intHeadingDeg)
            
        #Strings to hold the "Target Lock" status.     
        stringXOk = " "
        stringYOk = " "
        
        #Incrementing frame index
        iFrame = iFrame + 1
            
        #Read the frames
        _,frame = cap.read()
    
        #Smooth it
        frame = cv2.blur(frame,(3,3))
    
        #Convert to hsv and find range of colors
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv,np.array((50,147,146)), np.array((90,187,186)))#green
        thresh1 = cv2.inRange(hsv,np.array((1, 140, 165)), np.array((7, 190, 211))) #base
        thresh2 = thresh.copy()
        
        #Find contours in the threshold image
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        contours1,hierarchy1 = cv2.findContours(thresh1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        #Finding contour with maximum area and store it as best_cnt
        max_area = 0#green
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > max_area:
                max_area = area
                best_cnt = cnt

        max_area1 = 0 #orange
        for cnt1 in contours1:
            area1 = cv2.contourArea(cnt1)
            if area1 > max_area1:
                max_area1 = area1
                best_cnt1 = cnt1
        
        #Finding centroids of best_cnt and draw a circle there
        M = cv2.moments(best_cnt)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        cv2.circle(frame,(cx,cy),3,(36,173,89),-1)

        M1 = cv2.moments(best_cnt1)
        cx1,cy1 = int(M1['m10']/M1['m00']), int(M1['m01']/M1['m00'])
        cv2.circle(frame,(cx1,cy1),3,(200,84,56),-1)
        
        #After 150 frames, it compares the bot's X and X average,
        #if they are the same + or - 5, it assumes the bot is being tracked.
        if iFrame >= 25:
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
            #print tX,tY
            
            if t==0:
                tX=p[0][0]
                tY=p[0][1]
                t=1
            elif t<rowsp:
                
                tX=p[t][0]
                tY=p[t][1]
                t=t+1
                print tX,tY
            newTarget = "No"
        
        if iFrame >= 50:
            if tX > cxAvg -15 and tX < cxAvg + 15:
                print "Made it through the X"
                if tY > cyAvg -15 and tY < cyAvg + 15:
                    print "Made it through the Y"
                    newTarget = "Yes"
                    dots=dots+1

        dx1 = cx1 - cx
        dy1 = cy1 - cy
        rads1 = atan2(dy1,dx1)
        degs1 = degrees(rads1)
        degs1=180-degs1
        '''if degs1<0:
            degs1=180-degs1
        else:
            degs1=180-degs1'''
        degs1=int(math.floor(degs1))
        print cx,cy,cx1,cy1,degs1
        intHeadingDeg = degs1
        
        
        #Slope
        dx = cxAvg - tX
        dy = cyAvg - tY

        
        #q=abs(degs-degs1)
        
        #print q
           
        #Quad I -- Good
        if tX >= cxAvg and tY <= cyAvg:
            rads = atan2(dy,dx)
            degs = degrees(rads)
            degs=-degs 
          
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
        '''strTargetDegs = " "
        
        #Put the target angle into a string to printed.
        strTargetDegs = str(math.floor(degs))'''
        q=abs(targetDegs-degs1)       
        #///End Finding Target Angle////////////////////////////////////

        
        #//// Move Bot //////////////////////////////////////
        
        #targetDegs = Target angle
        #intHeadingDeg = Current Bot Angle
        
        #Don't start moving until things are ready.
        #Don't start moving until things are ready.
        if iFrame >= 160:
            #This compares the bot's heading with the target angle.  It must
            #be +-30 for the bot to move forward, otherwise it will turn.
            shortestAngle = targetDegs - intHeadingDeg
            
            if shortestAngle > 180:
                shortestAngle -= 360
            
            if shortestAngle < -180:
                shortestAngle += 360
            
            if shortestAngle <= 30 and shortestAngle >= -31:
                tranx = 3
                print "Forward"
            elif shortestAngle >= 1:
                tranx = 2
                print "Turn Right"
            elif shortestAngle < 1:
                tranx = 4
                print "Turn Left"
        
        #//// End Move Bot //////////////////////////////////
        
   
        
        
        #////////CV Dawing//////////////////////////////
        
        #Target circle
        cv2.circle(frame, (tX, tY), 10, (0, 0, 255), thickness=-1)
        
        #ser.write(botXY)
        
        #Background for text.
        cv2.rectangle(frame, (18,2), (170,160), (255,255,255), -1)

        #Target angle.
        cv2.line(frame, (tX,tY), (cxAvg,cyAvg),(0,255,0), 1)
        cv2.line(frame, (cx,cy), (cx1,cy1),(0,0,255), 1)
        #Bot's X and Y is written to image
        cv2.putText(frame,str(cx)+" cx, "+str(cy)+" cy",(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
        
        #Bot's X and Y averages are written to image
        cv2.putText(frame,str(cxAvg)+" cxA, "+str(cyAvg)+" cyA",(20,40),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))

        #"Ok" is written to the screen if the X&Y are close to X&Y Avg for several iterations.
        cv2.putText(frame,stringXOk,(20,60),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
        cv2.putText(frame,stringYOk,(20,80),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))

        #Print the compass to the frame.
        cv2.putText(frame,"Bot: "+str(degs1)+" Degs",(20,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
        cv2.putText(frame,"Target: "+str(targetDegs)+" Deg",(20,120),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
        cv2.putText(frame,"diff: "+str(q)+" Degs",(20,140),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
        #Dots eaten.
        #cv2.putText(frame,"Dots Ate: "+ str(dots),(20,140),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
                
        #After the frame has been modified to hell, show it.
        cv2.imshow('frame',frame) #Color image
        #cv2.imshow('thresh',thresh2) #Black-n-White Threshold image
        
        #/// End CV Draw //////////////////////////////////////

        
        if cv2.waitKey(33)== 27:
            # Clean up everything before leaving
            cv2.destroyAllWindows()
            cap.release()
            #Tell the robot to stop before quit.
            #ser.write("5") 
            #ser.close() # Closes the serial connection.
            break
'''
def rxtx():

    
    # Below 32 everything in ASCII is gibberish
    counter = 32
    
    #So the data can be passed to the OpenCV thread.
    global rx
    global intRx
    global tranx
    global motorDuration
    global motorBusy
    
    while(True):
        counter +=1
                  
        # Read the newest output from the Arduino
        #print tranx
        #ser.flushOutput()
        #This is for threading out the motor timer.  Allowing for control
        #over the motor burst duration.
        
            
            
             #Clear the buffer?
           
        #Delay one tenth of a second
        #sleep(.1)
                
        #This is supposed to take only the first three digits.
        
        #Reset counter if over 255.
        if counter == 255:
            counter = 32    


'''
#Threads OpenCV stuff.        
OpenCV = threading.Thread(target=OpenCV)
OpenCV.start()

#Threads the serial functions.
#rxtx = threading.Thread(target=rxtx)
#rxtx.start()




