from tkinter import*
from  tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import tkinter


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1368x768+0+0")
        self.root.title("Developer Information")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",20,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1368,height=35)
        
         #Back
        
        b1_1=Button(self.root,text="Back",cursor="hand2",command=self.Back,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1310,y=0,width=50,height=30)
        title_lbl_1=Label(self.root,text="DEVELOPED BY APURV A. RATHOD (ENROLLMENT NO:-180470107049)",font=("times new roman",12,"bold"),bg="white",fg="green")
        title_lbl_1.place(x=0,y=535,width=1368,height=35)

        img_top=Image.open(r'img\dev.jpg')
        img_top=img_top.resize((1368,700),Image.ANTIALIAS)#High level to low
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=1368,height=700)

        # Frame
    
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=600,height=600)

        img_top1=Image.open(r"img\APURV RATHOD.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top_tool=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top_tool)
        f_lbl.place(x=350,y=0,width=200,height=200)

        
#  Developer info

        dev_lebel=Label(main_frame,text='Hello my name, Apurv.',font=("times new roman",13,"bold"),bg="white")
        dev_lebel.place(x=0,y=5)

        dev_lebel=Label(main_frame,text='I am student of V.V.P Engineeimg college.',font=("times new roman",13,"bold"),bg="white")
        dev_lebel.place(x=0,y=40)

        dev_lebel=Label(main_frame,text='I am passionate about learn new things.',font=("times new roman",13,"bold"),bg="white")
        dev_lebel.place(x=0,y=75)

        img_top2=Image.open(r'img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg')
        img_top2=img_top2.resize((600,390),Image.ANTIALIAS)#High level to low
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(self.root,image=self.photoimg_top2)
        f_lbl.place(x=800,y=270,width=600,height=390)

    def Back(self):
            self.root.destroy()



if __name__ == "__main__":
    root =Tk()
    obj=Developer(root)
    root.mainloop()