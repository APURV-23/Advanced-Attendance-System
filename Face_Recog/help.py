from tkinter import*
from  tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import tkinter


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1368x768+0+0")
        self.root.title("Developer Information")

        title_lbl=Label(self.root,text="Help",font=("times new roman",20,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1368,height=35)
         #Back
        exitimg=Image.open(r'img\exit.jpg')
        exitimg=exitimg.resize((50,35),Image.ANTIALIAS)#High level to low
        self.photoimg11=ImageTk.PhotoImage(exitimg)

        b1_1=Button(self.root,text="Back",cursor="hand2",command=self.Back,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1310,y=0,width=50,height=35)

        img_top=Image.open(r'img\girl.jpeg')
        img_top=img_top.resize((1368,700),Image.ANTIALIAS)#High level to low
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=1368,height=700)

        dev_lebel=Label(f_lbl,text='Email:18comp.apurv.rathod@gmail.com',font=("times new roman",13,"bold"),fg="blue")
        dev_lebel.place(x=550,y=220)

        title_lbl_1=Label(f_lbl,text="DEVELOPED BY APURV A. RATHOD (ENROLLMENT NO:-180470107049)",font=("times new roman",12,"bold"),bg="white",fg="green")
        title_lbl_1.place(x=0,y=625,width=1368,height=35)

    def Back(self):
            self.root.destroy()

if __name__ == "__main__":
    root =Tk()
    obj=Help(root)
    root.mainloop()