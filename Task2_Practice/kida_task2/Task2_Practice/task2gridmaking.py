''' This code take image from user and return grid image
Syntax : draw_grid(img,n);
where img : original image on which we want grid
       n  : Number of equally spaced line

Alogrithm:
1. Take image input
2. Call draw_grid function with "image" and number of grid "n" as parameter
3. In function divide image of x*y pixel with n to get x/n and y/n in order to get x and y line coordinates where line will start.
4. Lets take example of 400*400 image then for 10 lines we get x/n=40 ,y/n =40 , for 10 lines in 400*400 we have to leave 40 pixels distance in x and y;
5. Draw line from (x=x/n,0) to (x=x/n,400) for first vertical ine, here (0,0) to (0,400) then (40,0) to (40,400) and so on till (400,0) to (400,400)
6. Draw line from (x,y/n) to (400,y/n) for first horizontal ine with above logic
7. return image

'''

import numpy
import cv2

def draw_grid(img,n):
     
    x,y,c= img.shape;   # get number of pixels in x,y of original image;
    print x 
    print y
    m=x/n;              # get x co-ordinate spaing for vertical line to start 
    n=y/n;              # get y co-ordinate spaing for horizontal line to start
    p = 0
    while p<y:
        cv2.line(img,(p,0),(p,x),(0,0,255),2) # draw vertical line
        cv2.line(img,(0,p),(y,p),(0,0,255),2) # draw horizontal line
        p += m
    return(img)                                 # reurn grid image


img = cv2.imread('test2.png') # image input
gridimage= draw_grid(img,20);       # call grid function
cv2.imshow('grid',gridimage);       # display grid image

cv2.waitKey(0)
cv2.destroyAllWindows()

