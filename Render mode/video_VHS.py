

"""
Created on Tue May 11 21:32:34 2021

@author: jedi
"""

import cv2
import numpy as np


# Create a VideoCapture object and read from input file

# If the input is the camera, pass 0 instead of the video file name



# Check if camera opened successfully


def VHS(frame):

    



     titanfall    = cv2.VideoCapture(frame)

     fourcc       = cv2.VideoWriter_fourcc(*'MP4V')

     VHS_VIDEO    = cv2.VideoWriter('VHS.avi'    , fourcc , 30 , (1920,1080) )

     if (titanfall.isOpened()== False):

        print("Error opening video stream or file")

     while(titanfall.isOpened()):

            ret, frame = titanfall.read()

            VHS=frame.copy()
            a=0.7
            b=10
            rows,cols,channels=frame.shape

            for z in range(0,3) :    
               VHS[:,:,z]  = a*VHS[:,:,z]+b
               VHS = VHS.astype(np.uint8)

            for i in range(rows):                        #這段指令用來調對比度 + 加增加每2為間隔 加 像素 40
              for j in range(cols):
                  for c in range(3):
                      color= int(frame[i,j][c]*a+b)
         
                      if i%2==0:                         #判斷是否為偶數行
                         color        = color      + 40  #偶數用來判斷是否超過255 的參數
                         VHS[i,j][c]  = VHS[i,j][c]+ 40  #在偶數行的pixel 都加40
             
                         if color>255:           # 防止像素值越界（0~255）
                             VHS[i,j][c]=255
     
                         elif color<0:           # 防止像素值越界（0~255）
                             VHS[i,j][c]=0
    
                  
    
                  
                      else:      
                          if color>255:           # 防止像素值越界（0~255）
                             VHS[i,j][c]=255
                          elif color<0:           # 防止像素值越界（0~255）
                             VHS[i,j][c]=0
         
            
         
            
         
            
            if ret == True:
                            
             
             cv2.imshow('VHS', VHS)              # 顯示 VHS 影片
             VHS_VIDEO.write(VHS)                # 把檔案寫進去
             
             if cv2.waitKey(10) & 0xFF == ord('q'):
                               
                             
                  break
                                       
            else:
                                            
                  break
   
     titanfall.release()
     cv2.destroyAllWindows()



