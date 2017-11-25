import numpy as np
import cv2
# Initialize camera
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

#red=1
#yellow=2
#blue=3


rowsp = 3 # rows for provison array
colsp = 3 # column for provison array
p=[]      # array for grid map
for row in xrange(rowsp): p += [[0]*colsp]
p=[(128,80,2),(128,232,3),(128,370,1)]


rowsb = 3 # rows for bed array
colsb = 3 # column for bed array
b=[]      # array for grid map
for row in xrange(rowsb): b += [[0]*colsb]
b=[(529,80,1),(529,232,3),(529,370,2)]


rowsob = 8 # rows for obstacle array
colsob = 3 # column for provison array
ob=[]     # array for grid map
for row in xrange(rowsob): ob += [[0]*colsob]
ob=[(225,68,1),(225,187,0),(225,307,1),(225,417,0),(351,68,1),(351,187,0),(351,307,1),(351,417,0)]


rowsspos = 3 # rows for grid map array
colsspos = 2 # column for grid map array
spos=[]      # array for grid map
for row in xrange(rowsspos): spos += [[0]*colsspos] # define array g with all element zero 
spos=[(288,77),(288,246),(288,403)]

rowst = 15 # rows for grid map array
colst = 2 # column for grid map array
t=[]      # array for grid map
for row in xrange(rowst): t += [[0]*colst] # define array g with all element zero 



global b1,b2,b3,p1,p2,p3
global d1,d2,d3,d4,d5,d6,d7,d8,dcat1,dcat2
global d1f,d2f,d3f,d4f
global p1count,p2count,p3count
global next_target1,next_target2,next_target3
p1count=0
p2count=0
p3count=0
d1f=0
d2f=0
d3f=0
d4f=0
'''next_target1=0
next_target2=0
next_target3=0'''

def bed_color_pos():
    global b1,b2,b3
    b1=b[0][2]
    b2=b[1][2]
    b3=b[2][2]

def provsn_color_pos():
    global p1,p2,p3
    p1=p[0][2]
    p2=p[1][2]
    p3=p[2][2]        

def obstacle_location():
    global d1,d2,d3,d4,d5,d6,d7,d8,dcat1,dcat2
    d1=ob[0][2]
    d2=ob[1][2]
    d3=ob[2][2]
    d4=ob[3][2]
    d5=ob[4][2]
    d6=ob[5][2]
    d7=ob[6][2]
    d8=ob[7][2]
    dcat1 = str(d1)+str(d2)+str(d3)+str(d4)
    dcat2 = str(d5)+str(d6)+str(d7)+str(d8)


def getmatch():
    global p1count,p2count,p3count
   
    
    if(b1==p1):
        p1count=p1count+1
    elif(b1==p2):
        p2count=p2count+1
    else:
        p3count=p3count+1

    if(b2==p1):
        p1count=p1count+1
    elif(b2==p2):
        p2count=p2count+1
    else:
        p3count=p3count+1

    if(b3==p1):
        p1count=p1count+1
    elif(b3==p2):
        p2count=p2count+1
    else:
        p3count=p3count+1
        

def getfirsttarget(dcat):
    global d1f,d2f,d3f,d4f

    if(dcat=="1100"):
        d3f=1
        return (spos[1][0],ob[2][1])
    elif(dcat=="1010"):
        d2f=1
        return (spos[1][0],ob[1][1])
    elif(dcat=="1001"):
        dmiddle=1
        return (ob[1][0],spos[1][1])
    elif(dcat=="0101"):
        d3f=1
        return (spos[1][0],ob[2][1])
    elif(dcat=="0011"):
        d2f=1
        print '11'
        return (spos[1][0],ob[1][1])
    elif(dcat=="0110"):
        if(botangle<180):
            d1f=1
            return (spos[1][0],ob[0][1])
        else:
            d4f=1
            return (spos[2][0],ob[3][1])
    

def turn90():
    #ser.write('a')
    a=1
    
