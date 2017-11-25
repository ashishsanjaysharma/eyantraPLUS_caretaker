'''
        team eYRCPlus #75

function :
1. maxItemLength of item of an array
2. print2dlist : print 2-dimensional array systematically row and columnwise
3. Play : give route and shortest path
4. grid_map() : give grid map of image in form of '1's and '0's
                -2: for origin
                -1: for obscatles
                 0: for navigable path 
5. scan() : this scan grid map and add points with count in array 'a' , for eg. count=0 for scan zero and so on
6. send_co_rdinates() : fetch all points added in array ' a' and pass each points to add_count()
7. fun(x,y) : pad required number aside four co-ordinates
             for eg. if fun(5,6) then add certain number aside (4,6),(7,6),(5,5),(5,7) in grid map array only if there  obatined by spacemap()
8. startone(x,y): Add '1' aside start point to start with mapping process
9. def fun3(x,y): Backtrace shortest path from end and add points to array ' m '


LOGIC :

1. take image
2. make grid map
                -2: for origin
                -1: for obscatles
                 0: for navigable path 

 for eg. count=0
 [  [   0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ] 
   [   0 ,  0 , -1 , -1 ,  0 ,  0 , -1 ,  0 ,  0 ,  0 ] 
   [   0 ,  0 , -1 ,  0 ,  0 , -1 , -1 ,  0 ,  0 ,  0 ] 
   [   0 , -1 , -1 ,  0 ,  0 ,  0 ,  0 ,  0 , -1 , -1 ]    
   [   0 ,  0 ,  0 ,  0 , -2 ,  0 , -1 ,  0 ,  0 ,  0 ] 
   [   0 , -1 , -1 ,  0 ,  0 ,  0 , -1 , -1 , -1 ,  0 ] 
   [   0 ,  0 , -1 , -1 ,  0 , -1 , -1 ,  0 ,  0 ,  0 ] 
   [   0 ,  0 ,  0 ,  0 ,  0 , -1 ,  0 ,  0 ,  0 ,  0 ] 
   [   0 , -1 , -1 , -1 ,  0 ,  0 ,  0 , -1 ,  0 ,  0 ] 
   [   0 ,  0 ,  0 , -1 ,  0 ,  0 ,  0 , -1 ,  0 ,  0 ] ]

array a= [(5,4),(5,6),(4,5),(6,5)] because scan() search for count+1 i.e here'1' and add to array 'a'

3. add count='1' aside -2 i.e origin as all points are at distance 1

 for eg.
 [  [   0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ] 
   [   0 ,  0 , -1 , -1 ,  0 ,  0 , -1 ,  0 ,  0 ,  0 ] 
   [   0 ,  0 , -1 ,  0 ,  0 , -1 , -1 ,  0 ,  0 ,  0 ] 
   [   0 , -1 , -1 ,  0 ,  1 ,  0 ,  0 ,  0 , -1 , -1 ]    
   [   0 ,  0 ,  0 ,  1 , -2 ,  1 , -1 ,  0 ,  0 ,  0 ] 
   [   0 , -1 , -1 ,  0 ,  1 ,  0 , -1 , -1 , -1 ,  0 ] 
   [   0 ,  0 , -1 , -1 ,  0 , -1 , -1 ,  0 ,  0 ,  0 ] 
   [   0 ,  0 ,  0 ,  0 ,  0 , -1 ,  0 ,  0 ,  0 ,  0 ] 
   [   0 , -1 , -1 , -1 ,  0 ,  0 ,  0 , -1 ,  0 ,  0 ] 
   [   0 ,  0 ,  0 , -1 ,  0 ,  0 ,  0 , -1 ,  0 ,  0 ] ]

   

4.  add count='2' aside 1 i.e origin as all points are at distance 1

[  [   0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ] 
   [   0 ,  0 , -1 , -1 ,  0 ,  0 , -1 ,  0 ,  0 ,  0 ] 
   [   0 ,  0 , -1 ,  0 ,  2 , -1 , -1 ,  0 ,  0 ,  0 ] 
   [   0 , -1 , -1 ,  2 ,  1 ,  2 ,  0 ,  0 , -1 , -1 ] 
   [   0 ,  0 ,  2 ,  1 , -2 ,  1 , -1 ,  0 ,  0 ,  0 ] 
   [   0 , -1 , -1 ,  2 ,  1 ,  0 , -1 , -1 , -1 ,  0 ] 
   [   0 ,  0 , -1 , -1 ,  0 , -1 , -1 ,  0 ,  0 ,  0 ] 
   [   0 ,  0 ,  0 ,  0 ,  0 , -1 ,  0 ,  0 ,  0 ,  0 ] 
   [   0 , -1 , -1 , -1 ,  0 ,  0 ,  0 , -1 ,  0 ,  0 ] 
   [   0 ,  0 ,  0 , -1 ,  0 ,  0 ,  0 , -1 ,  0 ,  0 ] ]

5. keep doing this until you get end point and grid look kike this, highest value -1 = shortest path

[  [   0 ,  0 ,  0 ,  0 ,  4 ,  5 ,  0 ,  7 ,  8 ,  9 ] 
   [   0 ,  0 , -1 , -1 ,  3 ,  4 , -1 ,  6 ,  7 ,  8 ] 
   [   0 ,  0 , -1 ,  3 ,  2 , -1 , -1 ,  5 ,  6 ,  7 ] 
   [   0 , -1 , -1 ,  2 ,  1 ,  2 ,  3 ,  4 , -1 , -1 ] 
   [   4 ,  3 ,  2 ,  1 , -2 ,  1 , -1 ,  5 ,  6 ,  7 ] 
   [   0 , -1 , -1 ,  2 ,  1 ,  2 , -1 , -1 , -1 ,  8 ] 
   [   8 ,  7 , -1 , -1 ,  2 , -1 , -1 ,  9 , 10 ,  9 ] 
   [   7 ,  6 ,  5 ,  4 ,  3 , -1 ,  7 ,  8 ,  9 , 10 ] 
   [   0 , -1 , -1 , -1 ,  4 ,  5 ,  6 , -1 , 10 , 11 ] 
   [   0 ,  0 ,  0 , -1 ,  5 ,  6 ,  7 , -1 , 11 ,  0 ] ]

6. Keep doing this until you get final grid map
7. once done track end point and search for count-1 aside end point and keep tracing until you get start point
8. Reverse that array and print 

'''

