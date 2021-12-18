# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:32:34 2021

@author: jedi
"""

import cv2
import numpy as np


# Create a VideoCapture object and read from input file

# If the input is the camera, pass 0 instead of the video file name

titanfall = cv2.VideoCapture('oo.mp4')

# Check if camera opened successfully
def do_mosaic(frame, x, y, w, h, neighbor=5):


   #獲取這張圖片的h和w，並賦值給fh和fw 
   fh, fw = frame.shape[0], frame.shape[1] #判斷如果超過返回 

   if (y + h > fh) or (x + w > fw): 
 
     return
 
   for i in range(0, h - neighbor, neighbor): # 關鍵點0 減去neightbour 防止溢出

    for j in range(0, w - neighbor, neighbor):
     rect = [j + x, i + y, neighbor, neighbor] 
     color = frame[i + y][j + x].tolist() # 關鍵點1 tolist 
     left_up = (rect[0], rect[1]) 
     right_down = (rect[0] + neighbor - 1, rect[1] + neighbor - 1) # 關鍵點2 減去一個像素 
     cv2.rectangle(frame, left_up, right_down, color, -1)




fourcc       = cv2.VideoWriter_fourcc(*'MP4V')

VHS_VIDEO     = cv2.VideoWriter('VHS.avi'    , fourcc,30,(1920,1080))
WHITE_VIDEO   = cv2.VideoWriter('BLACK_WHITE.avi' , fourcc,30,(1920,1080))
YELLOW_VIDEO  = cv2.VideoWriter('YELLOW.avi' , fourcc,30,(1920,1080))
CLASSIC_VIDEO = cv2.VideoWriter('CLASSIC.avi', fourcc,30,(1920,1080))
DOT_VIDEO     = cv2.VideoWriter('DOT.avi'    , fourcc,30,(1920,1080))


if (titanfall.isOpened()== False):

  print("Error opening video stream or file")

 

# Read until video is completed3
while(titanfall.isOpened()):

  # Capture frame-by-frame

  ret, frame = titanfall.read()

  (width,heigh,dimension)=frame.shape

  "這邊是做黃色 RETRO_CONSOLE"
  
  
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
  hsv[:,:,1]= hsv[:,:,2]
 
  for i in range(0,width) : 
      
            for j in range(0,heigh) :
         
                
            
                if  219< hsv[i,j,2]  :     #  先判斷 R 是否大於204
 
                             hsv[i,j,2]= 255  # 大於204  B , G 直接判斷為255
                             hsv[i,j,1]= 255


                             if 219 <= hsv[i,j,0] <255 :       #再來判斷 B 是否大於84  , 傳給255
 
                                            hsv[i,j,0]= 219



                             if 183 <= hsv[i,j,0] <219 :       #再來判斷 B 是否大於84  , 傳給255
 
                                            hsv[i,j,0]= 183

                             if 147 <= hsv[i,j,0] <183 :   
 
                                            hsv[i,j,0]= 147
                    
                             if 111 <= hsv[i,j,0] <147 :   
 
                                            hsv[i,j,0]= 111
                    
                             if 75 <= hsv[i,j,0]  <111 :   
 
                                            hsv[i,j,0]= 75
                    
                             if 39 <= hsv[i,j,0] < 75 :   
 
                                            hsv[i,j,0]= 39
                   
                             if 3 <= hsv[i,j,0]< 39 :   
 
                                            hsv[i,j,0]= 3
                   
                             if hsv[i,j,0]     < 3  :   
 
                                            hsv[i,j,0]=  0            
            
         
            
         
            
         
            
                if 183< hsv[i,j,2] <= 219 :     #  先判斷 R 是否大於204
 
                             hsv[i,j,2]= 219  # 大於204  B , G 直接判斷為255
                             hsv[i,j,1]= 219


                             if 183 <= hsv[i,j,0] <219 :       #再來判斷 B 是否大於84  , 傳給255
 
                                            hsv[i,j,0]= 183

                             if 147 <= hsv[i,j,0] <183 :   
 
                                            hsv[i,j,0]= 147
                    
                             if 111 <= hsv[i,j,0] <147 :   
 
                                            hsv[i,j,0]= 111
                    
                             if 75 <= hsv[i,j,0] <=111 :   
 
                                            hsv[i,j,0]= 75
                    
                             if 39 <= hsv[i,j,0] < 75 :   
 
                                            hsv[i,j,0]= 39
                   
                             if 3 <= hsv[i,j,0]< 39 :   
 
                                            hsv[i,j,0]= 3
                   
                             if hsv[i,j,0]     < 3  :   
 
                                            hsv[i,j,0]=  0   
          






                elif  147< hsv[i,j,2] <=183 :    #  先判斷 R 是否介於204 --102 之間
 
                               hsv[i,j,2]= 183   # 大於204  R, G 直接判斷為153
                               hsv[i,j,1]= 183
                   
                   
                               if hsv[i,j,2] < hsv[i,j,0] :  # 今天 b 不大於 r , 如過大於 , b 直接跟r一樣

                                  hsv[i,j,0] = hsv[i,j,2] 
                                  
                                  
                                  
                      
                               elif hsv[i,j,2] > hsv[i,j,0] : # b 小於 r ,就算ok
                
                       
                                    if 147 <= hsv[i,j,0] <183 :   
 
                                            hsv[i,j,0]= 147
                    
                                    if 111 <= hsv[i,j,0] <147 :   
 
                                            hsv[i,j,0]= 111
                    
                                    if 75 <= hsv[i,j,0] <111 :   
 
                                            hsv[i,j,0]= 75
                    
                                    if 39 <= hsv[i,j,0] < 75 :   
 
                                            hsv[i,j,0]= 39
                   
                                    if 3 <=hsv[i,j,0]  < 39 :   
 
                                            hsv[i,j,0]= 3
                   
                                    if hsv[i,j,0]     < 3 :   
 
                                            hsv[i,j,0]=  0   
          
          







                elif 111< hsv[i,j,2] <=147 :    #  先判斷 R 是否介於204 --102 之間
 
                               hsv[i,j,2]= 147   # 大於204  R, G 直接判斷為153
                               hsv[i,j,1]= 147
                   
                   
                               if hsv[i,j,2] < hsv[i,j,0] :  # 今天 b 不大於 r , 如過大於 , b 直接跟r一樣

                                  hsv[i,j,0] = hsv[i,j,2] 
                                  
                                  
                                  
                      
                               elif hsv[i,j,2] > hsv[i,j,0] : # b 小於 r ,就算ok
                
                       
                                    if 111 <= hsv[i,j,0] <147 :   
 
                                            hsv[i,j,0]= 111
                    
                                    if 75 <= hsv[i,j,0] <111 :   
 
                                            hsv[i,j,0]= 75
                    
                                    if 39 <=hsv[i,j,0]  < 75 :   
 
                                            hsv[i,j,0]= 39
                   
                                    if 3 <=hsv[i,j,0]   < 39 :   
 
                                            hsv[i,j,0]=  3
                   
                                    if hsv[i,j,0]       < 3 :   
 
                                            hsv[i,j,0]=  0   
          





                elif  75 <hsv[i,j,2] <=111 :    #  先判斷 R 是否介於204 --102 之間
 
                               hsv[i,j,2]= 111   # 大於204  R, G 直接判斷為153
                               hsv[i,j,1]= 111
                   
                   
                               if hsv[i,j,2] < hsv[i,j,0] :  # 今天 b 不大於 r , 如過大於 , b 直接跟r一樣

                                  hsv[i,j,0] = hsv[i,j,2] 
                                  
                                  
                                  
                      
                               elif hsv[i,j,2] > hsv[i,j,0] : # b 小於 r ,就算ok
                
                       
                                    if 75 <= hsv[i,j,0] <111 :   
 
                                            hsv[i,j,0]= 75
                    
                                    if 39 <= hsv[i,j,0]  <75 :   
 
                                            hsv[i,j,0]= 39
                   
                                    if 3 <= hsv[i,j,0] < 39 :   
 
                                            hsv[i,j,0]= 3
                   
                                    if hsv[i,j,0]       <3 :   
 
                                            hsv[i,j,0]=  0   
          
                
                
                elif 39 < hsv[i,j,2] <=75 :   
                    
                                    hsv[i,j,2]= 75
                                    hsv[i,j,1]= 75
                   
                             
                                    if hsv[i,j,2] < hsv[i,j,0] :

                                       hsv[i,j,0] = hsv[i,j,2] 

                        
                                    elif hsv[i,j,2] > hsv[i,j,0] :
                
                       
                                         if 39 <= hsv[i,j,0] < 75 :   
 
                                            hsv[i,j,0] = 39
                   
                                         if 3 <=  hsv[i,j,0] < 39 :   
 
                                            hsv[i,j,0]= 3
                   
                                         if hsv[i,j,0]< 3 :   
 
                                            hsv[i,j,0]=  0   


                elif  3< hsv[i,j,2] <=39 :
                    
                                    hsv[i,j,2]= 39
                                    hsv[i,j,1]= 39
                   
                             
                                    if hsv[i,j,2] < hsv[i,j,0] :

                                       hsv[i,j,0] = hsv[i,j,2] 
                      
                                    elif hsv[i,j,2] > hsv[i,j,0] :
                
                       
                                         if 3 <= hsv[i,j,0] < 39 :   
 
                                            hsv[i,j,0]= 3
                   
                                         if hsv[i,j,0]< 3 :   
 
                                            hsv[i,j,0]=  0    
                                            
                                            
                elif hsv[i,j,2] <=3 :
                    
                                    hsv[i,j,2]= 3
                                    hsv[i,j,1]= 3
                   
                             
                                    if hsv[i,j,2] < hsv[i,j,0] :

                                       hsv[i,j,0] = hsv[i,j,2] 
                      
                                    elif hsv[i,j,2] > hsv[i,j,0] :
                
                       

                                         if hsv[i,j,0] < 3 :   
 
                                            hsv[i,j,0]=  0     

  do_mosaic(hsv, 0, 0, hsv.shape[1],hsv.shape[0],2)


  "馬賽克化"


  classic =  cv2.resize(frame,(int(frame.shape[1]*0.3),int(frame.shape[0]*0.3)),interpolation=cv2.INTER_CUBIC)
  classic =  cv2.resize(classic,(int(frame.shape[1]),int(frame.shape[0]))) 
  do_mosaic(classic, 0, 0, classic.shape[1],classic.shape[0])
 




  "黑白色 BLACK & WHITE"

  new_gray = np.ones((width, heigh, dimension),dtype=np.uint8)
 

  gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

  
  for z in range(0,2,1)  :
   new_gray[:,:,z] = gray
  
  
   rows,cols,channels=new_gray.shape
   new_gray[:,:,2] = gray-6 
  
  for i in range(rows):
     for j in range(cols):
            if new_gray[i,j,2]>=250      :
                new_gray[i,j,2]=0



 
    
 
    
 
 
    
 
  " 調對比度的數字  VHS"
  
  VHS=frame.copy()
  a=0.7
  b=10


  for z in range(0,3) :    
   VHS[:,:,z]  = a*VHS[:,:,z]+b
   VHS = VHS.astype(np.uint8)


  for i in range(rows):
    for j in range(cols):
        for c in range(3):
            color= int(frame[i,j][c]*a+b)
         
            if i%2==0:   
               color        = color      + 40
               VHS[i,j][c]  = VHS[i,j][c]+ 40
               
               
               
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

    cv2.imshow('VHS', VHS)

    VHS_VIDEO.write(VHS)
    
    cv2.imshow('classic', classic)
    
    CLASSIC_VIDEO.write(classic)
    
    cv2.imshow('gray',new_gray)

    WHITE_VIDEO.write(new_gray)  

    # Display the resulting frame
    
     
    cv2.imshow('HSV',hsv)

    YELLOW_VIDEO.write(hsv)  
    
    for x in range(0,heigh,6) :
     DOOM_DOT=cv2.line(frame,(x,0),(x,heigh),(2,2,2),2)
    for y in range(0,width,6) :   
     DOOM_DOT=cv2.line(frame,(0,y),(heigh,y),(2,2,2),2)  
   
    
    cv2.imshow('DOT', DOOM_DOT)

    DOT_VIDEO.write(DOOM_DOT)
    


   

    if cv2.waitKey(1) & 0xFF == ord('q'):
     
     
     break

 

  # Break the loop

  else:

    break


 

# When everything done, release the video capture object

titanfall.release()

 
# Closes all the frames

cv2.destroyAllWindows()


