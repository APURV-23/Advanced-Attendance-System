from tkinter import *
from tkinter import ttk
from types import coroutine
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recongnition_System
import mysql.connector
from time import strftime
from datetime import datetime
import tkinter
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
from main import Face_Recongnition_System
from chattbot import ChatBot

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1368x768+0+0")
        self.root.title(" Login Page")
        # self.root.wm_iconbitmap("img\face.ico")


        self.bg=ImageTk.PhotoImage(file=r"img\BingWallpaper (7).jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=520,y=170,width=340,height=450)

        img1=Image.open(r"img\baseline_account_circle_white_48dp.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        title_lbl_1=Label(self.root,text="DEVELOPED BY APURV A. RATHOD (ENROLLMENT NO:-180470107049)",font=("times new roman",12,"bold"),bg="white",fg="green")
        title_lbl_1.place(x=0,y=635,width=1368,height=35)

        #label1

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg='white',bg='black')
        username.place(x=50,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=30,y=180,width=280)

        #label1

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg='white',bg='black')
        password.place(x=50,y=225)

        self.txtpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=30,y=250,width=280)

        # ====Icon Images====

        img2=Image.open(r"img\baseline_account_circle_white_48dp.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=545,y=325,width=25,height=25)

        img3=Image.open(r"img\iconfinder_lock_115716 (1).png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=545,y=394,width=25,height=25)

        # LoginButton

        loginbtn=Button(frame,command=self.Login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RAISED,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)


        #Regestration Button

        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RAISED,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=25,y=345,width=120)

        #Forgot password button

        forgatbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RAISED,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgatbtn.place(x=20,y=375,width=120)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    def Login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.txtuser.get()=="Apurv" and self.txtpassword.get()=="1234":
            messagebox.showinfo("Success","Welcome to Facial Attendance System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Apurv@admin#2020",database="student_details")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpassword.get()
                                                                                      ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNO","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recongnition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

# ===========================Reset Password =======================
    def reset_password(self):
        if self.combo_security_Q.get()=="Select ":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_Security.get()=="":
            messagebox.showerror("Error","Please enter the answer ",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Apurv@admin#2020",database="student_details")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_Security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset , please login new password",parent=self.root2)
                self.root2.destroy()






# ========Forgot Password======================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password ",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Apurv@admin#2020",database="student_details")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)

            if row==None:
                messagebox.showerror("My Error","Plese enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=lbl=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg='black',bg='white')
                security_Q.place(x=40,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="read only",width=20)
                self.combo_security_Q["values"]=("Select ","Your Birth Place","Your Pet Name","Your Hobbies","Your favourite book")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=40,y=120,width=280)
        # 6
                Security=lbl=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg='black',bg='white')
                Security.place(x=40,y=160)

                self.txt_Security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_Security.place(x=40,y=200,width=250)

                new_password=lbl=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg='black',bg='white')
                new_password.place(x=40,y=260)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=40,y=290,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=120,y=350)
       





            

