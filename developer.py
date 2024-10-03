from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
import webbrowser

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg4.png")
        bg1=bg1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Detect Face  button 2
        det_img_btn=Image.open(r"Images_GUI\my.jpg")
        det_img_btn=det_img_btn.resize((280,280),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",command=self.facebook)
        det_b1.place(x=560,y=200,width=280,height=280)

        det_b1_1 = Button(bg_img,text="Sahan Dulmith",cursor="hand2",command=self.facebook,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=560,y=480,width=280,height=45)


    def facebook(self):
            self.new = 1
            self.url = "https://www.youtube.com/@sahandulmith"
            webbrowser.open(self.url,new=self.new)
        




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()