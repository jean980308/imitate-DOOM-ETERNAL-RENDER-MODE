

"""
Created on Tue May 11 21:32:34 2021

@author: jedi
"""

import cv2
import numpy as np

# Create a VideoCapture object and read from input file

# If the input is the camera, pass 0 instead of the video file name



# Check if camera opened successfully


def DOT(frame):



     titanfall = cv2.VideoCapture(frame)

     fourcc       = cv2.VideoWriter_fourcc(*'MP4V')

     video_dot     = cv2.VideoWriter('DOT.avi'    , fourcc,30,(1920,1080))
     
     
     if (titanfall.isOpened()== False):

        print("Error opening video stream or file")

     while(titanfall.isOpened()):

         ret, frame = titanfall.read()

         (width,heigh,dimension)=frame.shape


         
         if ret == True:
 
             
                                      
          for x in range(0,heigh,6) :    # 在圖片Y軸 , 每6行為一組 在X軸劃一條線 ,畫到最終點
              
           DOOM_DOT=cv2.line(frame,(x,0),(x,heigh),(10,10,10),2)  # 畫線x軸 顏色黑色 BGR=(2,2,2)
           
          for y in range(0,width,6) :    # 在圖片X軸 , 每6行為一組 在Y軸畫一條線,畫到最終點
              
           DOOM_DOT=cv2.line(frame,(0,y),(heigh,y),(10,10,10),2)  # 畫線y軸 顏色黑色 BGR=(2,2,2)



           cv2.imshow('DOT', DOOM_DOT)


           video_dot.write(DOOM_DOT)
    
          if cv2.waitKey(1) & 0xFF == ord('q'):
     
     
              break
                                       
                                               
         else:
                                            
           break
       
        
   
     titanfall.release()
     cv2.destroyAllWindows()




