import tkinter as tk
from tkinter import ttk
import sqlite3
import re
import random
from tkinter import messagebox
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import smtplib
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

        for F in (StartPage, Login, SignUp, Registration, AttendanceEmployee, SecondPage, ThirdPage, Employee, Show_Employee, Developers, Email):
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
		conn = sqlite3.connect("Registration.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS employee(id integer unique primary key autoincrement, employee_name TEXT, employee_id TEXT, employee_department, employee_email TEXT)")
		c.execute("CREATE TABLE IF NOT EXISTS absent_employee(employee_name TEXT, employee_id TEXT, employee_department, employee_status TEXT, attendance_date TEXT, attendance_time TEXT)")
		c.execute('CREATE TABLE IF NOT EXISTS Login(id integer unique primary key autoincrement, Username TEXT, Password TEXT)')
		c.execute("CREATE TABLE IF NOT EXISTS attendance_sheet(employee_name TEXT, employee_id TEXT, employee_department TEXT, employee_status TEXT, attendance_date TEXT,attendance_time TEXT)");
		c.execute("CREATE TABLE IF NOT EXISTS Signup(id integer unique primary key autoincrement, frist_name TEXT, last_name TEXT, Username TEXT)")
		c.execute('CREATE TABLE IF NOT EXISTS Login(id integer unique primary key autoincrement, Username TEXT, Password TEXT)')


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
            elif admin_name_error == "ali" and admin_pass_error == "ali@UE":
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
		btn_attendance = ttk.Button(self, text="Train Model", width=20, command = lambda:trainer()).place(x=490, y=110, width=150, height=40)
		btn_train_ = ttk.Button(self, text="Mark Attendance", width = 20, command = lambda: recognizer()).place(x=490, y=170, width=150, height=40)
		btn_list = ttk.Button(self, text="Employee List", width=20, command = lambda: controller.show_frame(Employee)).place(x=490, y=230, width=150, height=40)
		btn_show_employee = ttk.Button(self, text="Show Attendance", width=20, command = lambda:controller.show_frame(Show_Employee)).place(x=490, y=290, width=150, height=40)
		btn_show_employee = ttk.Button(self, text="Save To Cloud (FireBase)", width=20, command = lambda:cloud()).place(x=490, y=350, width=150, height=40)
		btn_show_employee = ttk.Button(self, text="Send Email", width=20, command = lambda:controller.show_frame(Email)).place(x=490, y=410, width=150, height=40)
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
					try:
						employee_name = result[0][0]
					except IndexError:
						messagebox.showerror("Error", "Employee Does Not Exists Or Train Model Again")
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
						
						c.execute('SELECT * FROM attendance_sheet WHERE employee_name = (?) AND attendance_date = CURRENT_DATE;', (employee_name,))
						rzlt = c.fetchall()
						if len(rzlt) > 0:
							cap.release()
							cv2.destroyAllWindows()
							messagebox.showerror('ERROR',"Attendance Already Marked")
								
						
						else:
							
							c.execute("SELECT attendance_date FROM absent_employee ORDER BY employee_id DESC LIMIT 1;")
							last_record = c.fetchall()
							c.execute("SELECT * FROM absent_employee")
							i = c.fetchall()

							if len(i) == 0:
								c.execute("INSERT INTO absent_employee(employee_name, employee_id, employee_department) SELECT employee_name, employee_id, employee_department FROM employee")
								c.execute("UPDATE absent_employee SET attendance_date = :attend_date WHERE attendance_date IS NULL", {'attend_date': date_now})
								conn.commit()
							
							elif last_record[0][0] == None or len(i) >0:
								try:
									last_record_dat = last_record[0][0]
									date_record = datetime.strptime(str(last_record_dat), '%Y-%m-%d').date()
								except ValueError as e:
									pass
								current_date = datetime.strptime(date_now, '%Y-%m-%d').date()									
								if date_record != current_date:
										c.execute("INSERT INTO absent_employee(employee_name, employee_id, employee_department) SELECT employee_name, employee_id, employee_department FROM employee")

								if len(i) > 0:
									c.execute("SELECT * FROM absent_employee WHERE employee_id = (?)", (id_emp,))
									x = c.fetchall()
									if len(x) == 0:
										c.execute("INSERT INTO absent_employee(employee_name, employee_id, employee_department, attendance_date) VALUES (?,?,?,?)", (name_emp, id_emp, dept_emp,date_now))
								
								c.execute("INSERT INTO attendance_sheet(employee_name, employee_id, employee_department,employee_status, attendance_date, attendance_time) VALUES(?,?,?,?,?,?)",(name_emp, id_emp, dept_emp, status_emp, date_now, time_now))
								c.execute("UPDATE absent_employee SET employee_status = 'ABSENT' WHERE NOT employee_id = :emp_rec_id AND employee_status IS NULL", {'emp_rec_id': id_emp})
								c.execute("UPDATE absent_employee SET attendance_time  = 'N/A' WHERE NOT employee_id = :emp_rec_id AND attendance_time  IS NULL", {'emp_rec_id': id_emp})
								c.execute("UPDATE absent_employee SET attendance_date = :attend_date WHERE attendance_date IS NULL", {'attend_date': date_now})
								c.execute("UPDATE absent_employee SET employee_status = 'PRESENT' WHERE employee_id = :emp_rec_id AND employee_status = 'ABSENT' OR employee_status IS NULL", {'emp_rec_id': id_emp})
								c.execute("UPDATE absent_employee SET attendance_time  = :attend_time WHERE employee_id = :emp_rec_id AND attendance_time = 'N/A' OR attendance_time IS NULL", {'emp_rec_id': id_emp, 'attend_time': time_now})
								messagebox.showinfo("Success", "Attendance of employee "+name_emp+" is Marked Successfully!")
								playsound('./sound.mp3')
								conn.commit()
							
								try:
									date_object = datetime.now()
									date_now = date_object.strftime("%Y-%m-%d")
									time_now = date_object.strftime("%H:%M:%S")
									c.execute('select employee_email from employee where id = (?);', (ids,))
									receiver_email = c.fetchall()[0][0]
									c.execute('select employee_name from employee where id = (?);', (ids,))
									receiver_name = c.fetchall()[0][0]
									sender_email = 'pydeveloper000@gmail.com'
									sender_password = 'fypproject'
									server = smtplib.SMTP('smtp.gmail.com', 587)
									server.ehlo()
									server.starttls()
									server.login(sender_email, sender_password)
									attendance_mail = "Hello There "+receiver_name+", Your Attendance is marked Successfully of the date "+date_now+" ."
									message = 'Subject: Attendance Marked \n{}'.format(attendance_mail)
									server.sendmail(sender_email,receiver_email,message)
									server.quit()
									messagebox.showinfo("Success", "Attendance Marked And Mail is Successfully Sent To The Employee")
								except:
									messagebox.showerror("Error", "Attendance Marked But Email Doesn't Sent Because Something Went Wrong")							

							# elif True:
							# 		try:
							# 			last_record_date = last_record[0][0]
							# 		except ValueError as e:
							# 			pass
							# 		date_record = datetime.strptime(str(last_record_date), '%Y-%m-%d').date()
							# 		current_date = datetime.strptime(date_now, '%Y-%m-%d').date()
							# 		if date_record != current_date:
							# 			c.execute("INSERT INTO absent_employee(employee_name, employee_id, employee_department) SELECT employee_name, employee_id, employee_department FROM employee")
							# 			conn.commit()

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

        Label(self, text="Employee Email", font=("Times New Roman", 12, 'bold'), bg="black", fg="white").place(x=150, y=160)

        emp_email = StringVar()
        usr_email = ttk.Entry(self, width=20, textvariable=emp_email)
        usr_email.place(x=270, y=160)

        btn_emp = ttk.Button(self, text="Register & Capture", command= lambda: save_emp())
        btn_emp.place(x=270, y=190,width=140, height=40)
        btn_back = ttk.Button(self, text="Back", command= lambda: controller.show_frame(AttendanceEmployee))
        btn_back.place(x=5, y=50)
        Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)


        def save_emp():

            emp_id_error = emp_id.get()
            emp_user_error = user_emp.get()
            emp_depart_error = emp_depart.get()
            name = user.get()
            emp_email_error = emp_email.get()

            email = str(emp_email.get())

            conn = sqlite3.connect("Registration.db")
            c = conn.cursor()
            
            uid = c.lastrowid
            conn.commit()
            find_data= ("SELECT * FROM employee WHERE employee_id = ?")
            c.execute(find_data,[(emp_id_error)])
            resultss=c.fetchall()
            match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b', email, re.I)

            if emp_user_error == "":
                messagebox.showerror("Error", "Employee Name Can't be empty")

            elif emp_id_error == "":
                messagebox.showerror("Error", "Employee ID Can't be empty")

            elif len(emp_depart_error) == 0:
                messagebox.showerror("Error", "Employee Department Can't be empty")

            elif len(resultss) >0:
            	messagebox.showerror("Error", "This Employee ID Already Exists")

            elif emp_email_error == "":
                messagebox.showerror("Error", "Employee Email Can't be empty")
           
            elif match == None:
                messagebox.showerror("Error", "Invalid Email Address")

            else:
                conn = sqlite3.connect('Registration.db')
                c = conn.cursor()
                c.execute('INSERT INTO employee (employee_name, employee_id, employee_department, employee_email) VALUES (?,?,?,?)',
                          (user_emp.get(), emp_id.get(), emp_depart.get(), emp_email.get()))
                conn.commit()
                user.delete(0, END)
                usr_id.delete(0, END)
                emp_dep.delete(0, END)
                usr_email.delete(0, END)


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
                messagebox.showerror("Invalid Input", "Please Enter First Name")
            elif lname_error == "":
                messagebox.showerror("Invalid Input", "Please Enter Last Name")
            elif user_error == "":
                messagebox.showerror("Invalid Input", "Please Enter Username")
            elif pass_error == "":
                messagebox.showerror("Invalid Input", "Please Enter Password")
            elif conpass_error == "":
                messagebox.showerror("Invalid Input", "Please Enter Confirm Password")
            elif pass_error != conpass_error:
                messagebox.showinfo("Invalid Input", "Password Does Not Matches")
            else:
                conn=sqlite3.connect('Registration.db')
                c=conn.cursor()
                
                c.execute("INSERT INTO Signup(frist_name, last_name, Username) VALUES (?,?,?)", (fname_var.get(), lname_var.get(), usr_var.get()))
                
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
		tree["columns"]=("one","two","three", "four", "five")
		tree.column("#0", width=0, minwidth=50, stretch=tk.NO)
		tree.column("one", width=50, minwidth=50, stretch=tk.NO)
		tree.column("two", width=70, minwidth=70)
		tree.column("three", width=100, minwidth=100, stretch=tk.NO)
		tree.column("four", width=150, minwidth=150, stretch=tk.NO)
		tree.column("five", width=170, minwidth=170, stretch=tk.NO)

		tree.heading("#0",text="index",anchor=tk.W)
		tree.heading("one", text="ID",anchor=tk.W)
		tree.heading("two", text="Employee Name",anchor=tk.W)
		tree.heading("three", text="Employee ID",anchor=tk.W)
		tree.heading("four", text="Employee Department", anchor= tk.W)
		tree.heading("five", text="Employee Email", anchor= tk.W)
		tree.place(x=5, y=80, width=650)
		
		
		btn_view_data = ttk.Button(self, text="Show Data", width=20, command= lambda: view())
		btn_view_data.place(x= 110, y=350, width=100, height=40)


		clear_btn = ttk.Button(self, width=20, text="Refresh", command= lambda:refresh())
		clear_btn.place(x= 470, y=350, width=100, height=40)

		clear_btn = ttk.Button(self, width=20, text="Update Data", command= lambda:update())
		clear_btn.place(x= 470, y=400, width=100, height=40)


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
				td = [['ID','Employee Name', "Employee ID", "Employee Department", "Employee Email"]]
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
				data = pd.DataFrame(data_employee, columns= ['ID','Employee Name', 'Employee ID', 'Employee Department', 'Employee Email'])
				datatoexcel = pd.ExcelWriter("Employee Data Excel/Employee List "+today+".xlsx", engine='xlsxwriter')
				data.to_excel(datatoexcel, index=False, sheet_name = "Sheet")
				worksheet = datatoexcel.sheets['Sheet']
				worksheet.set_column('A:A', 25)
				worksheet.set_column('B:B', 20)
				worksheet.set_column('C:C', 25)
				worksheet.set_column('D:D', 20)
				worksheet.set_column('E:E', 25)
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

		def update():
			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			try:
				id = tree.item(tree.selection())['values']
				dlt_id = id[2]
				c.execute("SELECT * FROM employee WHERE employee_id=?;", ([(dlt_id)]))
				all_data = c.fetchall()
				update_id= all_data[0][0]
				old_name = all_data[0][1]
				old_email = all_data[0][4]
				top = Tk()
				top.geometry("300x400")
				top.title("Update Record")
				frame = Frame(top)
				Label(top, text="Update Data", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill="x")

				Label(top, text="Employee's Previous Name").pack()
				Entry(top, width=30, textvariable=StringVar(top, value=old_name), state='readonly').pack()

				Label(top, text="Employee's New Name").pack()
				new_value_name_var = StringVar()
				new_value_name = ttk.Entry(top, width=30, textvariable= new_value_name_var)
				new_value_name.pack()

				Label(top, text="Employee's Previous Email").pack()
				Entry(top, width=30, textvariable=StringVar(top, value=old_email), state='readonly').pack()
				
				Label(top, text="Employee's New Email").pack()
				new_value_email_var = StringVar()
				new_value_email = ttk.Entry(top, width=30, textvariable= new_value_email_var)
				new_value_email.pack()
				
				btn_update = ttk.Button(top, width=12, text="Update", command= lambda:update_record(old_name, old_email, new_value_name.get(), new_value_email.get()))
				btn_update.pack()
				frame.pack()
				
				def update_record(name, email, new_name, new_email):

					match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b', new_email, re.I)

					if new_name == "":
						messagebox.showerror("Error", "Please Enter Name")
					elif new_email == "":
						messagebox.showerror("Error", "Please Enter Email")
					elif match == None:
						messagebox.showerror("Error", "Invalid Email Address")
					else:
						conn = sqlite3.connect("Registration.db")
						c = conn.cursor()
						c.execute('UPDATE employee SET employee_name = :new_name WHERE employee_name = :name',{'name': name, "new_name": new_name})
						c.execute('UPDATE employee SET employee_email = :new_email WHERE employee_email = :email',{'email': email, "new_email": new_email})
						conn.commit()
						messagebox.showinfo("Success", "Record Is Updated Successfully Please Refresh To See Changes.")
						top.destroy()

			except IndexError as e:
				messagebox.showerror("Error", "Please Select A Record")



