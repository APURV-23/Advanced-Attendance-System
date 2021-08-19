from tkinter import*
from  tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import connect, cursor
import cv2
import os
import csv
import xlrd
from tkinter import filedialog
import tkinter




mydata=[]
class Student_Attendance:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1368x768+0+0")
                self.root.title("Student Attendance")

        # =========================Variable===============================   
                self.var_atten_id=StringVar()
                self.var_atten_roll=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_dep=StringVar()
                self.var_atten_time=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_attendance=StringVar()








                # IMG1
                img=Image.open(r'img\smart-attendance.jpg')
                img=img.resize((689,130),Image.ANTIALIAS)#High level to low
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=689,height=120)
                
                # IMG2
                img2=Image.open(r'img\clg.jpg')
                img2=img2.resize((689,130),Image.ANTIALIAS)#High level to low
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=689,y=0,width=689,height=120)
                
                # BG image
                img3=Image.open(r'img\pexels-pixabay-268362.jpg')
                img3=img3.resize((1368,768),Image.ANTIALIAS)#High level to low
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=110,width=1368,height=580)

                title_lbl=Label(bg_img,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",20,"bold"),bg="white",fg="green")
                title_lbl.place(x=0,y=0,width=1368,height=35)

                main_frame=Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=10,y=40,width=1340,height=550)

                #Back
                exitimg=Image.open(r'img\exit.jpg')
                exitimg=exitimg.resize((50,35),Image.ANTIALIAS)#High level to low
                self.photoimg11=ImageTk.PhotoImage(exitimg)

                b1_1=Button(bg_img,text="Back",cursor="hand2",command=self.Back,font=("times new roman",15,"bold"),bg="white",fg="black")
                b1_1.place(x=1310,y=0,width=50,height=35)        


                # left side frame

                Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RAISED,text="Student Attendance Details",font=("times new roman",11,"bold"))
                Left_frame.place(x=10,y=5,width=680,height=530)

                # left img
                img_left=Image.open(r'img\girl.jpeg')
                img_left=img_left.resize((660,130),Image.ANTIALIAS)#High level to low
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(Left_frame,image=self.photoimg_left)
                f_lbl.place(x=5,y=0,width=660,height=130)
                
                
                # Class Student Informantion
                
                Left_inside_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Informantion",font=("times new roman",11,"bold"))
                Left_inside_frame.place(x=5,y=135,width=660,height=350)
                
                #attendance id

                attendanceID_lebel=Label(Left_inside_frame,text='AttendanceID:',font=("times new roman",11,"bold"),bg="white")
                attendanceID_lebel.grid(row=0,column=0,padx=4,pady=5,sticky=W)

                attendanceID_entery=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",11,"bold"))
                attendanceID_entery.grid(row=0,column=1,padx=4,pady=5,sticky=W)

                #RollNo

                RollNo_lebel=Label(Left_inside_frame,text='Roll No:',font=("times new roman",11,"bold"),bg="white")
                RollNo_lebel.grid(row=0,column=2,padx=4,pady=5,sticky=W)

                RollNo_entery=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",11,"bold"))
                RollNo_entery.grid(row=0,column=3,padx=4,pady=5,sticky=W)

                #Student_Name
                
                Student_Name_lebel=Label(Left_inside_frame,text='Name:',font=("times new roman",11,"bold"),bg="white")
                Student_Name_lebel.grid(row=1,column=0,padx=4,pady=5,sticky=W)

                Student_Name_entery=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",11,"bold"))
                Student_Name_entery.grid(row=1,column=1,padx=4,pady=5,sticky=W)

                #Class_Division
                
                Department_lebel=Label(Left_inside_frame,text='Department:',font=("times new roman",11,"bold"),bg="white")
                Department_lebel.grid(row=1,column=2,padx=4,pady=5,sticky=W)
                Department_entery=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",11,"bold"))
                Department_entery.grid(row=1,column=3,padx=4,pady=5,sticky=W)


                #Time

                Time_lebel=Label(Left_inside_frame,text='Time:',font=("times new roman",11,"bold"),bg="white")
                Time_lebel.grid(row=2,column=0,padx=4,pady=5,sticky=W)

                Time_entery=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",11,"bold"))
                Time_entery.grid(row=2,column=1,padx=4,pady=5,sticky=W)

                #date

                Date_lebel=Label(Left_inside_frame,text='Date:',font=("times new roman",11,"bold"),bg="white")
                Date_lebel.grid(row=2,column=2,padx=4,pady=5,sticky=W)

                Date_entery=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",11,"bold"))
                Date_entery.grid(row=2,column=3,padx=4,pady=5,sticky=W)

                # Attendance Status

                Attendance_Status_lebel=Label(Left_inside_frame,text='Attendance Status :',font=("times new roman",11,"bold"),bg="white")
                Attendance_Status_lebel.grid(row=4,column=0,padx=10)

                Attendance_Status_combo=ttk.Combobox(Left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",11,"bold"),state="read only",width=20)
                Attendance_Status_combo["values"]=("Status","Present","Absent")
                Attendance_Status_combo.current(0)
                Attendance_Status_combo.grid(row=4,column=1,padx=2,pady=10,sticky=W)

                # Button Frame1
                button_frame=LabelFrame(Left_inside_frame,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",11,"bold"))
                button_frame.place(x=0,y=300,width=680,height=30)

                Import_csv_button=Button(button_frame,text="Import csv",command=self.importCsv,width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
                Import_csv_button.grid(row=0,column=0)
                
                Export_csv_button=Button(button_frame,text="Export csv",command=self.exportCsv,width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
                Export_csv_button.grid(row=0,column=1)

                Update_button=Button(button_frame,text="Update",command=self.update_data,width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
                Update_button.grid(row=0,column=2)

                reset_button=Button(button_frame,text="Reset",width=22,command=self.reset_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
                reset_button.grid(row=0,column=3)
                


        # right side frame

                right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",11,"bold"))
                right_frame.place(x=700,y=5,width=635,height=530)


        # Table Frame

                table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text=" Search System",font=("times new roman",11,"bold"))
                table_frame.place(x=5,y=5,width=620,height=500)

                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("ID","Roll","Name","Department","Time","Date","Attendance "),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.AttendanceReportTable.xview)
                scroll_y.config(command=self.AttendanceReportTable.yview)

                self.AttendanceReportTable.heading("ID",text="ID")
                self.AttendanceReportTable.heading("Roll",text="Roll")
                self.AttendanceReportTable.heading("Name",text="Name")
                self.AttendanceReportTable.heading("Department",text="Deapartment")
                self.AttendanceReportTable.heading("Time",text="Time")
                self.AttendanceReportTable.heading("Date",text="Date")
                self.AttendanceReportTable.heading("Attendance ",text="Attendance ")

                self.AttendanceReportTable["show"]="headings"

                self.AttendanceReportTable.column("ID",width=100)
                self.AttendanceReportTable.column("Roll",width=100)
                self.AttendanceReportTable.column("Name",width=100)
                self.AttendanceReportTable.column("Department",width=100)
                self.AttendanceReportTable.column("Time",width=100)
                self.AttendanceReportTable.column("Date",width=100)
                self.AttendanceReportTable.column("Attendance ",width=100)

                self.AttendanceReportTable.pack(fill=BOTH,expand=1)

                self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

                

                # ===============================fetch data==================================

        def fetch_data(self,rows):
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in rows:
                        self.AttendanceReportTable.insert("",END,values=i)
               

        

                #import CSV

        def importCsv(self):
                global mydata
                mydata.clear()
                fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln) as myfile:
                        csvread=csv.reader(myfile,delimiter=",")
                        for i in csvread:
                                mydata.append(i)
                        self.fetch_data(mydata)

        #export CSV

        def exportCsv(self):
                try:
                        if len(mydata)<1:
                                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                                return False
                        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV Files","*.CSV"),("EXCEL Files","*.xlsx"),("All Files","*.*")),parent=self.root)
                        with open(fln,mode="w",newline="") as myfile:
                                exp_write=csv.writer(myfile,delimiter=",")
                                for i in mydata:
                                        exp_write.writerow(i)
                                messagebox.showinfo("Data Export","Your data exported to  "+os.path.basename(fln)+"  successfully",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        def get_cursor(self,event=""):
                cursor_row=self.AttendanceReportTable.focus()
                content=self.AttendanceReportTable.item(cursor_row)
                rows=content['values']
                self.var_atten_id.set(rows[0])
                self.var_atten_roll.set(rows[1])
                self.var_atten_name.set(rows[2])
                self.var_atten_dep.set(rows[3])
                self.var_atten_time.set(rows[4])
                self.var_atten_date.set(rows[5])
                self.var_atten_attendance.set(rows[6])

                # RESET
        def reset_data(self):
                self.var_atten_id.set("")
                self.var_atten_roll.set("")
                self.var_atten_name.set("")
                self.var_atten_dep.set("")
                self.var_atten_time.set("")
                self.var_atten_date.set("")
                self.var_atten_attendance.set("")

        def update_data(self):
                global mydata
                if self.var_atten_dep.get()=="Select Deparatment" or self.var_atten_name.get()=="" or self.var_atten_id.get()=="":
                        messagebox.showerror("Error","All Fields are required",parent=self.root)
                else:
                        try:
                                Update=messagebox.askyesno("Update","DO you want this student details",parent=self.root)
                                if Update>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="Apurv@admin#2020",database="student_details")
                                        my_cursor=conn.cursor()
                                        my_cursor.execute("update attendancetable set Roll=%s,Name=%s,Department=%s,Time=%s,Date=%s,Attendance =%s where ID=%s",(                                                                                                                                 
                                                                                                                                                self.var_atten_roll.get(),
                                                                                                                                                self.var_atten_name.get(),
                                                                                                                                                self.var_atten_dep.get(),
                                                                                                                                                self.var_atten_time.get(),
                                                                                                                                                self.var_atten_date.get(),
                                                                                                                                                self.var_atten_attendance.get(),
                                                                                                                                                self.var_atten_id.get()                                                                                        
                                                                                                                                        
                                                                                                                                        ))

                                        messagebox.showinfo("Update","Successfully updated student details",parent=self.root)
                                        conn.commit()
                                        self.fetch_data(mydata)
                                        conn.close()
                        except Exception as es:
                                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                 


        def Back(self):
            self.root.destroy()










if __name__ == "__main__":
    root =Tk()
    obj=Student_Attendance(root)
    root.mainloop()