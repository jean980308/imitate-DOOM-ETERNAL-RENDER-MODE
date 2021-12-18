
"""
Created on Tue May 11 21:32:34 2021

@author: jedi
"""

import cv2
import numpy as np


# Create a VideoCapture object and read from input file

# If the input is the camera, pass 0 instead of the video file name



# Check if camera opened successfully


def blackXwhite(frame):



     titanfall             = cv2.VideoCapture(frame)
     
     fourcc                = cv2.VideoWriter_fourcc(*'MP4V')
     
     video_blackXwhite     = cv2.VideoWriter('blackXwhite.avi'    , fourcc,30,(1920,1080))
     
     
     if (titanfall.isOpened()== False):

        print("Error opening video stream or file")

     while(titanfall.isOpened()):

         ret, frame = titanfall.read()

         (width,heigh,dimension)=frame.shape


         new_gray = np.ones((width, heigh, dimension),dtype=np.uint8)   # 先創立一個以1為主的圖片
 
         gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)                   # 把 RGB圖片 轉換成 灰階化圖片

         for z in range(0,2,1)  :
         
          new_gray[:,:,z] = gray                                        # 把 灰階圖片1維度 傳入新圖片 B G R 三個維度 , 三個維度化素都一樣
  
          rows,cols,channels=new_gray.shape
  
          new_gray[:,:,2] = gray-6                                      # 原本灰圖片-6畫素 傳入新圖片 R維度
  
    
  
         for i in range(rows):                                          # 在R維度 , 如果畫素 大於250變為0 ,因為 你gray-6 但如果今天 剛好那個畫素維為0 or 1 減 6後  , 會變成 250 255 , 畫素瞬間變成紅色 ,維度 2 為R 因此顏色不會變成灰色 變成 紅色 
            for j in range(cols):
             if new_gray[i,j,2]>=250 :
                new_gray[i,j,2]=0



              
         if ret == True:


          cv2.imshow('black&white', new_gray)
          
          
          video_blackXwhite.write(new_gray)    
       
          if cv2.waitKey(10) & 0xFF == ord('q'):
     
     
              break
                                       
                                               
         else:
                                            
           break
   
     titanfall.release()
     cv2.destroyAllWindows()