class Show_Employee(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		Label(self, text="Employee Attendance", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill=X)
		photo = PhotoImage(file = '1.png')
		l = Label(self, image=photo)
		l.image=photo
		l.pack()
		Label(self, text="Seach Employee By Entering Employee ID", font=("Times New Roman", 10, 'bold'), bg="black", fg="white").place(x=50, y=90)
	
		search_id = StringVar()
		search_box1 = ttk.Entry(self, width=20, textvariable= search_id)
		search_box1.focus()
		search_box1.place(x=300, y=90)
		search_btn = ttk.Button(self, text="Search By Id", command= lambda:search_by_id())
		search_btn.place(x=470, y=90, width=140, height=30)

		Label(self, text="Seach Employee By Entering Date as YYYY-MM-DD", font=("Times New Roman", 10, 'bold'), bg="black", fg="white").place(x=5, y=150)
		search_date = StringVar()
		search_box2 = ttk.Entry(self, width=20, textvariable= search_date)
		search_box2.focus()
		search_box2.place(x=300, y=150)
		search_btn_date = ttk.Button(self, width=20, text="Search By Date", command= lambda:search_by_date())
		search_btn_date.place(x=470, y=150, width=140, height=30)

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
		clear_btn.place(x=100, y=450, width=140, height=30)
		clear_btn = ttk.Button(self, width=20, text="Save to PDF", command= lambda:pdf())
		clear_btn.place(x=270, y=450, width=140, height=30)
		clear_btn = ttk.Button(self, width=20, text="Clear All", command= lambda:clear())
		clear_btn.place(x=450, y=450, width=140, height=30)

		btn_back = ttk.Button(self, text="Back", width=15, command = lambda:controller.show_frame(AttendanceEmployee))
		btn_back.place(x=5, y=50)
		Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)
		
		def xlsx():
			i = random.randint(0,1000)
			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			counter_data = len(tree_scnd.get_children())
			today = str(date.today())
			id_error = search_id.get()
			date_error = search_date.get()
			date_another_error = str(date_error)
			if counter_data != 0:
				if id_error == 0 and date_error == 0:
					messagebox.showerror("Error", "Please Insert Date Or Id")
				elif id_error !=0 or date_error !=0:
					if id_error !=0:
						id_search = str(search_id.get())
						c.execute("SELECT * FROM absent_employee WHERE employee_id = (?)", (id_search,))
						resultss_id=c.fetchall()
						if not os.path.exists('./Saved Employee Attendance Excel'):
							os.makedirs('./Saved Employee Attendance Excel')
						if len(resultss_id) !=0:
							try:
								j = str(i)
								data = pd.DataFrame(resultss_id, columns= ['Employee Name','Employee ID', 'Employee Department', 'Attendance', 'Date', 'Time'])
								datatoexcel = pd.ExcelWriter("Saved Employee Attendance Excel/Employee List "+today+"("+j+").xlsx", engine='xlsxwriter')
								data.to_excel(datatoexcel, index=False, sheet_name = "Sheet")
								worksheet = datatoexcel.sheets['Sheet']
								worksheet.set_column('A:A', 25)
								worksheet.set_column('B:B', 20)
								worksheet.set_column('C:C', 25)
								worksheet.set_column('D:D', 20)
								worksheet.set_column('E:E', 20)
								worksheet.set_column('F:F', 20)
								datatoexcel.save()
								messagebox.showinfo("Success", "Excel File is Generated Successfully Employee List "+today+"("+j+").xlsx")
							except:
								messagebox.showerror("Error", "Invalid Id Or Record Does Not Exists")
				
					if date_another_error == '':
						pass
					else:
						date_search = str(search_date.get()) 
						try:
							try:
								searched_date = datetime.strptime(date_search, '%Y-%m-%d').date()
							except UnboundLocalError as e:
								pass
						except ValueError as e:
							pass
						c.execute("SELECT * FROM absent_employee WHERE attendance_date = (?)", (searched_date,))
						results_data=c.fetchall()

						if not os.path.exists('./Saved Employee Attendance Excel'):
							os.makedirs('./Saved Employee Attendance Excel')
						if len(results_data) !=0:
							try:
								data = pd.DataFrame(results_data, columns= ['Employee Name','Employee ID', 'Employee Department', 'Attendance', 'Date', 'Time'])
								datatoexcel = pd.ExcelWriter("Saved Employee Attendance Excel/Employee List "+today+"("+str(i)+").xlsx", engine='xlsxwriter')
								data.to_excel(datatoexcel, index=False, sheet_name = "Sheet")
								worksheet = datatoexcel.sheets['Sheet']
								worksheet.set_column('A:A', 25)
								worksheet.set_column('B:B', 20)
								worksheet.set_column('C:C', 25)
								worksheet.set_column('D:D', 20)
								worksheet.set_column('E:E', 20)
								worksheet.set_column('F:F', 20)
								datatoexcel.save()
								messagebox.showinfo("Success", "Excel File is Generated Successfully Employee List "+today+"("+str(i)+").xlsx")
							except:
								messagebox.showerror("Error", "Invalid Date Or Record Does Not Exists")
			else:
				messagebox.showerror("Error", "No Data Availble In Treeview")
						

		def pdf():
			i = random.randint(0,1000)
			conn = sqlite3.connect("Registration.db")
			counter_data = len(tree_scnd.get_children())
			c = conn.cursor()
			today = str(date.today())
			id_error = search_id.get()
			date_error = search_date.get()
			date_another_error = str(date_error)
			if counter_data !=0:
				if id_error == 0 and date_error == 0:
					messagebox.showerror("Error", "Please Insert Date Or Id")
				elif id_error !=0 or date_error !=0:
					if id_error !=0:
						id_search = str(search_id.get())
						c.execute("SELECT * FROM absent_employee WHERE employee_id = (?)", (id_search,))
						resultss_id=c.fetchall()
						if not os.path.exists('./Saved Employee Attendance PDF'):
							os.makedirs('./Saved Employee Attendance PDF')
						if len(resultss_id) !=0:
							try:
								pdf = SimpleDocTemplate("./Saved Employee Attendance PDF/Employee List "+today+"("+str(i)+").pdf")
								flow_obj = []
								td = [['Employee Name','Employee ID', "Employee Department", "Employee Status", "Attendance Date", "Attendance Time"]]
								for j in resultss_id:
									td.append(j)
								table = Table(td)
								flow_obj.append(table)
								pdf.build(flow_obj)
								messagebox.showinfo("Success", "PDF generated Successfully With This Name Employee List "+today+"("+str(i)+").pdf")
							except:
								messagebox.showerror("Error", "Invalid Id Or Record Does Not Exists")
				
					if date_error =='':
						pass
					else:
						date_search = str(search_date.get()) 
						try:
							try:
								searched_date = datetime.strptime(date_search, '%Y-%m-%d').date()
							except UnboundLocalError as e:
								pass
						except ValueError as e:
							pass
						c.execute("SELECT * FROM absent_employee WHERE attendance_date = (?)", (searched_date,))
						results_data=c.fetchall()

						if not os.path.exists('./Saved Employee Attendance PDF'):
							os.makedirs('./Saved Employee Attendance PDF')
						if len(results_data) !=0:
							try:
								pdf = SimpleDocTemplate("./Saved Employee Attendance PDF/Employee List "+today+"("+str(i)+").pdf")
								flow_obj = []
								td = [['Employee Name','Employee ID', "Employee Department", "Employee Status", "Attendance Date", "Attendance Time"]]
								for j in results_data:
									td.append(j)
								table = Table(td)
								flow_obj.append(table)
								pdf.build(flow_obj)
								messagebox.showinfo("Success", "PDF generated Successfully With This Name Employee List "+today+"("+str(i)+").pdf")
							except:
								messagebox.showerror("Error", "Invalid Id Or Record Does Not Exists")
			else:
				messagebox.showerror("Error", "No Data Availble In Treeview")
						

		def search_by_id():
			for i in tree_scnd.get_children():
				tree_scnd.delete(i)
			id_error = search_id.get()

			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			id_search = str(search_id.get())
			find_data= ("SELECT * FROM absent_employee WHERE employee_id = ?")
			c.execute(find_data,[(id_search)])
			resultss=c.fetchall()
			counter_data = len(tree_scnd.get_children())

			if id_error == "":
				messagebox.showerror("Error", "Please Enter Employee ID")
			
			elif len(resultss) ==0:
				messagebox.showerror("Error", "Invalid ID or Record Does Not Exists")

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
				try:
					searched_date = datetime.strptime(date_search, '%Y-%m-%d').date()
				except ValueError as e:
					# messagebox.showerror("Error", "Incorrect Date Format")
					pass
				find_data= ("SELECT * FROM absent_employee WHERE attendance_date = ?")
				try:
					c.execute(find_data,[(searched_date)])
				except UnboundLocalError as e:
					pass
				results_data=c.fetchall()

				counter_date = len(tree_scnd.get_children())
			
			
				if len(results_data) == 0:
					messagebox.showerror("Error", "Please Enter a Valid Date or Record Does not Exists")
				if counter_date == 0:
					for r in results_data:
						tree_scnd.insert("", tk.END, values=r)


