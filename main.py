import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tkinter import *
from playsound import playsound
import cv2
import os
from tkinter import filedialog
import socket
import sys
from time import sleep
import pyrebase
import csv
from PIL import Image
import numpy as np
from datetime import date
from datetime import datetime
import xlsxwriter
import pandas as pd
import openpyxl
from PIL import ImageTk
import pyodbc
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle


class MainClass(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Facial Recoginition Attendance System")
        self.wm_geometry("650x550")
        self.wm_resizable(False, False)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Login, SignUp, Registration, AttendanceEmployee, SecondPage, ThirdPage, Employee, Show_Employee, Developers):
            frame = F(container, self)

            self.frames[F] = frame
            

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		Label(self, text="Welcome to Facial Attendance System",
              font=("Times New Roman", 25, "bold"), bg="black", fg="white").pack(fill=X)
		photo = PhotoImage(file = 'img1.png')
		l = Label(self, image=photo)
		l.image=photo
		l.pack()

		button_main = ttk.Button(self, text="Login as Admin",command= lambda: controller.show_frame(SecondPage))
		button_main.place(x=490, y=70, width=150, height=40)

		button = ttk.Button(self, text="Login",
                           command=lambda: controller.show_frame(Login))
		button.place(x=490, y=130, width=150, height=40)

		Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)



class SecondPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        Label(self, text="Admin Login Page", font=("Times New Roman",20, 'bold'), bg='black', fg='white').pack(fill=X)
        photo = PhotoImage(file = '1.png')
        l = Label(self, image=photo)
        l.image=photo
        l.pack()
        Label(self, text="Admin Username", font=("Times new Roman", 14, 'bold'), bg='black', fg='white').place(x=100, y=70)
        admin_user = StringVar()
        admin_name = ttk.Entry(self, width=20, textvariable=admin_user)
        admin_name.place(x=260, y=76)

        Label(self, text="Admin Password", font=("Times New Roman", 14, 'bold'), bg='black', fg='white').place(x=100, y=100)
        admin_pass = StringVar()
        admin_password = ttk.Entry(self, width=20, textvariable=admin_pass, show="*")
        admin_password.place(x=260, y=105)

        btn_admin = ttk.Button(self, text="Login", command= lambda: checker())
        btn_admin.place(x=275, y=135)

        btn_back = ttk.Button(self, text="Back", command= lambda: controller.show_frame(StartPage))
        btn_back.place(x=5, y=55)
        Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)
        def checker():
            admin_name_error = admin_user.get()
            admin_pass_error = admin_pass.get()
            if admin_name_error == "":
                messagebox.showerror("Error", "Please Fill The Fields First")
            elif admin_pass_error == "":
                messagebox.showerror("Error","Please Fill The Fields First")
            elif admin_name_error == "AdminUE" and admin_pass_error == "Admin@UE":
                controller.show_frame(ThirdPage)
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
                admin_name.delete(0, END)
                admin_password.delete(0, END)
                
