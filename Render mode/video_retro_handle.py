

"""
Created on Tue May 11 21:32:34 2021

@author: jedi
"""

import cv2
import numpy as np

# Create a VideoCapture object and read from input file

# If the input is the camera, pass 0 instead of the video file name



# Check if camera opened successfully


def retro_handle(frame):

    
     def do_mosaic(frame, x, y, w, h, neighbor=5):   #  馬賽克化 函數
       
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


     titanfall = cv2.VideoCapture(frame)

     fourcc               =  cv2.VideoWriter_fourcc(*'MP4V')

     video_retro_console  =  cv2.VideoWriter('retro_console.avi'    , fourcc,30,(1920,1080))


     if (titanfall.isOpened()== False):

        print("Error opening video stream or file")

     while(titanfall.isOpened()):

         ret, frame = titanfall.read()

         (width,heigh,dimension)=frame.shape
         
         
         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
         hsv[:,:,1]= hsv[:,:,2]
 
    
         for i in range(0,width) :    # 這一段程式 是用來設定9個門檻值  讓圖片 變成相對應的顏色
      
            for j in range(0,heigh) :
         
             for z in range(0,3):               
            
                if  219< hsv[i,j,2]  :     #  先判斷 R 是否大於204
 
                             hsv[i,j,2]= 230  # 大於204  B , G 直接判斷為255
                             hsv[i,j,1]= 230


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

         do_mosaic(hsv, 0, 0, hsv.shape[1],hsv.shape[0],5)   # 在最終在馬賽克畫一次

         hsv[i,j,z] = hsv[i,j,z]+50
      
         
         if i%6==0 & j%6==0  :                        #判斷是否為偶數行
 
            if hsv[i,j,z]<=49 :
               hsv[i,j,z]=255



       
         if ret == True:

          
          cv2.imshow('retro_console', hsv)
          video_retro_console.write(hsv)
          if cv2.waitKey(10) & 0xFF == ord('q'):
     
     
              break
                                       
                                               
         else:
                                            
           break
   
     titanfall.release()
     cv2.destroyAllWindows()




