
import cv2
import numpy as np


# Create a VideoCapture object and read from input file

# If the input is the camera, pass 0 instead of the video file name



# Check if camera opened successfully


def classic(frame):

    
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


     titanfall       = cv2.VideoCapture(frame)

     fourcc          = cv2.VideoWriter_fourcc(*'MP4V')

     video_classic   = cv2.VideoWriter('classic.avi'    , fourcc,30,(1920,1080))


     if (titanfall.isOpened()== False):

        print("Error opening video stream or file")

     while(titanfall.isOpened()):

         ret, frame = titanfall.read()

         (width,heigh,dimension)=frame.shape

         classic =  cv2.resize(frame,(int(frame.shape[1]*0.3),int(frame.shape[0]*0.3)),interpolation=cv2.INTER_CUBIC) # 把畫面 解系度降低
         classic =  cv2.resize(classic,(int(frame.shape[1]),int(frame.shape[0])))  # 把畫面再度放大
         do_mosaic(classic, 0, 0, classic.shape[1],classic.shape[0])               # 在馬賽克化
       
         
       
        
       
        
       
        
       
        
         if ret == True:

       #   video_classic.write(classic)
             
          cv2.imshow('classic', classic)
       
        
          video_classic.write(classic)
         
          if cv2.waitKey(10) & 0xFF == ord('q'):
     
     
              break
                                       
         else:
                                            
           break
   
     titanfall.release()
     cv2.destroyAllWindows()