class ThirdPage(tk.Frame):
    
    def __init__(self, parent, controller):
        

        tk.Frame.__init__(self, parent)
        Label(self, text="SignUP or Login", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill=X)
        photo = PhotoImage(file = '1.png')
        l = Label(self, image=photo)
        l.image=photo
        l.pack()

        btn_signUp = ttk.Button(self, text="Signup", command= lambda: controller.show_frame(SignUp))
        btn_signUp.place(x=490, y=70, width=150, height=40)

        btn_login = ttk.Button(self, text="Login", command = lambda: controller.show_frame(Login))
        btn_login.place(x=490, y=130, width=150, height=40)
        Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label(self, text="Login", font=("Times new Roman", 20, "bold"), bg="black", fg="white").pack(fill=X)
        photo = PhotoImage(file = '1.png')
        l = Label(self, image=photo)
        l.image=photo
        l.pack()


        Label(self, text="Username", font=("Times New Roman", 14, "bold"), bg='black', fg='white').place(x=100, y=100)
        user_var = StringVar()
        user = ttk.Entry(self, width=20, textvariable=user_var)
        user.place(x=200, y=101)
        user.focus()

        Label(self, text="Password", font=("Times New Roman", 14, "bold"), bg='black', fg='white').place(x=100, y=130)

        pass_var = StringVar()
        password = ttk.Entry(self, width=20, textvariable=pass_var, show="*")
        password.place(x=200, y=130)

        button2 = ttk.Button(self, text="Login", command=lambda: check())
        button2.place(x=220, y=165)


        button1 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=5, y=50)
        Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)

        def check():
        	conn = sqlite3.connect("Registration.db")
        	c = conn.cursor()
        	c.execute('CREATE TABLE IF NOT EXISTS Login(id integer unique primary key autoincrement, Username TEXT, Password TEXT)')
        	conn.commit()
        	a = user.get()
        	b = password.get()
        	if a == "":
        		 messagebox.showerror("Invalid Input", "Please Enter Username")
        	elif b == "":
        		messagebox.showerror("Invalid Input", "Please Enter Password")
        	else:
        		with sqlite3.connect("Registration.db") as db:
        			cursor=db.cursor()
        		
        		find_user= ("SELECT * FROM Login WHERE Username = ? AND Password = ?")
        		cursor.execute(find_user,[(a),(b)])
        		results=cursor.fetchall()
        		if results:
        			for i in results:
        				controller.show_frame(AttendanceEmployee)
        		else:
        			messagebox.showerror("Invalid", "Invalid Username or Password.")




