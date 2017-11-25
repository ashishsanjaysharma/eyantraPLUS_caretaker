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
import array

#g= array.array();
g={};


def path_detect(img):
    x,y,z= img.shape;
    n=10      # get number of pixels in x,y of original image;
    m=x/n;              # get x co-ordinate spaing for vertical line to start 
    n=y/n;# get y co-ordinate spaing for horizontal line to start
    p = 20;
    while p<x:
        q = 20;
        while q<y:
            if p<400 and q<400:
                    b,c,d=img[p][q];
                    print b,c,d;
                    if b>250 and c>250 and d>250:
                      g[p,q]=0;
                 
                    else:
                    
                       g[p,q]=1;
            q=q+40;
          
        p=p+40;
        
    return g;

    
                              # reurn grid image


img = cv2.imread('test_image5.png')
gridmap= path_detect(img);

#cv2.imshow('i',img);
'''
p=40;

while p<400:
       q = 40;
       while q<400:
          if p<400 and q<400:
             print gridmap.at<int>(i,j);
              
          q=q+40;
          
       p=p+40;'''
print g;
'''
for i in range(400):
    j=0;
    for j in range(400):
        a= g[i][j];
        print a;
        j=j+40;
    i=i+40;'''
   
cv2.waitKey(0)
cv2.destroyAllWindows()


   

 
   
        
            
            
            
            
                

                
            
                
               
            
            
        
        
  
