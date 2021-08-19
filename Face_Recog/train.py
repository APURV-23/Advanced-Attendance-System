from tkinter import*
from  tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import numpy as np
from numpy.lib.type_check import imag
import tkinter





class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1368x768+0+0")
        self.root.title("Students Details")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",20,"bold"),bg="yellow",fg="orange")
        title_lbl.place(x=0,y=0,width=1368,height=35)

        img_top=Image.open(r'img\facialrecognition.png')
        img_top=img_top.resize((1368,280),Image.ANTIALIAS)#High level to low
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=1368,height=280)

        # button

        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="yellow",fg="orange")
        b1_1.place(x=0,y=315,width=1368,height=50)

        img_bottom=Image.open(r'img\leaderphoto.jfif')
        img_bottom=img_bottom.resize((1368,320),Image.ANTIALIAS)#High level to low
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=360,width=1368,height=320)

        #BACK
        exitimg=Image.open(r'img\exit.jpg')
        exitimg=exitimg.resize((50,35),Image.ANTIALIAS)#High level to low
        self.photoimg11=ImageTk.PhotoImage(exitimg)

        b1_1=Button(self.root,text="Back ",cursor="hand2",command=self.Back,font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_1.place(x=1310,y=0,width=50,height=35)

    # def faceDetection(test_img):             
    #         gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    #         face_haar=cv2.CascadeClassifier(r'haarcascade_frontalface_alt.xml') #Give path to haar classifier as i have given
    #         faces=face_haar.detectMultiScale(gray_img,scaleFactor=1.2,minNeighbors=3)
    #         return faces,gray_img

    #     #Labels for training data has been created

    # def labels_for_training_data(directory):
    #         faces=[]
    #         faceID=[]
            

    #         for path,subdirnames,filenames in os.walk(directory):
    #             for filename in filenames:
    #                 if filename.startswith("."):
    #                     print("skipping system file")
    #                     continue
    #                 id=os.path.basename(path)
    #                 img_path=os.path.join(path,filename)
    #                 print ("img_path",img_path)
    #                 print("id: ",id)
    #                 test_img=cv2.imread(img_path)
    #                 if test_img is None:
    #                     print ("Not Loaded Properly")
    #                     continue

    #                 faces_rect,gray_img=faceDetection(test_img)
    #                 if len(faces_rect)!=1:
    #                     continue
    #                 (x,y,w,h)=faces_rect[0]
    #                 roi_gray=gray_img[y:y+w,x:x+h]
    #                 faces.append(roi_gray)
    #                 faceID.append(int(id))
    #         return faces,faceID


    #     #Here training Classifier is called
    # def train_classifier(faces,faceID):                              
    #         face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    #         face_recognizer.train(faces,np.array(faceID))
    #         return face_recognizer


    #     #Drawing a Rectangle on the Face Function
    # def draw_rect(test_img,face):                                      
    #         (x,y,w,h)=face
    #         cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),thickness=3)

    #     #Putting text on images
    # def put_text(test_img,text,x,y):                                    
    #         cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,3,(255,0,0),6)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #gray scale image here
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ======= Train the classifier and save=======================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!",parent=self.root)

            
    
    def Back(self):
            self.root.destroy()






        




if __name__ == "__main__":
    root =Tk()
    obj=Train(root)
    root.mainloop()