class AttendanceEmployee(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		Label(self, text="Attendance & Employee Registration", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill="x") 
		photo = PhotoImage(file = 'img1.png')
		l = Label(self, image=photo)
		l.image=photo
		l.pack()          
		btn_emp_reg = ttk.Button(self, text="Register Employee", width=20, command=lambda: controller.show_frame(Registration)).place(x=490, y=50, width=150, height=40)
		btn_attendance = ttk.Button(self, text="Train Model", width=20, command = lambda:trainer()).place(x=490, y=120, width=150, height=40)
		btn_train_ = ttk.Button(self, text="Mark Attendance", width = 20, command = lambda: recognizer()).place(x=490, y=190, width=150, height=40)
		btn_list = ttk.Button(self, text="Employee List", width=20, command = lambda: controller.show_frame(Employee)).place(x=490, y=260, width=150, height=40)
		btn_show_employee = ttk.Button(self, text="Show Attendance", width=20, command = lambda:controller.show_frame(Show_Employee)).place(x=490, y=330, width=150, height=40)
		btn_show_employee = ttk.Button(self, text="Save To Cloud (FireBase)", width=20, command = lambda:cloud()).place(x=490, y=400, width=150, height=40)
		btn_show_employee = ttk.Button(self, text="About Developers", width=20, command = lambda:controller.show_frame(Developers)).place(x=490, y=470, width=150, height=40)
		Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)
		def trainer():
			os.system('py trainer.py')
		def cloud():
			try:
				s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect(('www.google.com',80))
				s.close()
				filename=filedialog.askopenfilename(initialdir ='./Attendance',title='Select a file',filetype=(("csv","*.xlsx"),("All files","*.*")))
				config ={

				"apiKey": "AIzaSyD5XTeUeF33km1uclE6FmGnPNAO67oQ9gQ",
				"authDomain": "attendance-system-3d620.firebaseapp.com",
				"databaseURL": "https://attendance-system-3d620.firebaseio.com",
				"projectId": "attendance-system-3d620",
				"storageBucket": "attendance-system-3d620.appspot.com",
				"messagingSenderId": "853160863868",
				"appId": "1:853160863868:web:a25fb086b553786e9101f9",
				"measurementId": "G-GX9NBVKBCZ"
				}
				if len(filename) > 0:

					firebase=pyrebase.initialize_app(config)
					storage = firebase.storage()
					path_on_cloud= "Attendance/"+os.path.basename(filename)
					storage.child(path_on_cloud).put(filename)
					messagebox.showinfo("Success","Successfully uploaded to Firebase")
				else:
					messagebox.showerror("Error","No file Selected")
			except Exception:
				messagebox.showerror('Error',"You are not connected to internet")
				sleep(1)
				
		def recognizer():
			conn = sqlite3.connect('Registration.db')
			c = conn.cursor()

			fname = "trainer/trainer.yml"
			if not os.path.isfile(fname):
				messagebox.showerror("Error","Please train the data first")
				exit(0)
			Attendance = "Attendance"
			if not os.path.exists(Attendance):
				os.makedirs("Attendance")
			else:
				pass
			face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
			cap = cv2.VideoCapture(0)
			recognizer = cv2.face.LBPHFaceRecognizer_create()
			recognizer.read(fname)
			while True:
				ret, img = cap.read()
				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				faces = face_cascade.detectMultiScale(gray, 1.3, 5)
				for (x,y,w,h) in faces:
					cv2.rectangle(img,(x,y),(x+w-10,y+h-10),(0,255,0),3)
					ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
					c.execute("select employee_name from employee where id = (?);", (ids,))
					result = c.fetchall()
					employee_name = result[0][0]

					c.execute('select * from employee where id = (?);', (ids,))
					result2  = c.fetchall()[0]
					pid_emp = result2[0]
					name_emp = result2[1]
					id_emp = result2[2]
					dept_emp = result2[3]
					status_emp = 'Present'

					date_object = datetime.now()
					date_now = date_object.strftime("%Y-%m-%d")
					time_now = date_object.strftime("%H:%M:%S")

					if conf < 70:
						cv2.putText(img, employee_name, (x+5,y+h-12), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
						
						conn = sqlite3.connect("Registration.db")
						c = conn.cursor()
						c.execute("CREATE TABLE IF NOT EXISTS attendance_sheet(employee_name TEXT, employee_id TEXT, employee_department TEXT, employee_status TEXT, attendance_time TEXT,attendance_date TEXT)");
						c.execute('SELECT * FROM attendance_sheet WHERE employee_name = (?) AND attendance_date = CURRENT_DATE;', (employee_name,))
						rzlt = c.fetchall()
						
						if len(rzlt) > 0:
							cap.release()
							cv2.destroyAllWindows()
							messagebox.showerror('ERROR',"Attendance Already Marked")
								
						
						else:
							c.execute("INSERT INTO attendance_sheet(employee_name, employee_id, employee_department,employee_status, attendance_time, attendance_date) VALUES(?,?,?,?,?,?)",(name_emp, id_emp, dept_emp, status_emp, time_now, date_now))
							#c.execute("INSERT INTO attendance_sheet (attendance_time)VALUES(time(CURRENT_TIME,'localt'))")
							messagebox.showinfo("Success", "Attendance of employee "+name_emp+" is Marked Successfully!")
							playsound('./sound.mp3')
							conn.commit()
							cap.release()
							cv2.destroyAllWindows()							
						c.execute('SELECT * FROM attendance_sheet WHERE attendance_date = CURRENT_DATE')
						attendance_of_employee = c.fetchall()
						conn.commit()
						today = str(date.today())
						try:
							data_emp = [name_emp, id_emp, dept_emp, status_emp]
							data = pd.DataFrame(attendance_of_employee, columns= ['Employee Name','Employee ID', 'Employee Department', 'Attendance', 'Date', 'Time'])
							datatoexcel = pd.ExcelWriter("Attendance/Employee Attendance "+today+".xlsx", engine='xlsxwriter')
							data.to_excel(datatoexcel, index=False, sheet_name = "Sheet")
							worksheet = datatoexcel.sheets['Sheet']
							worksheet.set_column('A:A', 25)
							worksheet.set_column('B:B', 20)
							worksheet.set_column('C:C', 25)
							worksheet.set_column('D:D', 20)
							worksheet.set_column('E:E', 20)
							worksheet.set_column('F:F', 20)
							datatoexcel.save()

						except Exception as e:
							messagebox.showerror('Error', "Data Saved to Database Successfully But xlsx File Is In Use")

					else:
						cv2.putText(img, 'No Match', (x+5,y+h-12), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
						cv2.putText(img,'Hit Enter to exit',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
					cv2.imshow('Face Recognizer',img)
				k = cv2.waitKey(30) & 0xff
				if k == 13:
					cap.release()
					cv2.destroyAllWindows()
					break
				
						

			

class Registration(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label(self, text="Register Employee", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill="x")
        photo = PhotoImage(file = '1.png')
        l = Label(self, image=photo)
        l.image=photo
        l.pack()
        Label(self, text="Employee Name", font=("Times new Roman", 12, 'bold'), bg="black", fg="white").place(x=150, y=70)
        user_emp = StringVar()
        user = ttk.Entry(self, width=20, textvariable=user_emp)
        user.place(x=270, y=70)
        user.focus()

        Label(self, text="Employee ID", font=("Times New Roman", 12, 'bold'), bg="black", fg="white").place(x=150, y=100)

        emp_id = StringVar()
        usr_id = ttk.Entry(self, width=20, textvariable=emp_id)
        usr_id.place(x=270, y=100)


        Label(self, text="Employee Department", font=("Times New Roman", 12, 'bold'), bg="black", fg="white").place(x=110, y=130)
        emp_depart = StringVar()
        emp_dep = ttk.Combobox(self, width=16, textvariable=emp_depart,font=("Times New Roman", 10), state='readonly')
        emp_dep['values'] = ("IT", "Physics", 'Chemistry', 'B.ed',
        'MA(English)','MA(Education)', 'Zology', 'Botany', 'BBA')
        emp_dep.place(x=270, y=130)


        btn_emp = ttk.Button(self, text="Register & Capture", command= lambda: save_emp())
        btn_emp.place(x=270, y=160,width=140, height=40)
        btn_back = ttk.Button(self, text="Back", command= lambda: controller.show_frame(AttendanceEmployee))
        btn_back.place(x=5, y=50)
        Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)


        def save_emp():
            emp_id_error = emp_id.get()
            emp_user_error = user_emp.get()
            emp_depart_error = emp_depart.get()
            name = user.get()

            conn = sqlite3.connect("Registration.db")
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS employee(id integer unique primary key autoincrement, employee_name TEXT, employee_id TEXT, employee_department)")
            uid = c.lastrowid
            conn.commit()
            find_data= ("SELECT * FROM employee WHERE employee_id = ?")
            c.execute(find_data,[(emp_id_error)])
            resultss=c.fetchall()

            if emp_user_error == "":
                messagebox.show("Error", "Employee Name Can't be empty")
            elif emp_id_error == "":
                messagebox.showerror("Error", "Employee ID Can't be empty")
            elif emp_depart_error == "":
                messagebox.showerror("Error", "Employee Department Can't be empty")
                print(emp_depart_error)
            elif len(resultss) >0:
            	messagebox.showerror("Error", "This Employee ID Already Exists")
            else:
                conn = sqlite3.connect('Registration.db')
                c = conn.cursor()
                c.execute('INSERT INTO employee (employee_name, employee_id, employee_department) VALUES (?,?,?)',
                          (user_emp.get(), emp_id.get(), emp_depart.get()))
                
                conn.commit()
                user.delete(0, END)
                usr_id.delete(0, END)
                emp_dep.delete(0, END)

                conn = sqlite3.connect("Registration.db")
                c = conn.cursor()
                c.execute("SELECT max(id) FROM employee")
                max_id = c.fetchone()[0]
                vid_cam = cv2.VideoCapture(0)
                face_detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
                count = 0
                assure_path_exists("dataset/")
                while(True):
                     _,image_frame = vid_cam.read()
                     gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
                     faces = face_detector.detectMultiScale(gray, 1.1, 5)
                     for(x,y,w,h) in faces:
                        cv2.rectangle(image_frame, (x,y), (x+w-10, y+h-10), (255,0,0), 2)
                        count+=1

                        cv2.imwrite("dataset/"+name+"."+str(max_id)+"."+str(count)+".jpg",gray[y:y+h,x:x+w])
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(image_frame,str(count),(0,120), font, 1, (255,255,255), 2, cv2.LINE_AA)
                        cv2.imshow('frame', image_frame)
                     if cv2.waitKey(50) & 0xFF == ord('q'):
                        break
                     elif count >=100:
                        break
                vid_cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Saved", "Data Saved Successfully!")


                
        def assure_path_exists(path):
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)

                
              
class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conn = sqlite3.connect("Registration.db")
        c = conn.cursor()
        Label(self, text="Sign Up", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill=X)
        photo = PhotoImage(file = '1.png')
        l = Label(self, image=photo)
        l.image=photo
        l.pack()

        Label(self, text="First Name", font=("Times New Roman", 12, 'bold'), bg="black", fg="white").place(x=150, y=70)

        fname_var = StringVar()
        frist_name = ttk.Entry(self, width=20, textvariable=fname_var)
        frist_name.place(x=240, y=70)
        frist_name.focus()

        Label(self, text="Last Name", font=("Times New Roman", 12, 'bold'), bg="black", fg="white").place(x=150, y=100)

        lname_var = StringVar()
        last_name = ttk.Entry(self, width=20, textvariable=lname_var)
        last_name.place(x=240, y=100)
        Label(self, text="Username", font=("Times New Roman", 12, 'bold'), bg="black", fg="white").place(x=150, y=130)

        usr_var = StringVar()
        user_name = ttk.Entry(self, width=20, textvariable=usr_var)
        user_name.place(x=240, y=130)

        Label(self, text="Password", font=("Times New Roman", 12, 'bold'), bg="black", fg="white").place(x=150, y=160)

        pass_var = StringVar()
        passwor = ttk.Entry(self, width=20, textvariable=pass_var, show="*")
        passwor.place(x=240, y=160)

        Label(self, text="Confirm Password", font=("Times New Roman", 12, 'bold'), bg="black", fg="white").place(x=100, y=190)

        conpass_var = StringVar()
        con_pass = ttk.Entry(self, width=20, textvariable=conpass_var, show="*")
        con_pass.place(x=240, y=190)

        btn_sign = ttk.Button(self, text="Signup", command = lambda: save())
        btn_sign.place(x=240, y=220,width=110, height=40)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=5, y=50)

        button2 = ttk.Button(self, text="Go to Login Page",
                            command=lambda: controller.show_frame(Login))
        button2.place(x=240, y=270, width=110, height=40)
        Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)
        def save():
            user_error = usr_var.get()
            lname_error = lname_var.get()
            fname_error = fname_var.get()
            pass_error = pass_var.get()
            conpass_error = conpass_var.get()

            if fname_error == "":
                messagebox.showinfo("Invalid Input", "Please Enter First Name")
            elif lname_error == "":
                messagebox.showinfo("Invalid Input", "Please Enter Last Name")
            elif user_error == "":
                messagebox.showinfo("Invalid Input", "Please Enter Username")
            elif pass_error == "":
                messagebox.showinfo("Invalid Input", "Please Enter Password")
            elif conpass_error == "":
                messagebox.showinfo("Invalid Input", "Please Enter Confirm Password")
            elif pass_error != conpass_error:
                messagebox.showinfo("Invalid Input", "Password Does Not Matches")
            else:
                conn=sqlite3.connect('Registration.db')
                c=conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS Signup(id integer unique primary key autoincrement, frist_name TEXT, last_name TEXT, Username TEXT)")
                c.execute("INSERT INTO Signup(frist_name, last_name, Username) VALUES (?,?,?)", (fname_var.get(), lname_var.get(), usr_var.get()))
                c.execute('CREATE TABLE IF NOT EXISTS Login(id integer unique primary key autoincrement, Username TEXT, Password TEXT)')
                c.execute('INSERT INTO Login(Username, Password) VALUES(?,?)', (usr_var.get(), pass_var.get()))
                conn.commit()
                messagebox.showinfo("Saved", "Data Saved Successfully!")
                frist_name.delete(0, END)
                last_name.delete(0,END)
                user_name.delete(0,END)
                passwor.delete(0,END)
                con_pass.delete(0,END)


