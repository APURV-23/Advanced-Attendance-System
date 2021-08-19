from tkinter import*
from  tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from students import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Student_Attendance
from developer import Developer
from help import Help
import tkinter
from time import strftime
from datetime import datetime
from chattbot import ChatBot


class Face_Recongnition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1368x768+0+0")
        self.root.title("Face Recongnition System")


         # IMG1
        img=Image.open(r'img\BestFacialRecognition.jpg')
        img=img.resize((400,130),Image.ANTIALIAS)#High level to low
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)
        # IMG2
        img1=Image.open(r'img\facialrecognition.png')
        img1=img1.resize((600,130),Image.ANTIALIAS)#High level to low
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=600,height=130)
        # IMG3
        img2=Image.open(r'img\img1.jpeg')
        img2=img2.resize((400,130),Image.ANTIALIAS)#High level to low
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=400,height=130)
        # BG image
        img3=Image.open(r'img\pexels-victor-freitas-973506.jpg')
        img3=img3.resize((1368,768),Image.ANTIALIAS)#High level to low
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1368,height=580)

        # b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Exit)
        # b1.place(x=1310,y=0,width=50,height=35)
        
        b1_1=Button(self.root,text="Exit",cursor="hand2",command=self.Exit,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1310,y=132,width=50,height=45)


        title_lbl=Label(bg_img,text="FACE RECONGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",15,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1368,height=45)

        title_lbl_1=Label(bg_img,text="DEVELOPED BY APURV A. RATHOD (ENROLLMENT NO:-180470107049)",font=("times new roman",12,"bold"),bg="white",fg="green")
        title_lbl_1.place(x=0,y=525,width=1368,height=35)
      

        # =======Time=========

        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text =string)
            lbl.after(1000,time)
        lbl =Label(title_lbl,font =('times new roman',14,'bold'),background='white',foreground ='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

    

        #Student button
        img4=Image.open(r'img\student.jpg')
        img4=img4.resize((180,180),Image.ANTIALIAS)#High level to low
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=135,y=100,width=180,height=180)
        
        b1_1=Button(bg_img,text="Students details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=135,y=260,width=180,height=25)
        
        #Face detector
        img5=Image.open(r'img\face_detector1.jpg')
        img5=img5.resize((180,180),Image.ANTIALIAS)#High level to low
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognition_data)
        b1.place(x=445,y=100,width=180,height=180)
        
        b1_1=Button(bg_img,text="Face Dectector",cursor="hand2",command=self.face_recognition_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=445,y=260,width=180,height=25)
        
        #Attendance face button
        img6=Image.open(r'img\smart-attendance.jpg')
        img6=img6.resize((180,180),Image.ANTIALIAS)#High level to low
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.Student_Attendance_data)
        b1.place(x=755,y=100,width=180,height=180)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.Student_Attendance_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=755,y=260,width=180,height=25)
        
        #Chatbot  button
        img7=Image.open(r'img\chatbot.jfif')
        img7=img7.resize((180,180),Image.ANTIALIAS)#High level to low
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.ChatBot)
        b1.place(x=1055,y=100,width=180,height=180)
        
        b1_1=Button(bg_img,text="ChatBot",cursor="hand2",command=self.ChatBot,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1055,y=265,width=180,height=25)
        
        #Train face button
        img8=Image.open(r'img\di.jpg')
        img8=img8.resize((180,180),Image.ANTIALIAS)#High level to low
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=135,y=330,width=180,height=180)
        
        b1_1=Button(bg_img,text="Train A Model ",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=135,y=490,width=180,height=25)
        
        #Photos face button
        img9=Image.open(r'img\pexels-thisisengineering-3861969.jpg')
        img9=img9.resize((180,180),Image.ANTIALIAS)#High level to low
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=445,y=330,width=180,height=180)
        
        b1_1=Button(bg_img,text="Photoes Of Student ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=445,y=490,width=180,height=25)
        
        
        #Developer button
        img10=Image.open(r'img\dev.jpg')
        img10=img10.resize((180,180),Image.ANTIALIAS)#High level to low
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Developer_data)
        b1.place(x=745,y=330,width=180,height=180)
       
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.Developer_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=745,y=490,width=180,height=25)
        
        #Help Button
        img11=Image.open(r'img\help.jpg')
        img11=img11.resize((180,180),Image.ANTIALIAS)#High level to low
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Help_data)
        b1.place(x=1055,y=330,width=180,height=180)
       
        b1_1=Button(bg_img,text="Help ",cursor="hand2",command=self.Help_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1055,y=490,width=180,height=25)

    def open_img(self):
        os.startfile("data")

# =========================Function Buttons=================================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def Student_Attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Attendance(self.new_window)

    def Developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def Help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def ChatBot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)

    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("Face Recognition","Are sure exit this project",parent=self.root)
        if self.Exit >0:
            self.root.destroy()
        else:
            return


 

if __name__ == "__main__":
    root =Tk()
    obj=Face_Recongnition_System(root)
    root.mainloop()