def move2d():
    global d1f,d2f,d3f,d4f
    if(d1f==1):
        return (ob[0][0], ob[0][1])
    elif(d2f==1):
        return (ob[1][0], ob[1][1])
    elif(d3f==1):
        return (ob[2][0], ob[2][1])
    elif(d4f==1):
        return (ob[3][0], ob[3][1])


def go_for_prov():
    global d1f,d2f,d3f,d4f
    global p1count,p2count,p3count
    global next_target1,next_target2,next_target3
    
    if(d1f==1):
        if(p1count==0 and p2count>0):
            next_target1= (p[1][0],p[1][1])#p2
            next_target2= (p[2][0],p[2][1])#p3
            if(d2==1 and d3==1 and d4==0):           
                next_target3=(ob[3][0],ob[3][1])#d4
            if(d2==0 and d3==1 and d4==1):
                next_target3=(ob[1][0],ob[1][1])#d2
            if(d2==1 and d3==0 and d4==1):
                next_target3=(ob[2][0],ob[2][1])#d3
                
        elif(p1count>0 and p2count==0):
            
            next_target1=(p[0][0],p[0][1])#p1
            next_target2=(p[2][0],p[2][1])#p3
            if(d2==1 and d3==1 and d4==0):           
                next_target3=(ob[3][0],ob[3][1])#d4
            if(d2==0 and d3==1 and d4==1):
                next_target3=(ob[1][0],ob[1][1])#d2
            if(d2==1 and d3==0 and d4==1):
                next_target3=(ob[2][0],ob[2][1])#d3
                
        elif(p1count>0 and p2count>0):
                
            next_target1=(p[0][0],p[0][1])#p1
            next_target2=(p[1][0],p[1][1])#p2
            if(d2==1 and d3==1 and d4==0):
                next_target3=(ob[3][0],ob[3][1])#d4
            if(d2==0 and d3==1 and d4==1):
                next_target3=(ob[1][0],ob[1][1])#d2
            if(d2==1 and d3==0 and d4==1):
                next_target3=(ob[2][0],ob[2][1])#d3

    if(d2f==1):
        if(p2count>0 and p1count==0):
            next_target1= (p[1][0],p[1][1])#p2
            next_target2= (p[2][0],p[2][1])#p3
            if(d1==1 and d3==1 and d4==0):
                next_target3=(ob[3][0],ob[3][1])#d4
            if(d1==0 and d3==1 and d4==1):
                next_target3=(ob[0][0],ob[0][1])#d1
            if(d1==1 and d3==0 and d4==1):
                next_target3=(ob[2][0],ob[2][1])#d3
                
        elif(p1count>0 and p2count==0):
            next_target1=(p[0][0],p[0][1])#p1
            next_target2=(p[2][0],p[2][1])#p3
            if(d1==1 and d3==1 and d4==0):
                next_target3=(ob[3][0],ob[3][1])#d4
            if(d1==0 and d3==1 and d4==1):
                next_target3=(ob[0][0],ob[0][1])#d1
            if(d1==1 and d3==0 and d4==1):
                next_target3=(ob[2][0],ob[2][1])#d3
                
        elif(p1count>0 and p2count>0):
            if(d1==1 and d3==1 and d4==0):
                next_target1=(p[0][0],p[0][1])#p1
                next_target2=(p[1][0],p[1][1])#p2
                next_target3=(ob[3][0],ob[3][1])#d4
            if(d1==0 and d3==1 and d4==1):
                next_target1=(p[1][0],p[1][1])#p2
                next_target2=(p[0][0],p[0][1])#p1
                next_target3=(ob[0][0],ob[0][1])#d1
            if(d1==1 and d3==0 and d4==1):
                next_target1=(p[0][0],p[0][1])#p1
                next_target2=(p[1][0],p[1][1])#p2
                next_target3=(ob[2][0],ob[2][1])#d3

    if(d3f==1):
        
        if(p2count>0 and p3count==0):
            next_target1= (p[1][0],p[1][1])#p2
            next_target2= (p[0][0],p[0][1])#p1
            if(d1==1 and d2==1 and d4==0):
                next_target3=(ob[3][0],ob[3][1])#d4
            if(d1==0 and d2==1 and d4==1): 
                next_target3=(ob[0][0],ob[0][1])#d1
            if(d1==1 and d2==0 and d4==1):   
                next_target3=(ob[1][0],ob[1][1])#d2
            
        elif(p3count>0 and p2count==0):
            next_target1=(p[2][0],p[2][1])#p3
            next_target2=(p[0][0],p[0][1])#p1
            if(d1==1 and d2==1 and d4==0):
                next_target3=(ob[3][0],ob[3][1])#d4
            if(d1==0 and d2==1 and d4==1):
                next_target3=(ob[0][0],ob[0][1])#d1
            if(d1==1 and d2==0 and d4==1):
                next_target3=(ob[1][0],ob[1][1])#d2
            
        elif(p2count>0 and p3count>0):
            
            if(d1==1 and d2==1 and d4==0):
                print '6'
                next_target1=(p[1][0],p[1][1])#p2
                next_target2=(p[2][0],p[2][1])#p3
                next_target3=(ob[3][0],ob[3][1])#d4
                print '5'
            if(d1==0 and d2==1 and d4==1):
                next_target1=(p[2][0],p[2][1])#p3
                next_target2=(p[1][0],p[1][1])#p2
                next_target3=(ob[0][0],ob[0][1])#d1
            if(d1==1 and d2==0 and d4==1):
                next_target1=(p[2][0],p[2][1])#p3
                next_target2=(p[1][0],p[1][1])#p2
                next_target3=(ob[1][0],ob[1][1])#d2

    if(d4f==1):
        if(p2count>0 and p3count==0):
            next_target1= (p[1][0],p[1][1])#p2
            next_target2= (p[0][0],p[0][1])#p1
            if(d1==1 and d2==1 and d3==0):
                next_target3=(ob[2][0],ob[2][1])#d3
            if(d1==0 and d2==1 and d3==1):
                next_target3=(ob[0][0],ob[0][1])#d1
            if(d1==1 and d2==0 and d3==1):
                next_target3=(ob[1][0],ob[1][1])#d2
                    
        elif(p3count>0 and p2count==0):
            next_target1=(p[2][0],p[2][1])#p3
            next_target2=(p[0][0],p[0][1])#p1
            if(d1==1 and d2==1 and d3==0):
                next_target3=(ob[2][0],ob[2][1])#d3
            if(d1==0 and d2==1 and d3==1):
                next_target3=(ob[0][0],ob[0][1])#d1
            if(d1==1 and d2==0 and d3==1):
                next_target3=(ob[1][0],ob[1][1])#d2
        elif(p2count>0 and p3count>0):
            next_target1=(p[2][0],p[2][1])#p3
            next_target2=(p[1][0],p[1][1])#p2
            if(d1==1 and d2==1 and d3==0):
                next_target3=(ob[2][0],ob[2][1])#d3
            if(d1==0 and d2==1 and d3==1):
                next_target3=(ob[0][0],ob[0][1])#d1
            if(d1==1 and d2==0 and d3==1):
                next_target3=(ob[1][0],ob[1][1])#d2
        
        

                
                    
                    
                    
                
                    
                
                

    '''
    if(df3==1 or df4==1):
        if(p2count==0 and p3count>0):
            next_target= p[1][0],p[1][1]
        elif(p2count>0 and p3count==0):
            next_target=p[0][0],p[0][1]#
            elif(p2count>0 and p3count>0):
                if(df4==1):
                    next_target= p[1][0],p[1][1]
                else:
    '''

    


    
                
bed_color_pos()
provsn_color_pos()
obstacle_location()
print d1,d2,d3,d4
getmatch()
print p1count,p2count,p3count
print getfirsttarget(str(d1)+str(d2)+str(d3)+str(d4))
print d1f,d2f,d3f,d4f
print move2d()
go_for_prov()
print next_target1,next_target2,next_target3






    
        

    






















                  
 
############################################
## Close and exit
cap.release()
cv2.destroyAllWindows()
############################################