class Employee(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		Label(self, text="Employee's Data", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill="x")
		photo = PhotoImage(file = '1.png')
		l = Label(self, image=photo)
		l.image=photo
		l.pack()
		conn = sqlite3.connect('Registration.db')
		c = conn.cursor()
		rows = c.fetchall()
		tree = ttk.Treeview(self)
		tree["columns"]=("one","two","three", "four")
		tree.column("#0", width=0, minwidth=50, stretch=tk.NO)
		tree.column("one", width=50, minwidth=50, stretch=tk.NO)
		tree.column("two", width=150, minwidth=150)
		tree.column("three", width=150, minwidth=150, stretch=tk.NO)
		tree.column("four", width=150, minwidth=150, stretch=tk.NO)
		tree.heading("#0",text="index",anchor=tk.W)
		tree.heading("one", text="ID",anchor=tk.W)
		tree.heading("two", text="Employee Name",anchor=tk.W)
		tree.heading("three", text="Employee ID",anchor=tk.W)
		tree.heading("four", text="Employee Department", anchor= tk.W)
		tree.place(x=5, y=80, width=650)
		
		
		btn_view_data = ttk.Button(self, text="Show Data", width=20, command= lambda: view())
		btn_view_data.place(x= 110, y=350, width=100, height=40)


		clear_btn = ttk.Button(self, width=20, text="Refresh", command= lambda:refresh())
		clear_btn.place(x= 470, y=350, width=100, height=40)

		btn_dlt = ttk.Button(self, text="Delete User", width=20, command= lambda: dlt())
		btn_dlt.place(x= 290, y=350, width=100, height=40)

		btn_view_data = ttk.Button(self, text="Save to PDF", width=20, command= lambda: pdf())
		btn_view_data.place(x= 110, y=400, width=100, height=40)

		btn_view_data = ttk.Button(self, text="Save to Xlsx", width=20, command= lambda: xlsx())
		btn_view_data.place(x= 290, y=400, width=100, height=40)
		
		btn_back = ttk.Button(self, text="Back", width=12, command = lambda:controller.show_frame(AttendanceEmployee))
		btn_back.place(x=5, y=50)
		Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)

		def pdf():
			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			c.execute('SELECT * FROM employee')
			data_employee = c.fetchall()
			counter = len(tree.get_children())
			if counter == 0:
				messagebox.showerror("Error", "No Data Availble in Table")
			else:
				if not os.path.exists('./Employee Data PDF'):
					os.makedirs('./Employee Data PDF')
				today = str(date.today())
				pdf = SimpleDocTemplate("./Employee Data PDF/Employee List "+today+".pdf")
				flow_obj = []
				td = [['ID','Employee Name', "Employee ID", "Employee Department"]]
				for i in data_employee:
					td.append(i)
				table = Table(td)
				flow_obj.append(table)
				pdf.build(flow_obj)
				messagebox.showinfo("Success", "PDF generated Successfully")

		def xlsx():
			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			c.execute('SELECT * FROM employee')
			data_employee = c.fetchall()
			counter = len(tree.get_children())
			today = str(date.today())
			if counter == 0:
				messagebox.showerror("Error", "No Data Availble in Table")
			else:
				if not os.path.exists('./Employee Data Excel'):
					os.makedirs('./Employee Data Excel')
				data = pd.DataFrame(data_employee, columns= ['ID','Employee Name', 'Employee ID', 'Employee Department'])
				datatoexcel = pd.ExcelWriter("Employee Data Excel/Employee List "+today+".xlsx", engine='xlsxwriter')
				data.to_excel(datatoexcel, index=False, sheet_name = "Sheet")
				worksheet = datatoexcel.sheets['Sheet']
				worksheet.set_column('A:A', 25)
				worksheet.set_column('B:B', 20)
				worksheet.set_column('C:C', 25)
				worksheet.set_column('D:D', 20)
				datatoexcel.save()
				messagebox.showinfo("Success", "Excel File is Generated Successfully")

		def view():
			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			c.execute('SELECT * FROM employee')
			data_employee = c.fetchall()
			counter = len(tree.get_children())

			if counter == 0:
				for employee in data_employee:
					tree.insert("", tk.END, values= employee)
				conn.close()
			else:
				messagebox.showerror("Error", "Data Already Shown")

		def refresh():
			for i in tree.get_children():
				tree.delete(i)
			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			c.execute('SELECT * FROM employee')
			data_employee = c.fetchall()
			for employee in data_employee:
				tree.insert("", tk.END, values= employee)
			conn.close()


		def dlt():
			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			try:
				id = tree.item(tree.selection())['values']
				dlt_id = id[2]
				c.execute("DELETE FROM employee WHERE employee_id=?;", ([(dlt_id)]))
				messagebox.showinfo('Success', 'Record Deleted Successfully Please Refresh To See Changes')
				conn.commit()
				conn.close()
			except IndexError as e:
				messagebox.showerror("Error", "Please Select A Record")
				return


