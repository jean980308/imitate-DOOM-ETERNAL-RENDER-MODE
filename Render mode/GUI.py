import tkinter as tk

import tkinter.ttk as ttk

import video_classic

import video_blackwhite

import video_VHS

import video_dot

import video_retro_handle


from PIL import Image, ImageTk
"""
lbl_1.grid(column=0, row=500)

"""

window = tk.Tk()
window.title('render mode')
window.geometry('700x500')




img = Image.open('1.jpg')               # 在 gui 介面 放入一張照片     
img = img.resize( (600, 400) )   
imgTk =  ImageTk.PhotoImage(img)                        
lbl_1 = tk.Label(window, image=imgTk)                   
lbl_1.image = imgTk


mycombobox = ttk.Combobox(window, values=[ 'black & white' , 'VHS',  'retro_handled' , 'DOOM CLASSIC ' , 'DOT' ] ) # 再組合方塊 輸入各種渲染模式名稱


mycombobox.pack(pady=10)
mycombobox.current(0)









def button_event1():
   

    print(mycombobox.current(), mycombobox.get())    

    choose=mycombobox.current()      # 找出現在索引 , 渲染模式的名稱都有自己的索引 ,我們才可以尋找相對應的程式
 
    video='oo.mp4'




    if choose==0 :
     mybutton1['bg']   = 'white'
     mybutton1['text'] =('執行'  + mycombobox.get() + str(mycombobox.current()))
     """
     img = Image.open('2.png')                    
     img = img.resize( (600, 400) )   
     imgTk =  ImageTk.PhotoImage(img)                        
     lbl_1 = tk.Label(window, image=imgTk)                   
     lbl_1.image = imgTk
     lbl_1.pack(pady=40)
     """

     video_blackwhite.blackXwhite(video)
     



    if choose==1 :
     mybutton1['bg']   = 'purple'
     mybutton1['text'] =('執行'  + mycombobox.get() + str(mycombobox.current()))
     mybutton1['fg']   = 'black'  
     """
     img = Image.open('3.jpg')                    
     img = img.resize( (600, 400) )   
     imgTk =  ImageTk.PhotoImage(img)                        
     lbl_1 = tk.Label(window, image=imgTk)                   
     lbl_1.image = imgTk
     lbl_1.pack(pady=40)    
     """
     video_VHS.VHS(video)

    


    if choose==2 :
     mybutton1['bg']   = 'orange'
     mybutton1['text'] =('執行'  + mycombobox.get() + str(mycombobox.current()))
     mybutton1['fg']   = 'red'  
     """
     img = Image.open('6.jpg')                    
     img = img.resize( (600, 400) )   
     imgTk =  ImageTk.PhotoImage(img)                        
     lbl_1 = tk.Label(window, image=imgTk)                   
     lbl_1.image = imgTk
     lbl_1.pack(pady=40)
     """    
     video_retro_handle.retro_handle(video)

   


    if choose==3 :
     mybutton1['bg']   = 'blue'
     mybutton1['text'] =('執行'  + mycombobox.get() + str(mycombobox.current()))
     mybutton1['fg']   = 'red'  
     """
     img = Image.open('4.jpg')                    
     img = img.resize( (600, 400) )   
     imgTk =  ImageTk.PhotoImage(img)                        
     lbl_1 = tk.Label(window, image=imgTk)                   
     lbl_1.image = imgTk
     lbl_1.pack(pady=40)
     """
     video_classic.classic(video)

    
    
    if choose==4 :
     mybutton1['bg']   = 'green'
     mybutton1['text'] =('執行'  + mycombobox.get() + str(mycombobox.current()))
     """
     img = Image.open('5.png')                    
     img = img.resize( (600, 400) )   
     imgTk =  ImageTk.PhotoImage(img)                        
     lbl_1 = tk.Label(window, image=imgTk)                   
     lbl_1.image = imgTk
     lbl_1.pack(pady=40)
     """
     video_dot.DOT(video)
 
        
 
mybutton1= tk.Button(window, text='執行' , bg='yellow', command=button_event1 )
mybutton1.pack(pady=20)

lbl_1.pack(pady=30)
# 排版位置



window.mainloop()



