import numpy as np
import cv2
end=0        #variable to decide whether 'end' point reached

'''           maxItemLength of item of an array        '''

def maxItemLength(a):
        maxLen = 0
        rows = len(a)
        cols = len(a[0])
        for row in xrange(rows):
            for col in xrange(cols):
                maxLen = max(maxLen, len(str(a[row][col])))
        return maxLen

'''           maxItemLength of item of an array           '''

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






'               Play : give route and shortest path               '

def play(img):

    img = img
    
    count=1
    start=0
    end=0
    global i
    i=0
    x=0
    cxg=0
    cyg=0
    
    rows = 10 # rows for grid map array
    cols = 10 # column for grid map array
    g=[]      # array for grid map
    
    for row in xrange(rows): g += [[0]*cols] # define array g with all element zero



    rows1 = 20 # rows for grid map array
    cols1 = 2
    a=[]# column for grid map array
    for row1 in xrange(rows1): a += [[0]*cols1]


    rows1 = 20 # rows for grid map array
    cols1 = 2
    m=[]
    for row1 in xrange(rows1): m += [[0]*cols1]
    

    '''  grid_map() : give grid map of image in form of '1's and '0's
                -2: for origin
                -1: for obscatles
                 0: for navigable path  '''
    
    def grid_map(img):
        x,y,z= img.shape; # get size of image
        n=10             
        m=x/n;            # divide pixel value by 10 to scale x corodinate and store value of pixel in array 'g'
        n=y/n;            # divide pixel value by 10 to scale y corodinate and store value of pixel in array 'g'
    
        p = 20;           # start from centroid of first grid i.e (20,20) therefore initialize p=20 and q=20
        while p<x:
            q = 20;
            while q<y:
                if p<400 and q<400:
                        b,c,d=img[p][q]; # get RGB value of image
                    
                        if b>240 or c>240 or d>240: # check RGB value ,if white then assign '0' else '1'
                          g[p/40][q/40]=0;
                       
                        else:
                          g[p/40][q/40]=-1;
                q=q+40;
          
            p=p+40;
    
        return g;       



    '''  fun(x,y) : pad required number aside four co-ordinates
             for eg. if fun(5,6) then add certain number aside (4,6),(7,6),(5,5),(5,7) in grid map array only if there is navigable path and not origin or obstacles obatined by spacemap() '''
    
    def add_count(x,y):
        
        count1=count;
        if x==cyg and y==cxg:
            end=1
           
        if (x+1<10 and (g[x+1][y]==0)  and (g[x+1][y]!=-1)  and x>=0 and y>=0 and g[x+1][y]!=-2):
            g[x+1][y]=count1;
            
        if (g[x-1][y]==0 and (g[x-1][y]!=-1)  and x>=0 and y>=0 and g[x-1][y]!=-2):
            g[x-1][y]=count1;
        
        if (y+1<10 and g[x][y+1]==0  and (g[x][y+1]!=-1) and x>=0 and y>=0 and g[x][y+1]!=-2):
            g[x][y+1]=count1;
        
        if (g[x][y-1]==0 and (g[x][y-1]!=-1)  and x>=0 and y>=0  and g[x][y-1]!=-2):
            g[x][y-1]=count1;
        
    
    ''' scan() : this scan grid map and add points with count in array 'a' , for eg. count=0 for scan zero and so on  '''
    def scan():
        p = 0;
        i=0
   
        while p<=9:
            q = 0;
            while q<=9:
                if (g[p][q]==count):
                         a[i][0]=p
                         a[i][1]=q
                         if a[i][0]==cyg and a[i][1]==cxg:
                             global end
                             end=1
                             
                         i+=1
                     
                q=q+1;
            p=p+1;
    
        return end
    
    
    '''  send_co_rdinates() : fetch all points added in array ' a' and pass each points to add_count() '''
    
    def send_co_rdinates():
    
        count2=20
        for x in range(0,count2):
            if(a[x][0]!=0 and a[x][1]!=0):
                add_count(a[x][0],a[x][1]);
        
    
    ''' startone(x,y): Add '1' aside start point to start with mapping process  '''
    
    def startone(x,y):
            count1=count;
    
        
            if ((g[x+1][y]==0)  and x>=0 and y>=0):
                g[x+1][y]=count;
                a[0][0]=x+1
                a[0][1]=y
            
            if ((g[x-1][y]==0) and x>=0 and y>=0):
                g[x-1][y]=count;
                a[1][0]=x-1
                a[1][1]=y
            
            if ((g[x][y+1]==0) and  x>=0 and y>=0):
       
                g[x][y+1]=count;
                a[2][0]=x
                a[2][1]=y+1
            
            if ((g[x][y-1]==0) and  x>=0 and y>=0):
      
                g[x][y-1]=count;
                a[3][0]=x
                a[3][1]=y-1

    '''  def fun3(x,y): Backtrace shortest path from end and add points to array ' m '  '''
    
    def fun3(x,y):
        global start,i
    
    
        if(x==cxp and y==cyp):
            start=1
        
        if(g[x-1][y]==count):
            m[i][0]=x-1
            m[i][1]=y
        
        elif(x+1<=10 and g[x+1][y]==count):
            m[i][0]=x+1
            m[i][1]=y
       
        elif(g[x][y-1]==count):
            m[i][0]=x
            m[i][1]=y-1
        
        elif(y+1<=10 and g[x][y+1]==count):
             m[i][0]=x
             m[i][1]=y+1
        
        i=i+1
    
    
    ############################################
    '  Start and end marker paramter '
    paramg1 = [100,0,0]   #lower  pink
    paramg2 = [255,255,255]     #upper

    paramp1 = [10,100,0]   #lower orange
    paramp2 = [255,255,255]   #upper

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    ' extract color of start grid marker'
    
    lowerp = np.array(paramp1)    ## Convert the parameters into a form that OpenCV can understand
    upperp = np.array(paramp2)
    maskp  = cv2.inRange(hsv, lowerp, upperp)
    resp   = cv2.bitwise_and(img, img, mask= maskp)

    
    ' extract color of end grid marker '

    

   
    lowerg = np.array(paramg1)    ## Convert the parameters into a form that OpenCV can understand
    upperg = np.array(paramg2)
    maskg  = cv2.inRange(hsv, lowerg, upperg)
    resg   = cv2.bitwise_and(img, img, mask= maskg)

    

    ' Co-ordinate of End point '

    
    resg,threshg = cv2.threshold(maskg,127,255,0)
    contours, hierarchy = cv2.findContours(threshg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(threshg,contours,-1,(255,0,255),1)

    Mg = cv2.moments(contours[-1])
    cxg = int(Mg['m10']/Mg['m00'])
    cyg = int(Mg['m01']/Mg['m00'])

    ' scale down points to make it useable for arrays  '
    cxg=(cxg+20)/40                     
    cyg=(cyg+20)/40
    
    #print "End point = ", cxg, ", ", cyg
    


    ' Co-ordinate of start point '

    #grayp = cv2.cvtColor(resp,cv2.COLOR_BGR2GRAY)
    resp,threshp = cv2.threshold(maskp,127,255,0)
    contours, hierarchy = cv2.findContours(threshp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(threshp,contours,-1,(255,0,255),1)

    Mp = cv2.moments(contours[-1])
    cxp = int(Mp['m10']/Mp['m00'])
    cyp = int(Mp['m01']/Mp['m00'])      
    cxp=(cxp+20)/40   
    cyp=(cyp+20)/40
    #print "Start point = ", cxp, ", ", cyp
    

   
    ''' start of actual logic '''

    g=grid_map(img)  # get a grid image of image 
    cxp=cxp-1         # decrease every point by "1" because array index start with zeroes and to compensate that effect 
    cyp=cyp-1
    cxg=cxg-1
    cyg=cyg-1
    
    c=0
    startone(cxp,cyp)
    g[cxp][cyp]=-2
    count=2
    send_co_rdinates()
    
    while end!=1:
        global end    # Global variable to make pythton understand that " end " used here is global and not local var. '
        end=scan()    # Scan image and returns one if we reach end points
        count=count+1
        send_co_rdinates()        # send_co_rdinates() for adding count to grid map aside previous points
        
    #printList(g)     # Uncomment this to see grid map with added number which represent distance from origin
    length=count-1    # length is one less than the count '
    count3=count      # take copy of count for future use

    ##############################################

    count=count-2     # Start trace back with points aside end point with count= (shortest length) - 2
    
    fun3(cyg,cxg)
    

    while count!=0:   # Trace back until we get start point i.e count = 0 '
        
        count=count-1
        if x<25:
            fun3(m[x][0],m[x][1]) # Add points to m(a,b) where a= Two dimensional arrays 
        x=x+1

    
    for x in range(0,count3):   # logic to draw line from concurrent point from trace backed array, count3 hols shortest path length'
    
        if((m[x+1][1]!=0 and m[x+1][0]!=0)):
            cv2.line(img,(((m[x][1])*40+20),((m[x][0])*40+20)),(((m[x+1][1])*40+20),((m[x+1][0])*40+20)),(255,0,0),5)
        
    
    cv2.line(img,(((cxg)*40+20),((cyg)*40+20)),(((m[0][1])*40+20),((m[0][0])*40+20)),(255,0,0),5)
    m=np.rot90(m) # Two rotate function each 90 degree for reversing array '
    m=np.rot90(m)
    
    
    ''' define a reverse array '''
    rows1 = 20 # rows for reverse array
    cols1 = 2
    r=[]
    for row1 in xrange(rows1): r += [[0]*cols1]

    l=0

    r[0][0]=cxp+1
    r[0][1]=cyp+1

    ''' there is one problem , as soon as we rotate array twice , if array size is of 20 and we have only 5 points remaining 15 are (0,0)
        if we rotate it twice we get (0,0) at first 15 and actual points at last 5 points to avoid this we use below loop '''
    
    for y in range(0,20):
          
          if((m[y][1]!=0 and m[y][0]!=0)):
                  
                  r[l+1][0]=m[y][0]+1
                  r[l+1][1]=m[y][1]+1
                 
                  r[l+2][0]=cxg+1
                  r[l+2][1]=cyg+1
                  l=l+1
    
    return length, r # return length and shortest path array


if __name__ == "__main__":
    #code for checking output for single image
    img = cv2.imread('test_images/test_image1.png')
    route_length, route_path = play(img)
    print "route length = ", route_length
    print "route path   = ", route_path
    print '\n'
    #code for checking output for all images
    route_length_list = []
    route_path_list   = []
    for file_number in range(1,6):
        file_name = "test_images/test_image"+str(file_number)+".png"
        pic = cv2.imread(file_name)
        route_length, route_path = play(pic)
        #cv2.imshow('a'+str(file_number),pic) # Uncomment this to see image with traced path
        route_length_list.append(route_length)
        route_path_list.append(route_path)
    
    
    print route_length_list
    print '\n'
    printList(route_path_list) # printList function to print in systematic way
    cv2.waitKey(0)
    cv2.destroyAllWindows()
