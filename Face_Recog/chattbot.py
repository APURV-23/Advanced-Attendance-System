from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
	def __init__(self,root):
		self.root=root
		self.root.geometry("730x620+0+0")
		self.root.title("ChatBot")
		self.root.bind("<Return>,self.")

		chat_frame=Frame(self.root,bd=2,bg="white",width=610)
		chat_frame.pack()

		img_chat=Image.open('img\chatbot.jfif')
		img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
		self.photoimg=ImageTk.PhotoImage(img_chat)
               
		Title_label=Label(chat_frame,bd=3,relief=RAISED,anchor="nw",width=730,compound=LEFT,image=self.photoimg,text="  CHAT ME",font=("arial",25,"bold"),fg="Blue",bg="white")
		Title_label.pack(side=TOP)

		self.scroll_y=ttk.Scrollbar(chat_frame,orient=VERTICAL)
		self.text=Text(chat_frame,width=65,height=20,bd=3,relief=RAISED,font=("arial",14,"bold"),yscrollcommand=self.scroll_y)
		self.scroll_y.pack(side=RIGHT,fill=Y)
		self.text.pack()

		btn_frame=Frame(self.root,bd=4,bg="white",width=610)
		btn_frame.pack()

		label=Label(btn_frame,text="Type Something",font=("arial",14,"bold"),fg='blue',bg='white')
		label.grid(row=0,column=0,padx=5,sticky=W)

		self.entry=StringVar()
		self.entry1=ttk.Entry(btn_frame,width=40,textvariable=self.entry,font=('arial',15,'bold'))
		self.entry1.grid(row=0,column=1,padx=5,sticky=W)

		self.send=Button(btn_frame,text="Send>>",command=self.send,font=("arial",14,"bold"),width=6,bg="green")
		self.send.grid(row=0,column=2,padx=5,sticky=W)

		self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=("arial",12,"bold"),width=8,bg="red",fg="White")
		self.clear.grid(row=1,column=0,padx=5,sticky=W)

		self.back=Button(btn_frame,text="Back",command=self.Back,font=("arial",14,"bold"),width=6,bg="red",fg="White")
		self.back.grid(row=1,column=2,padx=5,sticky=W)

		

		self.msg=""
		self.label_1=Label(btn_frame,text=self.msg,font=("arial",14,"bold"),fg='red',bg='white')
		self.label_1.grid(row=1,column=1,padx=5,sticky=W)
# ======================Function Declartion===========================

	def enter_fun(self):
		self.send.invoke()
		self.entry.set("")

	def clear(self):
		self.text.delete("1.0",END)
		self.entry.set("")


	def send(self):
		send='\t\t\t'+'You: '+self.entry.get()
		self.text.insert(END,'\n'+send)
		self.text.yview(END)

		if (self.entry.get()==""):
			self.msg="Please enter some input"
			self.label_1.config(text=self.msg,fg="red")

		else:
			self.msg=""
			self.label_1.config(text=self.msg,fg="red")
		
		if (self.entry.get()=="hello"):
			self.text.insert(END,"\n\n"+"Bot: HI")

		elif (self.entry.get()=="Hi"):
			self.text.insert(END,"\n\n"+"Bot: Hello")

		elif (self.entry.get()=="How are you?"):
			self.text.insert(END,"\n\n"+"Bot: fine and you")

		elif (self.entry.get()=="Fantastic"):
			self.text.insert(END,"\n\n"+"Bot: Nice To Hear")
		elif (self.entry.get()=="Who created you?"):
			self.text.insert(END,"\n\n"+"Bot: APURV A. RATHOD did using python")

		elif (self.entry.get()=="What is your name?"):
			self.text.insert(END,"\n\n"+"Bot: My name is Mr.Intell")
		
		elif (self.entry.get()=="Can you speak in Gujrati?"):
			self.text.insert(END,"\n\n"+"Bot: I am still learning it..")

		elif (self.entry.get()=="What is Machine Learning?"):
			self.text.insert(END,"\n\n"+"Bot: Machine learning is the concept that a computer program can learn \n and adapt to new data without human intervention. \n Machine learning is a field of artificial intelligence (AI) that keeps a computer’s built-in algorithms current regardless of changes in the worldwide economy.")

		elif (self.entry.get()=="How does face recognition work?"):
			self.text.insert(END,"\n\n"+"Bot: Step 1: Face detection\nThe camera detects and locates the image of a face, either alone or in a crowd. \nThe image may show the person looking straight ahead or in profile.\nStep 2: Face analysis\nNext, an image of the face is captured and analyzed. \nMost facial recognition technology relies on 2D rather than 3D images because it can more conveniently match a 2D image with public photos or those in a database. \nThe software reads the geometry of your face. Key factors include \n the distance between your eyes, the depth of your eye sockets, the distance from forehead to chin, the shape of your cheekbones, and the contour of the lips,\n ears, and chin. The aim is to identify the facial landmarks that are key \n to distinguishing your face.\nStep 3: Converting the image to data\nThe face capture process transforms analog information (a face) into a set of digital information (data) based on the person's facial features. \nYour face's analysis is essentially turned into a mathematical formula. The numerical code is called a faceprint. \nIn the same way that thumbprints are unique, each person has their own faceprint.\nStep 4: Finding a match")
		
		elif (self.entry.get()=="What is Python Programing?"):
			self.text.insert(END,"\n\n"+"Bot: Python is a multi-paradigm language; it notably supports imperative, object-oriented, and functional programming models. Python functions are objects and can be handled like other objects. \nIn particular, they can be passed as arguments to other functions (also called higher-order functions).\n This is the essence of functional programming.Decorators provide a convenient syntax construct to define higher-order functions.")
		
		elif (self.entry.get()=="What is chatbot?"):
			self.text.insert(END,"\n\n"+"Bot: A chatbot is a software application used to conduct an on-line chat conversation via text or text-to-speech, \nin lieu of providing direct contact with a live human agent.")

		elif (self.entry.get()=="bye"):
			self.text.insert(END,"\n\n"+"Bot: Thanks you For Chatting")

		elif (self.entry.get()=="Help me"):
    			self.text.insert(END,"\n\n"+"Bot: Pls contact our developer and go to help section ")
			

		elif (self.entry.get()=="I have some problem"):
    			self.text.insert(END,"\n\n"+"Bot: Pls contact our developer and go to help section ")

		else:
			self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get it")

	def Back(self):
            self.root.destroy()

		
		




if __name__== "__main__":
	root =Tk()
	obj=ChatBot(root)
	root.mainloop()
        