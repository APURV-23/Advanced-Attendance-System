from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recongnition_System
import mysql.connector
import tkinter




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

                title_lbl_1=Label(self.root,text="DEVELOPED BY APURV A. RATHOD (ENROLLMENT NO:-180470107049)",font=("times new roman",12,"bold"),bg="white",fg="green")
                title_lbl_1.place(x=0,y=670,width=1368,height=35)

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
                b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
                b1.place(x=400,y=400,width=200)

        # =======function declaration============
        def register_data(self):
                if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                        messagebox.showerror("Error","All fields are required")
                elif self.var_pass.get()!=self.var_confpass.get():
                        messagebox.showerror("Error","Password & Confirm password must be same")
                elif self.var_check.get()==0:
                        messagebox.showerror("Error","Please agree our terms and condition")
                else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="Apurv@admin#2020",database="student_details")
                        my_cursor=conn.cursor()
                        query=("select * from register where email=%s")
                        value=(self.var_email.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        if row!=None:
                                messagebox.showerror("Error","User already exist, please try another email")
                        else:
                                my_cursor.execute=("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
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
                        messagebox.showinfo("Success","Register sussessfully")






if __name__ == "__main__":
    root =Tk()
    obj=Register(root)
    root.mainloop()