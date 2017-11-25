''' This code take image from user and return grid map of image
Syntax : path_detect(img);
where img : original image on which we want grid map
      

Alogrithm:
1. Take image input
2. Call draw_grid function with "image" as parameter
3. get RGB parameters of image
4. get centroid of each image for given example 400*400 image we divide by 10 to get 40*40
5. Create array named g for storing grid map
6. Check for centroid pixel RGB value of each grid
7. If Pixel RGB value matches with white color RGB i.e 255 then it is white color
8. Assign '0' to white color pixels in grid map array else assign '1'
9 Move to next pixel by incrementing x value by 40 same is done for y value.
10. Print array returned by function
'''

import numpy
import cv2

rows = 10 # rows for grid map array
cols = 10 # column for grid map array

g=[]      # array for grid map

for row in xrange(rows): g += [[0]*cols] # define array g with all element zero 

'''           maxItemLength of item of an array           '''
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

        
def path_detect(img):
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
        
                    if b>240 and c>240 and d>240: # check RGB value ,if white then assign '0' else '1'
                      g[p/40][q/40]=0;
                    else:
                      g[p/40][q/40]=1;
            q=q+40;
          
        p=p+40;
        
    return g;       # return grid map array

    
img = cv2.imread('test_image1.png') # take input image
gridmap= path_detect(img);            # call function to get gridmap

printList(g);                            # print array 'g'

cv2.waitKey(0)
cv2.destroyAllWindows()


   

 
   
        
            
            
            
            
                

                
            
                
               
            
            
        
        
  
