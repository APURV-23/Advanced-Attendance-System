from tkinter import*
from  tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import tkinter






class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1368x768+0+0")
        self.root.title("Students Details")

     # =========================Variable===============================   

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_Photo=StringVar()
        self.var_radio1=StringVar()
        



    

    
        
        # IMG1
        img=Image.open(r'img\BestFacialRecognition.jpg')
        img=img.resize((400,130),Image.ANTIALIAS)#High level to low
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=120)
        # IMG2
        img1=Image.open(r'img\facialrecognition.png')
        img1=img1.resize((600,130),Image.ANTIALIAS)#High level to low
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=600,height=120)
        # IMG3
        img2=Image.open(r'img\img1.jpeg')
        img2=img2.resize((400,130),Image.ANTIALIAS)#High level to low
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=400,height=120)
   
        
        # BG image
        img3=Image.open(r'img\pexels-victor-freitas-973506.jpg')
        img3=img3.resize((1368,768),Image.ANTIALIAS)#High level to low
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=110,width=1368,height=580)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",20,"bold"),bg="white",fg="green")
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

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RAISED,text="Student Details",font=("times new roman",11,"bold"))
        Left_frame.place(x=10,y=5,width=680,height=530)

        # left img
        img_left=Image.open(r'img\clg.jpg')
        img_left=img_left.resize((660,130),Image.ANTIALIAS)#High level to low
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=660,height=130)
        
        # Current course

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text=" Current Course Information",font=("times new roman",11,"bold"))
        current_course_frame.place(x=5,y=135,width=660,height=130)

        # Department

        dep_lebel=Label(current_course_frame,text='Department',font=("times new roman",11,"bold"),bg="white")
        dep_lebel.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",11,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # Course

        Course_lebel=Label(current_course_frame,text='Course',font=("times new roman",11,"bold"),bg="white")
        Course_lebel.grid(row=0,column=3,padx=10)

        Course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",11,"bold"),state="read only")
        Course_combo["values"]=("Select Course","BE","FE","SE","TE")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=4,padx=2,pady=10,sticky=W)
        
        # Year

        Year_lebel=Label(current_course_frame,text='Year',font=("times new roman",11,"bold"),bg="white")
        Year_lebel.grid(row=1,column=0,padx=10)

        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",11,"bold"),state="read only")
        Year_combo["values"]=("Select Year","2018-19","2019-20","2020-21","2021-22")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        # Semester

        Semester_lebel=Label(current_course_frame,text='Semester',font=("times new roman",11,"bold"),bg="white")
        Semester_lebel.grid(row=1,column=3,padx=10)

        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",11,"bold"),state="read only")
        Semester_combo["values"]=("Select Semester","Semester 1","Semester 2","Semester 3","Semester 4","Semester 5","Semester 6","Semester 7","Semester 8")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=4,padx=2,pady=10,sticky=W)
        
        # Class Student Informantion
            
        Class_Student_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Informantion",font=("times new roman",11,"bold"))
        Class_Student_course_frame.place(x=5,y=240,width=660,height=300)
        
        #StudentId

        StudentID_lebel=Label(Class_Student_course_frame,text='StudentID:',font=("times new roman",11,"bold"),bg="white")
        StudentID_lebel.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entery=ttk.Entry(Class_Student_course_frame,textvariable=self.var_std_id,width=20,font=("times new roman",11,"bold"))
        studentID_entery.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student_Name
        
        Student_Name_lebel=Label(Class_Student_course_frame,text='Student Name:',font=("times new roman",11,"bold"),bg="white")
        Student_Name_lebel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Student_Name_entery=ttk.Entry(Class_Student_course_frame,textvariable=self.var_std_name,width=20,font=("times new roman",11,"bold"))
        Student_Name_entery.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class_Division
        
        Class_Division_lebel=Label(Class_Student_course_frame,text='Class Division:',font=("times new roman",11,"bold"),bg="white")
        Class_Division_lebel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

       
        div_combo=ttk.Combobox(Class_Student_course_frame,textvariable=self.var_div,font=("times new roman",11,"bold"),state="read only",width=18)
        div_combo["values"]=("","G1","G2","G3")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #RollNo
     
        RollNo_lebel=Label(Class_Student_course_frame,text='RollNo :',font=("times new roman",11,"bold"),bg="white")
        RollNo_lebel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        RollNo_entery=ttk.Entry(Class_Student_course_frame,textvariable=self.var_roll,width=20,font=("times new roman",11,"bold"))
        RollNo_entery.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender

        Gender_lebel=Label(Class_Student_course_frame,text='Gender:',font=("times new roman",11,"bold"),bg="white")
        Gender_lebel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(Class_Student_course_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),state="read only",width=18)
        gender_combo["values"]=("","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # DOB
        
        DOB_lebel=Label(Class_Student_course_frame,text='DOB:',font=("times new roman",11,"bold"),bg="white")
        DOB_lebel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entery=ttk.Entry(Class_Student_course_frame,textvariable=self.var_dob,width=20,font=("times new roman",11,"bold"))
        DOB_entery.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        
        Email_lebel=Label(Class_Student_course_frame,text='Email:',font=("times new roman",11,"bold"),bg="white")
        Email_lebel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entery=ttk.Entry(Class_Student_course_frame,textvariable=self.var_email,width=20,font=("times new roman",11,"bold"))
        Email_entery.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #PhoneNO
        
        PhoneNO_lebel=Label(Class_Student_course_frame,text='Phone NO:',font=("times new roman",11,"bold"),bg="white")
        PhoneNO_lebel.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        PhoneNO_entery=ttk.Entry(Class_Student_course_frame,textvariable=self.var_phone,width=20,font=("times new roman",11,"bold"))
        PhoneNO_entery.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        
        Address_lebel=Label(Class_Student_course_frame,text='Address:',font=("times new roman",11,"bold"),bg="white")
        Address_lebel.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entery=ttk.Entry(Class_Student_course_frame,textvariable=self.var_address,width=20,font=("times new roman",11,"bold"))
        Address_entery.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #TeacherName
        
        TeacherName_lebel=Label(Class_Student_course_frame,text='Teacher Name:',font=("times new roman",11,"bold"),bg="white")
        TeacherName_lebel.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        TeacherName_entery=ttk.Entry(Class_Student_course_frame,textvariable=self.var_teacher,width=20,font=("times new roman",11,"bold"))
        TeacherName_entery.grid(row=4,column=3,padx=10,pady=5,sticky=W)

    #    Radiobutton
        radiobutton1=ttk.Radiobutton(Class_Student_course_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=6,column=0)

        radiobutton2=ttk.Radiobutton(Class_Student_course_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=6,column=1)

        # Button Frame1
        button_frame=LabelFrame(Class_Student_course_frame,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",11,"bold"))
        button_frame.place(x=0,y=190,width=680,height=30)

        save_button=Button(button_frame,text="Save",command=self.add_data,width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)
        
        update_button=Button(button_frame,text="Update",command=self.update_data,width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

        delete_button=Button(button_frame,text="Delete",command=self.delete_data,width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)

        reset_button=Button(button_frame,text="Reset",command=self.reset_data,width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)

        # photo button
        take_photo_btn=LabelFrame(Class_Student_course_frame,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",11,"bold"))
        take_photo_btn.place(x=0,y=220,width=680,height=30)

        take_Photo_button=Button(take_photo_btn,command=self.generate_dataset,text="Take Photo Sample",width=46,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_Photo_button.grid(row=0,column=2)

        update_Photo_button=Button(take_photo_btn,command=self.generate_dataset,text="Update Photo Sample",width=46,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_Photo_button.grid(row=0,column=3)


# right side frame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",11,"bold"))
        right_frame.place(x=700,y=5,width=635,height=530)

         # rigth img
        img_right=Image.open(r'C:\learn new\ML\Face_Recog\img\student.jpg')
        img_right=img_right.resize((630,130),Image.ANTIALIAS)#High level to low
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=620,height=130)


# ===========Search System==========
        
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text=" Search System",font=("times new roman",11,"bold"))
        search_frame.place(x=5,y=135,width=600,height=70)

        search_lebel=Label(search_frame,text='Search By:',font=("times new roman",11,"bold"),bg="red")
        search_lebel.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        self.var_com_search=StringVar()
        self.var_search=StringVar()
        
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",11,"bold"),state="read only")
        search_combo["values"]=("Select","RollNo ","Name","Department")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entery=ttk.Entry(search_frame,textvariable=self.var_search,width=13,font=("times new roman",11,"bold"))
        search_entery.grid(row=0,column=2,padx=10,pady=5,sticky=W)




        search_button=Button(search_frame,text="Search",command=self.search_data,width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=4)

        showAll_button=Button(search_frame,text="Show All",command=self.fetch_data,width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_button.grid(row=0,column=4,padx=4)

# Table Frame

        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text=" Search System",font=("times new roman",11,"bold"))
        table_frame.place(x=5,y=215,width=600,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","Student_id","Name","Division","RollNo","Gender","DOB","Email","Phone","Address","Teacher","PhotoSample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)   #pack scrollbar X and Y
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)  #config Scrollbar X and Y
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Deapartment")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student_id",text="StudentId")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("RollNo",text="RollNo")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("PhotoSample",text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student_id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("RollNo",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("PhotoSample",width=150) 


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ====================Function Decration============================= 
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Apurv@admin#2020",database="student_details")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                             ))


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sussess","Students details has been added Sussessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# ===============================fetch data==================================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Apurv@admin#2020",database="student_details")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ==================================get cursor=======================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

        # ==============================upadate function======================================
    def update_data(self):
        if self.var_dep.get()=="Select Deparatment" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","DO you want this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Apurv@admin#2020",database="student_details")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",( 
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_std_id.get(),
                                                                                                                
                                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Update","Successfully updated student details",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                 


                #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.messagebox.showerror("Error","Student id is must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Apurv@admin#2020",database="student_details")
                    my_cursor=conn.cursor()
                    sql1="DELETE from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql1,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                #rest
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course ")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("Select ")
        self.var_std_name.set(" ")
        self.var_div.set("Select Division ")
        self.var_roll.set(" ")
        self.var_gender.set(" ")
        self.var_dob.set(" ")
        self.var_email.set(" ")
        self.var_phone.set(" ")
        self.var_address.set(" ")
        self.var_teacher.set(" ")
        self.var_radio1.set(" ")


        # search
    def search_data(self):
        if self.var_com_search.get()==""  or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Apurv@admin#2020",database="student_details")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
                    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


# ===================Generate data set or take photo sample===================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Deparatment" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Apurv@admin#2020",database="student_details")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",( 
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
            
        #========Loaad predifiend data on face forntals from opencv==========

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,10)
            #scaling factor=1.3
            #Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(550,550))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def Back(self):
            self.root.destroy()







if __name__ == "__main__":
    root =Tk()
    obj=Student(root)
    root.mainloop()
        

    
        














        



































































        
        
        

       

       

        

    



    