class Register:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1368x768+0+0")
                self.root.title(" Register ")


        # ===================Variable==========================

                self.var_fname=StringVar()
                self.var_lname=StringVar()
                self.var_contact=StringVar()
                self.var_email=StringVar()
                self.var_securityQ=StringVar()
                self.var_securityA=StringVar()
                self.var_pass=StringVar()
                self.var_confpass=StringVar()
               
        


                self.bg=ImageTk.PhotoImage(file=r"img\bg_reg.jpg")
                lbl_bg=Label(self.root,image=self.bg)
                lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

                self.bg1=ImageTk.PhotoImage(file=r"img\quotes.webp")
                lbl_bg1=Label(self.root,image=self.bg1)
                lbl_bg1.place(x=50,y=100,width=470,height=550)

        # Frame
                frame=Frame(self.root,bg="white")
                frame.place(x=520,y=100,width=800,height=550)

                register_lbl=lbl=Label(frame,text="REGISTER HERE",font=("times new roman",15,"bold"),fg='green',bg='white')
                register_lbl.place(x=20,y=20)

                # ===== Label and enter=======
        # 1
                first_lbl=lbl=Label(frame,text="First name",font=("times new roman",10,"bold"),fg='black',bg='white')
                first_lbl.place(x=50,y=100)

                self.txt_first_lbl=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",10,"bold"))
                self.txt_first_lbl.place(x=50,y=120,width=280)
        # 2
                last_lbl=lbl=Label(frame,text="Last name",font=("times new roman",10,"bold"),fg='black',bg='white')
                last_lbl.place(x=450,y=100)

                self.txt_last_lbl=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",10,"bold"))
                self.txt_last_lbl.place(x=450,y=120,width=280)
        # 3
                Contact_lbl=lbl=Label(frame,text="Contact No",font=("times new roman",10,"bold"),fg='black',bg='white')
                Contact_lbl.place(x=50,y=150)

                self.txt_Contact_lbl=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",10,"bold"))
                self.txt_Contact_lbl.place(x=50,y=170,width=280)

        # 4
                Email_lbl=lbl=Label(frame,text="Email",font=("times new roman",10,"bold"),fg='black',bg='white')
                Email_lbl.place(x=450,y=150)

                self.txt_Email_lbl=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",10,"bold"))
                self.txt_Email_lbl.place(x=450,y=170,width=280)

        # 5
                security_que_lbl=lbl=Label(frame,text="Select Security Question",font=("times new roman",10,"bold"),fg='black',bg='white')
                security_que_lbl.place(x=50,y=210)

                self.combo_security=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",10,"bold"),state="read only",width=20)
                self.combo_security["values"]=("Select ","Your Birth Place","Your Pet Name","Your Hobbies","Your favourite book")
                self.combo_security.current(0)
                self.combo_security.place(x=50,y=230,width=280)
        # 6
                Security=lbl=Label(frame,text="Security Answer",font=("times new roman",10,"bold"),fg='black',bg='white')
                Security.place(x=450,y=210)

                self.Security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",10,"bold"))
                self.Security.place(x=450,y=230,width=280)
        # 7
                Password_lbl=lbl=Label(frame,text="Password",font=("times new roman",10,"bold"),fg='black',bg='white')
                Password_lbl.place(x=50,y=260)

                self.txt_Password_lbl=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",10,"bold"))
                self.txt_Password_lbl.place(x=50,y=280,width=280)
        # 8
                Confirm=lbl=Label(frame,text="Confirm Password",font=("times new roman",10,"bold"),fg='black',bg='white')
                Confirm.place(x=450,y=260)

                self.txt_Confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",10,"bold"))
                self.txt_Confirm.place(x=450,y=280,width=280)

        # =============CheakButton=========
                self.var_check=IntVar()
                checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Condition",font=("times new roman",10,"bold"),onvalue=1,offvalue=0,bg="white",activebackground="white")
                checkbtn.place(x=50,y=340)

        # ========Button==================

                img=Image.open(r"img\register-now-button-sign-key-260nw-1725903712.webp")
                img=img.resize((200,50),Image.ANTIALIAS)
                self.photoimage=ImageTk.PhotoImage(img)
                b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
                b1.place(x=45,y=400,width=200)

        # ========login==========
                img1=Image.open(r"img\login-button-png-18016.png")
                img1=img1.resize((200,50),Image.ANTIALIAS)
                self.photoimage1=ImageTk.PhotoImage(img1)
                b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
                b1.place(x=400,y=400,width=200)

        # =======function declaration============
        def register_data(self):
                if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                        messagebox.showerror("Error","All fields are required",parent=self.root)
                elif self.var_pass.get()!=self.var_confpass.get():
                        messagebox.showerror("Error","Password & Confirm password must be same",parent=self.root)
                elif self.var_check.get()==0:
                        messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="Apurv@admin#2020",database="student_details")
                        my_cursor=conn.cursor()
                        query=("select * from register where email=%s")
                        value=(self.var_email.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        if row!=None:
                                messagebox.showerror("Error","User already exist, please try another email",parent=self.root)
                        else:
                             conn=mysql.connector.connect(host="localhost",username="root",password="Apurv@admin#2020",database="student_details")
                             my_cursor=conn.cursor()
                             my_cursor.execute("INSERT into register values(%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                            self.var_fname.get(),
                                                                                                            self.var_lname.get(),
                                                                                                            self.var_contact.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_securityQ.get(),
                                                                                                            self.var_securityA.get(),
                                                                                                            self.var_pass.get()
                                                                                                        
                                                                                                             ))


                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Register sussessfully",parent=self.root)
# =================login now==================
    
        def return_login(self):
            self.root.destroy()        


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
        b1_1=Button(self.root,text="Exit",cursor="hand2",command=self.Exit,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1310,y=132,width=50,height=45)

        title_lbl=Label(bg_img,text="FACE RECONGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",15,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1368,height=45)

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
    main()
   