class Show_Employee(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		Label(self, text="Employee Attendance", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill=X)
		photo = PhotoImage(file = '1.png')
		l = Label(self, image=photo)
		l.image=photo
		l.pack()
		Label(self, text="Seach Employee By Entering Employee ID", font=("Times New Roman", 10, 'bold'), bg="black", fg="white").place(x=50, y=100)
	
		search_id = StringVar()
		search_box = ttk.Entry(self, width=20, textvariable= search_id)
		search_box.focus()
		search_box.place(x=300, y=100)
		search_btn = ttk.Button(self, text="Search By ID", command= lambda:search_by_id())
		search_btn.place(x=450, y=90, width=140, height=40)

		Label(self, text="Seach Employee By Entering Date as YYYY-MM-DD", font=("Times New Roman", 10, 'bold'), bg="black", fg="white").place(x=5, y=150)
		search_date = StringVar()
		search_box = ttk.Entry(self, width=20, textvariable= search_date)
		search_box.focus()
		search_box.place(x=300, y=150)
		search_btn_date = ttk.Button(self, width=20, text="Search By Date", command= lambda:search_by_date())
		search_btn_date.place(x=450, y=140, width=140, height=40)

		tree_scnd = ttk.Treeview(self)
		tree_scnd["columns"] = ("one", "two", "three", "four", "five", "six")
		tree_scnd.column("#0", width=0, minwidth=0, stretch=tk.NO)
		tree_scnd.column("one", width=100, minwidth=100, stretch= tk.NO)
		tree_scnd.column("two", width=100, minwidth=100, stretch=tk.NO)
		tree_scnd.column("three", width=150, minwidth=100, stretch=tk.NO)
		tree_scnd.column("four", width=100, minwidth= 100, stretch=tk.NO)
		tree_scnd.column("five", width=100, minwidth=100, stretch=tk.NO)
		tree_scnd.column("six", width=100, minwidth=100, stretch=tk.NO)

		tree_scnd.heading("#0",text="index", anchor= tk.W)
		tree_scnd.heading("one", text="Employee Name", anchor=tk.W)
		tree_scnd.heading("two", text="Employee ID", anchor=tk.W)
		tree_scnd.heading("three", text="Employee Department", anchor=tk.W)
		tree_scnd.heading("four", text="Employee Status", anchor=tk.W)
		tree_scnd.heading("five", text="Attendance Date", anchor=tk.W)
		tree_scnd.heading("six", text="Attendance Time", anchor=tk.W)

		tree_scnd.place(x=0, y=200)
		
		clear_btn = ttk.Button(self, width=20, text="Save to Xlsx", command= lambda:xlsx())
		clear_btn.place(x=100, y=450, width=140, height=40)
		clear_btn = ttk.Button(self, width=20, text="Save to PDF", command= lambda:pdf())
		clear_btn.place(x=270, y=450, width=140, height=40)
		clear_btn = ttk.Button(self, width=20, text="Clear All", command= lambda:clear())
		clear_btn.place(x=450, y=450, width=140, height=40)
		
		btn_back = ttk.Button(self, text="Back", width=15, command = lambda:controller.show_frame(AttendanceEmployee))
		btn_back.place(x=5, y=50)
		Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)
		
		def xlsx():
			counter_data = len(tree_scnd.get_children())
			today = str(date.today())
			if counter_data == 0:
				messagebox.showerror("Error", "No Data is Availble in Table")
			else:
				for line in tree_scnd.get_children():
					data_emp_table = []
					for value in tree_scnd.item(line)['values']:
						data_emp_table += [value]
				if not os.path.exists('./Saved Employee Attendance Excel'):
					os.makedirs('./Saved Employee Attendance Excel')
				data = pd.DataFrame([data_emp_table], columns= ['Employee Name','Employee ID', 'Employee Department', 'Attendance', 'Date', 'Time'])
				datatoexcel = pd.ExcelWriter("Saved Employee Attendance Excel/Employee List "+today+".xlsx", engine='xlsxwriter')
				data.to_excel(datatoexcel, index=False, sheet_name = "Sheet")
				worksheet = datatoexcel.sheets['Sheet']
				worksheet.set_column('A:A', 25)
				worksheet.set_column('B:B', 20)
				worksheet.set_column('C:C', 25)
				worksheet.set_column('D:D', 20)
				worksheet.set_column('E:E', 20)
				worksheet.set_column('F:F', 20)
				datatoexcel.save()
				messagebox.showinfo("Success", "Excel File is Generated Successfully")


		def pdf():
			counter_data = len(tree_scnd.get_children())
			today = str(date.today())
			if counter_data == 0:
				messagebox.showerror("Error", "No Data is Availble in Table")
			else:
				for line in tree_scnd.get_children():
					data_emp_table = []
					for value in tree_scnd.item(line)['values']:
						data_emp_table += [value]
				if not os.path.exists('./Saved Employee Attendance PDF'):
					os.makedirs('./Saved Employee Attendance PDF')

				pdf = SimpleDocTemplate("./Saved Employee Attendance PDF/Employee List "+today+".pdf")
				flow_obj = []
				td = [['Employee Name','Employee ID', 'Employee Department', 'Attendance', 'Date', 'Time']]
				for i in [data_emp_table]:
					td.append(i)
				table = Table(td)
				flow_obj.append(table)
				pdf.build(flow_obj)
				messagebox.showinfo("Success", "PDF generated Successfully")
		
		def search_by_id():
			for i in tree_scnd.get_children():
				tree_scnd.delete(i)
			id_error = search_id.get()

			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			id_search = str(search_id.get())
			find_data= ("SELECT * FROM attendance_sheet WHERE employee_id = ?")
			c.execute(find_data,[(id_search)])
			resultss=c.fetchall()
			counter_data = len(tree_scnd.get_children())

			if id_error == "":
				messagebox.showerror("Error", "Please Enter Employee ID")
			
			elif len(resultss) ==0:
				messagebox.showerror("Error", "Invalid ID or Employee Does Not Exists")

			elif counter_data == 0:
				for r in resultss:
					tree_scnd.insert("", tk.END, values=r)

		def clear():
			for i in tree_scnd.get_children():
				tree_scnd.delete(i)

		def search_by_date():
			for i in tree_scnd.get_children():
				tree_scnd.delete(i)
			date_error = search_date.get()

			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			date_search = str(search_date.get())
			if date_search == "":
				messagebox.showerror("Error", "Please Enter Date")
			else:
				searched_date = datetime.strptime(date_search, '%Y-%m-%d').date()
				find_data= ("SELECT * FROM attendance_sheet WHERE attendance_date = ?")
				c.execute(find_data,[(searched_date)])
				results_data=c.fetchall()

				counter_date = len(tree_scnd.get_children())
			
			
				if len(results_data) == 0:
					messagebox.showerror("Error", "Please Enter a Valid Date or Record Does not Exists")
				if counter_date == 0:
					for r in results_data:
						tree_scnd.insert("", tk.END, values=r)

class Developers(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		Label(self, text="About Us", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill=X)
		btn_back = ttk.Button(self, text="Back", width=15, command = lambda:controller.show_frame(AttendanceEmployee))
		btn_back.place(x=5, y=50)
		
		photo = PhotoImage(file = 'haider.png')
		l = Label(self, image=photo)
		l.image=photo
		l.pack()
		btn_back = ttk.Button(self, text="Back", width=15, command = lambda:controller.show_frame(AttendanceEmployee))
		btn_back.place(x=5, y=50)
		Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)

app = MainClass()
app.mainloop()