class Email(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		Label(self, text="Send Emails To Employee", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").pack(fill=X)

		photo = PhotoImage(file = '1.png')
		l = Label(self, image=photo)
		l.image=photo
		l.pack()


		btn_back = ttk.Button(self, text="Back", command= lambda: controller.show_frame(AttendanceEmployee))
		btn_back.place(x=5, y=50)

		conn = sqlite3.connect("Registration.db")
		c = conn.cursor()
		find_data= ("SELECT employee_email FROM employee")
		c.execute(find_data)
		resultss=c.fetchall()

		Label(self, text="Employee's Email Address", font=("Times New Roman", 12, 'bold'), bg="black", fg="white").place(x=50, y=80)

		email_address_var = StringVar()
		email_address = ttk.Combobox(self, width=30, textvariable=email_address_var,font=("Times New Roman", 10), state='readonly')
		email_address['values'] = resultss
		email_address.place(x=270, y=80)

		Label(self, text="Email's Content", font=("Times New Roman", 20, 'bold'), bg="black", fg="white").place(x=50, y=110)

		email_data = StringVar()
		email_content = Text(self,font=('calibri',20,'bold'),wrap="word")
		email_content.place(x=50,y=160,width=550,height=280)

		send_btn = ttk.Button(self, width=20, text="Send", command= lambda:send_email())
		send_btn.place(x=200, y=450, width=140, height=40)

		refresh_btn = ttk.Button(self, width=20, text="Refresh Email List", command= lambda:refresh_list())
		refresh_btn.place(x=350, y=450, width=140, height=40)

		Label(self, text="                                  Facial Recoginition Attendance System                               ", font=("Times New Roman", 15, 'bold'), bg="black", fg="white").place(x=0, y=515)


		def send_email():
			email_error = str(email_content.get(1.0,END))
			email_address_error = email_address_var.get()

			if len(email_address_error) == 0:
				messagebox.showerror("Error", "Please Select Email Of An Employee From List.")

			else:
				try:
					sender_email = 'pydeveloper000@gmail.com'
					sender_password = 'fypproject'
					server = smtplib.SMTP('smtp.gmail.com', 587)
					message = 'Subject: Facial Recoginition Attendance System \n{}'.format(email_error)
					server.ehlo()
					server.starttls()
					server.login(sender_email, sender_password)
					server.sendmail(sender_email,email_address_error,message)
					server.quit()
					messagebox.showinfo("Success", "Email Is Successfully Sent To The Employee.")
				except:
					messagebox.showerror("Error", "Email Didn't Sent Connection Problem Or Something Went Wrong")

		def refresh_list():
			email_list = email_address.get()
			conn = sqlite3.connect("Registration.db")
			c = conn.cursor()
			find_data= ("SELECT employee_email FROM employee")
			c.execute(find_data)
			resultss=c.fetchall()
			email_address['values'] = resultss


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
