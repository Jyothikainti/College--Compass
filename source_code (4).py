from tkinter import Tk, Frame, Label, Button, StringVar, OptionMenu, Entry, messagebox
from PIL import Image,ImageTk
import re
import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='Srushti_2018',)
cursor = conn.cursor()
cursor.execute('create database if not exists new_schema')
cursor.execute('use new_schema')

font_type1 = ('Roman',17,'bold')
font_type2 = ('Courier New',10,'bold')
font_type3 = ('Courier New',18,'bold')
font_type4 = ('Courier New',14,'bold')
font_type5 = ('Bookman Old Style',50,'bold')

root = Tk()

class main_page:
    def __init__(self,root):
        self.root = root
        self.main_page_frame = Frame(self.root, width=900, height=600, bg='lavender')
        self.main_page_frame.place(x=0,y=0)

        self.main_page_image = Image.open('D:/college_compass/assets/collegeCompass.png')
        self.main_page_image= self.main_page_image.resize((450, 600))
        self.main_page_image= ImageTk.PhotoImage(self.main_page_image)
        self.main_page_image_label = Label(self.main_page_frame, image= self.main_page_image)
        self.main_page_image_label.image = self.main_page_image
        self.main_page_image_label.place(x=0,y=0)

        self.title = Label(self.main_page_frame, text='  College \n Compass',bg='lavender',fg='black',font=font_type5)
        self.title.place(x=490,y=200)

        self.login_button = Button(self.main_page_frame, text="Login",bg='brown',fg='beige',width='7',cursor='hand2',command=self.On_login)
        self.login_button.place(x=720, y=30)
        self.login_button = Button(self.main_page_frame, text="Signup",bg='brown',fg='beige',width='7',cursor='hand2',command=self.On_signup)
        self.login_button.place(x=790, y=30)
        
    def On_login(self):
        self.main_page_frame.destroy()
        obj_classbtn1 = Login(root)
    def On_signup(self):
        self.main_page_frame.destroy()
        obj_classbtn2 = Signup(root)

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title('Login')

        #left frame
        self.login_frame_left = Frame(self.root, width=450, height=600,bg='#F1ABB9')
        self.login_frame_left.place(x=0,y=0)


        self.left_page_image = Image.open('D:/college_compass/assets/leftship.png')
        self.left_page_image= self.left_page_image.resize((450, 600))
        self.left_page_image= ImageTk.PhotoImage(self.left_page_image)
        self.left_page_image_label = Label(self.login_frame_left, image= self.left_page_image)
        self.left_page_image_label.image = self.left_page_image
        self.left_page_image_label.place(x=0,y=0)

        self.admin_login = Label(self.login_frame_left, text='ADMIN' , bg='#D9B378',fg='black',font=font_type3)
        self.admin_login.place(x=180,y=90)

        self.admin_username_login = Label(self.login_frame_left, text='Username' , bg='#D9B378',font=font_type4)
        self.admin_username_login.place(x=70,y=190)

        self.admin_Username_text = Entry(self.login_frame_left,width='20')
        self.admin_Username_text.place(x=185,y=192)
    
        self.admin_password_login = Label(self.login_frame_left, text='Password' , bg='#D9B378',font=font_type4)
        self.admin_password_login.place(x=70,y=250)
        
        self.admin_Password_text = Entry(self.login_frame_left,width='20',show='*')
        self.admin_Password_text.place(x=185,y=252)
        
        self.admin_login_button = Button(self.login_frame_left, text="Login",bg='black',fg='#D9B378',width='10',cursor='hand2',command=self.admin_login_to_campus)
        self.admin_login_button.place(x=160, y=310)


        #right frame
        self.login_frame_right = Frame(self.root, width=450, height=600,bg='#738085')
        self.login_frame_right.place(x=449,y=0) 

        self.right_page_image = Image.open('D:/college_compass/assets/rightship.png')
        self.right_page_image= self.right_page_image.resize((450, 600))
        self.right_page_image= ImageTk.PhotoImage(self.right_page_image)
        self.right_page_image_label = Label(self.login_frame_right, image= self.right_page_image)
        self.right_page_image_label.image = self.right_page_image
        self.right_page_image_label.place(x=0,y=0)

        self.user_login = Label(self.login_frame_right, text='USER' ,fg='black', bg='#D9B378',font=font_type3)
        self.user_login.place(x=190,y=90)
    
        self.username_login = Label(self.login_frame_right, text='Username' , bg='#D9B378',font=font_type4)
        self.username_login.place(x=70,y=190)

        self.Username_text = Entry(self.login_frame_right,width='20')
        self.Username_text.place(x=185,y=192)

        self.password_login = Label(self.login_frame_right, text='Password' , bg='#D9B378',font=font_type4)
        self.password_login.place(x=70,y=250)

        self.Password_text = Entry(self.login_frame_right,width='20',show='*')
        self.Password_text.place(x=185,y=252)
    
        self.user_login_button = Button(self.login_frame_right, text="Login",bg='black',fg='beige',width='10',command=self.user_login_to_campus,cursor='hand2')
        self.user_login_button.place(x=160, y=310)

        self.login_to_main_btn = Button(self.login_frame_left,text="<-",cursor='hand2',command=self.login_to_main)
        self.login_to_main_btn.place(x=20,y=10)

    def admin_login_to_campus(self):
        self.admin_login_namec = self.admin_Username_text.get()
        self.admin_login_passwordc = self.admin_Password_text.get()
        if self.admin_login_namec.strip() == "" or self.admin_login_passwordc.strip() == "":
            messagebox.showerror('EMPTY','Please enter your login details')
            return
        cursor.execute(f"SELECT username FROM admindata WHERE username = '{self.admin_login_namec}'")
        self.admindata = cursor.fetchone()
        self.admindata2 = ''.join(self.admindata)

        cursor.execute(f"SELECT password FROM admindata WHERE username = '{self.admin_login_namec}'")
        self.admin_passdata = cursor.fetchone()
        self.admin_passdata2 = ''.join(self.admin_passdata)

        if self.admin_login_namec == self.admindata2:
            if self.admin_login_passwordc == self.admin_passdata2:
                messagebox.showinfo('WELCOME','WELCOME TO COLLEGE COMPASS')
                self.login_frame_left.destroy()
                self.login_frame_right.destroy()
                ca = admin(root)
            else:
                messagebox.showerror('WRONG PASSWORD','CHECK YOUR PASSWORD')
        else:
            messagebox.showerror('WRONG ID','INVALID USERNAME')

    def user_login_to_campus(self):

        self.user_login_name = self.Username_text.get()
        self.user_login_password = self.Password_text.get()
        if self.user_login_name.strip() == "" or self.user_login_password.strip() == "":
            messagebox.showerror('EMPTY','Please enter your login details')
            return
        cursor.execute(f"SELECT username FROM logindata WHERE username = '{self.user_login_name}'")
        self.data = cursor.fetchone()
        self.fdata = ''.join(self.data)

        cursor.execute(f"SELECT password FROM logindata WHERE username = '{self.user_login_name}'")
        self.pass_data = cursor.fetchone()
        self.fpass_data = ''.join(self.pass_data)

        if self.user_login_name == self.fdata:
            if self.user_login_password == self.fpass_data:
                messagebox.showinfo('WELCOME','WELCOME TO COLLEGE COMPASS')
                self.login_frame_left.destroy()
                self.login_frame_right.destroy()
                ca = campus(root)
            else:
                messagebox.showerror('WRONG PASSWORD','CHECK YOUR PASSWORD')
        else:
            messagebox.showerror('WRONG ID','INVALID USERNAME')

    
    def login_to_main(self):
        self.login_frame_left.destroy()
        self.login_frame_right.destroy()
        #self.root.title("College-Compass")
        Ma = main_page(root)

class Signup:
    def __init__(self,root):
        self.root = root
        self.root.title('Signup')
        self.signup_frame = Frame(self.root, width=900, height=600,bg='#F1ABB9')
        self.signup_frame.place(x=0,y=0)

        self.signup_frame_image = Image.open('D:/college_compass/assets/galaxy.png')
        self.signup_frame_image= self.signup_frame_image.resize((900, 600))
        self.signup_frame_image= ImageTk.PhotoImage(self.signup_frame_image)
        self.signup_frame_image_label = Label(self.signup_frame, image= self.signup_frame_image)
        self.signup_frame_image_label.image = self.signup_frame_image
        self.signup_frame_image_label.place(x=0,y=0)

        self.white_signup = Label(self.signup_frame, text='' , bg='lavender',width=50,height=30)
        self.white_signup.place(x=280,y=50)

        self.user_signup = Label(self.signup_frame, text='SIGN-UP' , bg='Lavender',font=font_type3)
        self.user_signup.place(x=400,y=90)

        self.username_signup = Label(self.signup_frame, text=' Enter Username' , bg='lavender',font=font_type4)
        self.username_signup.place(x=280,y=190)
   
        self.password_signup = Label(self.signup_frame, text=' Enter Password' , bg='lavender',font=font_type4)
        self.password_signup.place(x=280,y=260)

        self.Username_entry_signup = Entry(self.signup_frame,width='30')
        self.Username_entry_signup.place(x=300,y=232)

        self.Password_entry_signup = Entry(self.signup_frame,width='30',show='*')
        self.Password_entry_signup.place(x=300,y=312)

        self.mobile_signup = Label(self.signup_frame, text=' Mobile number' , bg='lavender',font=font_type4)
        self.mobile_signup.place(x=280,y=350)
        
        self.mobile_entry_signup = Entry(self.signup_frame,width='30')
        self.mobile_entry_signup.place(x=300,y=390)

        self.user_signup_button = Button(self.signup_frame, text="Signup",bg='grey',fg='white',cursor='hand2',width='10',command=self.signup_to_select)
        self.user_signup_button.place(x=410, y=470)

        self.signup_to_main_btn = Button(self.signup_frame,text="<-",cursor='hand2',command=self.signup_to_main)
        self.signup_to_main_btn.place(x=20,y=10)

    def signup_to_main(self):
        self.signup_frame.destroy()
        Ma = main_page(root)

    def signup_to_select(self):
        self.username = self.Username_entry_signup.get()
        self.mobileno = self.mobile_entry_signup.get()
        self.password = self.Password_entry_signup.get()

        cursor.execute(f"SELECT username FROM logindata WHERE username = '{self.username}'")
        self.data = cursor.fetchone()

        if len(self.username)!=0:
            if len(self.password)!=0:
                if len(self.mobileno)!=0:
                    if re.match(r'^[a-zA-Z0-9._%@#$*&^!~]', self.password):
                        if re.match(r'^[6-9]\d{9}$', self.mobileno):
                                if self.data is None:
                                    query = "INSERT INTO logindata (Username, Password, MobileNumber) VALUES (%s, %s, %s)"
                                    values = (self.username, self.password, self.mobileno)
                                    cursor.execute(query, values)

                                    conn.commit()
                                    messagebox.showinfo('SAVED','SUCCESSFULLY SIGNED UP')
                                    self.signup_frame.destroy()
                                    self.root.title("Select")
                                    camp = campus(root)
                                elif self.data is not None:
                                    messagebox.showinfo('error','username already exists')
                            
                        else:
                            messagebox.showinfo('Validation Result', 'Invalid Mobile Number!')
                else:
                    messagebox.showinfo('Missing values','Please enter Mobilenumber')
            else:
                messagebox.showinfo('Missing values','Please enter Password')
        else:
            messagebox.showinfo('Missing values','Please enter Username')

class campus:
    def __init__(self,root):
        self.root = root
        self.root.title('Select')
        self.campus_frame = Frame(self.root, width=900, height=600,bg='#5390A6')
        self.campus_frame.place(x=0,y=0)

        self.campus_page_image = Image.open('D:/college_compass/assets/Campus.png')
        self.campus_page_image= self.campus_page_image.resize((900, 600))
        self.campus_page_image= ImageTk.PhotoImage(self.campus_page_image)
        self.campus_page_image_label = Label(self.campus_frame, image= self.campus_page_image)
        self.campus_page_image_label.image = self.campus_page_image
        self.campus_page_image_label.place(x=0,y=0)

        On_Campus_options = ["On_Campus","Department","Places"]

        self.On_campus_select = StringVar(root)
        self.On_campus_select.set(On_Campus_options[0])  # Default option

        self.On_type_options = OptionMenu(self.campus_frame, self.On_campus_select, *On_Campus_options)
        self.On_type_options.config(width=40,height=2)
        self.On_type_options.place(x=290, y=170)

        self.description1 = Label(self.campus_frame, text='Staff and Locations inside the academic blocks',bg='#5390A6',fg='black',cursor = 'hand1',font=font_type4)
        self.description1.place(x=200,y=250)

        self.off_campus_btn = Button(self.campus_frame,text="Off Campus",cursor='hand2',width=40,height=2,command=self.on_off_campus)
        self.off_campus_btn.place(x=300,y=330)

        self.description1 = Label(self.campus_frame, text='Staff and Locations inside the academic blocks',bg='beige',fg='black',cursor = 'hand1',font=font_type4)
        self.description1.place(x=200,y=250)

        self.description2 = Label(self.campus_frame, text='Locations outside the academic blocks', bg='beige',fg='black',cursor='hand1',font=font_type4)
        self.description2.place(x=240,y=395)

        self.oncampus_btn = Button(self.campus_frame,text="->",cursor='hand2',bg='white',fg='black',command=self.create_new_frame)
        self.oncampus_btn.place(x=650,y=180)


        self.campus_to_main_btn = Button(self.campus_frame,text="<-",cursor='hand2',command=self.campus_to_main)
        self.campus_to_main_btn.place(x=20,y=10)

    def create_new_frame(self):
        selected = self.On_campus_select.get()
        if selected == "Department":
            self.campus_frame.destroy()
            dep = departments(root)
        elif selected == "Places":
            self.campus_frame.destroy()
            pl = places(root)
        elif selected == "On_Campus":
            messagebox.showinfo('Select','Select an option from dropdown')
    
    def on_off_campus(self):
        self.campus_frame.destroy()
        off = off_campus(root)


    def campus_to_main(self):
        self.campus_frame.destroy()
        self.root.title("College-Compass")
        Ma = main_page(root)

class departments:
    def __init__(self,root):
        self.root = root
        self.root.title('Departments')
        self.departments_frame = Frame(self.root, width=900, height=600,bg='#936B9F')
        self.departments_frame.place(x=0,y=0)

        self.departments_to_select_btn = Button(self.departments_frame,text="<-",cursor='hand2',command=self.departments_to_select)
        self.departments_to_select_btn.place(x=20,y=10)

        self.AI_image = Image.open('D:/college_compass/assets/AI.png')
        self.AI_image= self.AI_image.resize((180, 180))
        self.AI_image = ImageTk.PhotoImage(self.AI_image)
        self.AI_btn = Button(self.departments_frame,image=self.AI_image,command=self.on_ai)
        self.AI_btn.place(x=50,y=70)

        self.CIVIL_image = Image.open('D:/college_compass/assets/CIVIL.png')
        self.CIVIL_image= self.CIVIL_image.resize((180, 180))
        self.CIVIL_image = ImageTk.PhotoImage(self.CIVIL_image)
        self.CIVIL_btn = Button(self.departments_frame,image=self.CIVIL_image)
        self.CIVIL_btn.place(x=270,y=70)

        self.CSE_image = Image.open('D:/college_compass/assets/CSE.png')
        self.CSE_image= self.CSE_image.resize((180, 180))
        self.CSE_image = ImageTk.PhotoImage(self.CSE_image)
        self.CSE_btn = Button(self.departments_frame,image=self.CSE_image)
        self.CSE_btn.place(x=470,y=70)

        self.CYBER_image = Image.open('D:/college_compass/assets/CYBER.png')
        self.CYBER_image= self.CYBER_image.resize((180, 180))
        self.CYBER_image = ImageTk.PhotoImage(self.CYBER_image)
        self.CYBER_btn = Button(self.departments_frame,image=self.CYBER_image)
        self.CYBER_btn.place(x=670,y=70)

        self.ECE_image = Image.open('D:/college_compass/assets/ECE.png')
        self.ECE_image= self.ECE_image.resize((180, 180))
        self.ECE_image = ImageTk.PhotoImage(self.ECE_image)
        self.ECE_btn = Button(self.departments_frame,image=self.ECE_image)
        self.ECE_btn.place(x=50,y=370)

        self.EEE_image = Image.open('D:/college_compass/assets/EEE.png')
        self.EEE_image= self.EEE_image.resize((180, 180))
        self.EEE_image = ImageTk.PhotoImage(self.EEE_image)
        self.EEE_btn = Button(self.departments_frame,image=self.EEE_image)
        self.EEE_btn.place(x=270,y=370)

        self.IT_image = Image.open('D:/college_compass/assets/IT.png')
        self.IT_image= self.IT_image.resize((180, 180))
        self.IT_image = ImageTk.PhotoImage(self.IT_image)
        self.IT_btn = Button(self.departments_frame,image=self.IT_image)
        self.IT_btn.place(x=470,y=370)

        self.MECH_image = Image.open('D:/college_compass/assets/MECH.png')
        self.MECH_image= self.MECH_image.resize((180, 180))
        self.MECH_image = ImageTk.PhotoImage(self.MECH_image)
        self.MECH_btn = Button(self.departments_frame,image=self.MECH_image)
        self.MECH_btn.place(x=670,y=370)
    def on_ai(self):
        self.departments_frame.destroy()
        ao = AI(root)

    def on_civil(self):
        self.departments_frame.destroy()
        ao = CIVIL(root)

    def on_cse(self):
        self.departments_frame.destroy()
        ao = CSE(root)
    
    def on_cyber(self):
        self.departments_frame.destroy()
        ao = CYBER(root)
    
    def on_ece(self):
        self.departments_frame.destroy()
        ao = ECE(root)
    
    def on_eee(self):
        self.departments_frame.destroy()
        ao = EEE(root)
    
    def on_it(self):
        self.departments_frame.destroy()
        ao = IT(root)
    
    def on_mech(self):
        self.departments_frame.destroy()
        ao = MECH(root)


    def departments_to_select(self):
        self.departments_frame.destroy()
        se = campus(root)

class AI:
    def __init__(self,root):
        self.root = root
        self.root.title('AI')
        self.on_ai_frame = Frame(self.root, width=900, height=600)
        self.on_ai_frame.place(x=0,y=0)

        cell_width = 25
        cell_height = 3

        cursor.execute("SHOW COLUMNS FROM ai_table")
        column_names = [col[0] for col in cursor.fetchall()]
        for j, column_name in enumerate(column_names):
            column_label = Label(self.on_ai_frame, text=column_name, bg='pink', width=cell_width, height=cell_height)
            column_label.grid(row=0, column=j)

        cursor.execute(f"SELECT * FROM ai_table")
        self.ai_data = cursor.fetchall()
        for i, row in enumerate(self.ai_data):
            for j, value in enumerate(row):
                self.ai_data_label = Label(self.on_ai_frame, text=value,bg='pink',width=cell_width,height=cell_height)
                self.ai_data_label.grid(row=i+1,column=j)
        
        self.ai_to_select_btn = Button(self.on_ai_frame,text="<-",cursor='hand2',command=self.ai_to_select)
        self.ai_to_select_btn.place(x=20,y=10)

    def ai_to_select(self):
        self.on_ai_frame.destroy()
        camp = campus(root)

class CIVIL:
    def __init__(self,root):
        self.root = root
        self.root.title('CIVIL')
        self.on_civil_frame = Frame(self.root, width=900, height=600,bg='#936B9B')
        self.on_civil_frame.place(x=0,y=0)

class CSE:
    def __init__(self,root):
        self.root = root
        self.root.title('CSE')
        self.on_cse_frame = Frame(self.root, width=300, height=600,bg='#936B9B')
        self.on_cse_frame.place(x=0,y=0)

class CYBER:
    def __init__(self,root):
        self.root = root
        self.root.title('CYBER')
        self.on_cyber_frame = Frame(self.root, width=300, height=600,bg='#936B9B')
        self.on_cyber_frame.place(x=0,y=0)

class ECE:
    def __init__(self,root):
        self.root = root
        self.root.title('ECE')
        self.on_ece_frame = Frame(self.root, width=300, height=600,bg='#936B9B')
        self.on_ece_frame.place(x=0,y=0)

class EEE:
    def __init__(self,root):
        self.root = root
        self.root.title('EEE')
        self.on_eee_frame = Frame(self.root, width=300, height=600,bg='#936B9B')
        self.on_eee_frame.place(x=0,y=0)

class IT:
    def __init__(self,root):
        self.root = root
        self.root.title('IT')
        self.on_it_frame = Frame(self.root, width=300, height=600,bg='#936B9B')
        self.on_it_frame.place(x=0,y=0)

class MECH:
    def __init__(self,root):
        self.root = root
        self.root.title('MECH')
        self.on_mech_frame = Frame(self.root, width=300, height=600,bg='#936B9B')
        self.on_mech_frame.place(x=0,y=0)

class places:
    def __init__(self,root):
        self.root = root
        self.root.title('Departments')
        self.places_left_frame = Frame(self.root, width=300, height=600,bg='lightyellow')
        self.places_left_frame.place(x=0,y=0)

        self.places_right_frame = Frame(self.root, width=595, height=600,bg='#936B9F')
        self.places_right_frame.place(x=305,y=0)

        self.right_page_image = Image.open('D:/college_compass/assets/location.png')
        self.right_page_image= self.right_page_image.resize((595, 600))
        self.right_page_image= ImageTk.PhotoImage(self.right_page_image)
        self.right_page_image_label = Label(self.places_right_frame, image= self.right_page_image)
        self.right_page_image_label.image = self.right_page_image
        self.right_page_image_label.place(x=0,y=0)

        self.places_to_select_btn = Button(self.places_left_frame, text="<-", command=self.places_to_select)
        self.places_to_select_btn.place(x=10, y=10)

        cursor.execute(f"SELECT name FROM places")
        self.data =cursor.fetchall()

        on_campus_places_options = [r for r, in self.data]
        self.selected_place = StringVar(root)
        self.selected_place.set(on_campus_places_options[0])

        self.on_campus_places_menu = OptionMenu(self.places_left_frame, self.selected_place, *on_campus_places_options)
        self.on_campus_places_menu.config(width=27)
        self.on_campus_places_menu.place(x=23, y=100)

        self.left_frame_btn = Button(self.places_left_frame,text="->",cursor='hand2',bg='black',fg='white',command=self.display_places)
        self.left_frame_btn.place(x=250,y=180)

    def display_places(self):
        self.selected = self.selected_place.get()
        cursor.execute(f"SELECT * FROM places WHERE name = '{self.selected}'")
        self.data1 = cursor.fetchone()
        if self.data1:
            name, block, room, floor, landmarks = self.data1
            self.block_label = Label(self.places_right_frame, text=f"Name ={name}\nBlock= {block}\nRoom No = {room}\nFloor = {floor}\nLandmarks = {landmarks}",bg='paleturquoise',font=("helvetica",13,"bold"),width=40,height=9)
            self.block_label.place(x=120, y=210)
        else:
            print("No data found for ID = 1")


    
    def places_to_select(self):
        self.places_left_frame.destroy()
        self.places_right_frame.destroy()
        ca = campus(root)

class off_campus:
    def __init__(self,root):
        self.root = root
        self.root.title('Off Campus')
        self.off_campus_frame = Frame(self.root, width=900, height=600,bg='#936B9F')
        self.off_campus_frame.place(x=0,y=0)

        cell_width = 42
        cell_height = 3

        cursor.execute("SHOW COLUMNS FROM off_campus")
        column_names = [col[0] for col in cursor.fetchall()]
        for j, column_name in enumerate(column_names):
            column_label = Label(self.off_campus_frame, text=column_name, bg='pink', width=cell_width, height=cell_height)
            column_label.grid(row=0, column=j)

        cursor.execute(f"SELECT * FROM off_campus")
        self.off_campus_data = cursor.fetchall()
        for i, row in enumerate(self.off_campus_data):
            for j, value in enumerate(row):
                self.ai_data_label = Label(self.off_campus_frame, text=value,bg='peachpuff',width=cell_width,height=cell_height)
                self.ai_data_label.grid(row=i+1,column=j)
                #self.ai_data_label.place(x=50,y=50)

        self.offcampus_to_select_btn = Button(self.off_campus_frame,text="<-",cursor='hand2',command=self.offcampus_to_select)
        self.offcampus_to_select_btn.place(x=20,y=10)

    def offcampus_to_select(self):
        self.off_campus_frame.destroy()
        camp = campus(root)

class admin:
    def __init__(self,root):
        self.root = root
        self.root.title('Select')
        self.admin_frame = Frame(self.root, width=900, height=600,bg='#5390A6')
        self.admin_frame.place(x=0,y=0)

        self.admin_page_image = Image.open('D:/college_compass/assets/Campus.png')
        self.admin_page_image= self.admin_page_image.resize((900, 600))
        self.admin_page_image= ImageTk.PhotoImage(self.admin_page_image)
        self.admin_page_image_label = Label(self.admin_frame, image= self.admin_page_image)
        self.admin_page_image_label.image = self.admin_page_image
        self.admin_page_image_label.place(x=0,y=0)

        self.admin_on_Campus_options = ["On_Campus","Department","Places"]

        self.admin_on_campus_select = StringVar(root)
        self.admin_on_campus_select.set(self.admin_on_Campus_options[0])  # Default option

        self.admin_on_type_options = OptionMenu(self.admin_frame, self.admin_on_campus_select, *self.admin_on_Campus_options)
        self.admin_on_type_options.config(width=40,height=2)
        self.admin_on_type_options.place(x=290, y=170)

        self.description1 = Label(self.admin_frame, text='Staff and Locations inside the academic blocks',bg='#5390A6',fg='black',cursor = 'hand1',font=font_type4)
        self.description1.place(x=200,y=250)

        self.off_campus_btn = Button(self.admin_frame,text="Off Campus",cursor='hand2',width=40,height=2,command=self.on_admin_off_campus)
        self.off_campus_btn.place(x=300,y=330)

        self.description1 = Label(self.admin_frame, text='Staff and Locations inside the academic blocks',bg='beige',fg='black',cursor = 'hand1',font=font_type4)
        self.description1.place(x=200,y=250)

        self.description2 = Label(self.admin_frame, text='Locations outside the academic blocks', bg='beige',fg='black',cursor='hand1',font=font_type4)
        self.description2.place(x=240,y=395)

        self.oncampus_btn = Button(self.admin_frame,text="->",cursor='hand2',bg='white',fg='black',command=self.admin_create_new_frame)
        self.oncampus_btn.place(x=650,y=180)


        self.campus_to_main_btn = Button(self.admin_frame,text="<-",cursor='hand2',command=self.campus_to_main)
        self.campus_to_main_btn.place(x=20,y=10)

    def admin_create_new_frame(self):
        selected = self.admin_on_campus_select.get()
        if selected == "Department":
            self.admin_frame.destroy()
            dep = admin_departments(root)
        elif selected == "Places":
            self.admin_frame.destroy()
            pl = admin_places(root)
        elif selected == "On_Campus":
            messagebox.showinfo('Select','Select an option from dropdown')
    
    def on_admin_off_campus(self):
        self.admin_frame.destroy()
        off = admin_off_campus(root)


    def campus_to_main(self):
        self.admin_frame.destroy()
        self.root.title("College-Compass")
        Ma = main_page(root)

class admin_departments:
    def __init__(self,root):
        self.root = root
        self.root.title('Modify departments')
        self.admin_departments_frame = Frame(self.root, width=900, height=600,bg='#5390A6')
        self.admin_departments_frame.place(x=0,y=0)

        self.admin_departments_to_select_btn = Button(self.admin_departments_frame,text="<-",cursor='hand2',command=self.admin_departments_to_select)
        self.admin_departments_to_select_btn.place(x=20,y=10)

        self.admin_AI_image = Image.open('D:/college_compass/assets/AI.png')
        self.admin_AI_image= self.admin_AI_image.resize((180, 180))
        self.admin_AI_image = ImageTk.PhotoImage(self.admin_AI_image)
        self.admin_AI_btn = Button(self.admin_departments_frame,image=self.admin_AI_image,command=self.admin_on_ai)
        self.admin_AI_btn.place(x=50,y=70)

        self.admin_CIVIL_image = Image.open('D:/college_compass/assets/CIVIL.png')
        self.admin_CIVIL_image= self.admin_CIVIL_image.resize((180, 180))
        self.admin_CIVIL_image = ImageTk.PhotoImage(self.admin_CIVIL_image)
        self.admin_CIVIL_btn = Button(self.admin_departments_frame,image=self.admin_CIVIL_image)
        self.admin_CIVIL_btn.place(x=270,y=70)

        self.admin_CSE_image = Image.open('D:/college_compass/assets/CSE.png')
        self.admin_CSE_image= self.admin_CSE_image.resize((180, 180))
        self.admin_CSE_image = ImageTk.PhotoImage(self.admin_CSE_image)
        self.admin_CSE_btn = Button(self.admin_departments_frame,image=self.admin_CSE_image)
        self.admin_CSE_btn.place(x=470,y=70)

        self.admin_CYBER_image = Image.open('D:/college_compass/assets/CYBER.png')
        self.admin_CYBER_image= self.admin_CYBER_image.resize((180, 180))
        self.admin_CYBER_image = ImageTk.PhotoImage(self.admin_CYBER_image)
        self.admin_CYBER_btn = Button(self.admin_departments_frame,image=self.admin_CYBER_image)
        self.admin_CYBER_btn.place(x=670,y=70)

        self.admin_ECE_image = Image.open('D:/college_compass/assets/ECE.png')
        self.admin_ECE_image= self.admin_ECE_image.resize((180, 180))
        self.admin_ECE_image = ImageTk.PhotoImage(self.admin_ECE_image)
        self.admin_ECE_btn = Button(self.admin_departments_frame,image=self.admin_ECE_image)
        self.admin_ECE_btn.place(x=50,y=370)

        self.admin_EEE_image = Image.open('D:/college_compass/assets/EEE.png')
        self.admin_EEE_image= self.admin_EEE_image.resize((180, 180))
        self.admin_EEE_image = ImageTk.PhotoImage(self.admin_EEE_image)
        self.admin_EEE_btn = Button(self.admin_departments_frame,image=self.admin_EEE_image)
        self.admin_EEE_btn.place(x=270,y=370)

        self.admin_IT_image = Image.open('D:/college_compass/assets/IT.png')
        self.admin_IT_image= self.admin_IT_image.resize((180, 180))
        self.admin_IT_image = ImageTk.PhotoImage(self.admin_IT_image)
        self.admin_IT_btn = Button(self.admin_departments_frame,image=self.admin_IT_image)
        self.admin_IT_btn.place(x=470,y=370)

        self.admin_MECH_image = Image.open('D:/college_compass/assets/MECH.png')
        self.admin_MECH_image= self.admin_MECH_image.resize((180, 180))
        self.admin_MECH_image = ImageTk.PhotoImage(self.admin_MECH_image)
        self.admin_MECH_btn = Button(self.admin_departments_frame,image=self.admin_MECH_image)
        self.admin_MECH_btn.place(x=670,y=370)
    def admin_on_ai(self):
        self.admin_departments_frame.destroy()
        ao = admin_AI(root)
    def admin_departments_to_select(self):
        self.admin_departments_frame.destroy()
        camp = campus(root)

class admin_AI:
    def __init__(self,root):
        self.root = root
        self.root.title('AI')
        self.admin_ai_frame = Frame(self.root, width=900, height=600)
        self.admin_ai_frame.place(x=0,y=0)

        self.white_modify = Label(self.admin_ai_frame, text='' , bg='lavender',width=60,height=30)
        self.white_modify.place(x=280,y=50)

        self.user_modify = Label(self.admin_ai_frame, text='Update' , bg='Lavender',font=font_type3)
        self.user_modify.place(x=400,y=90)

        self.name_modify = Label(self.admin_ai_frame, text=' name' , bg='lavender',font=font_type4)
        self.name_modify.place(x=280,y=160)

        self.modify_name_entry = Entry(self.admin_ai_frame,width='30')
        self.modify_name_entry.place(x=400,y=160)
   
        self.position_modify = Label(self.admin_ai_frame, text=' position' , bg='lavender',font=font_type4)
        self.position_modify.place(x=280,y=230)

        self.modify_position_entry = Entry(self.admin_ai_frame,width='30')
        self.modify_position_entry.place(x=400,y=230)

        self.block_modify = Label(self.admin_ai_frame, text=' Block' , bg='lavender',font=font_type4)
        self.block_modify.place(x=280,y=290)
        
        self.modify_block_entry = Entry(self.admin_ai_frame,width='30')
        self.modify_block_entry.place(x=400,y=290)

        self.floor_modify = Label(self.admin_ai_frame, text=' Floor' , bg='lavender',font=font_type4)
        self.floor_modify.place(x=280,y=350)
        
        self.modify_floor_entry = Entry(self.admin_ai_frame,width='30')
        self.modify_floor_entry.place(x=400,y=350)

        self.room_modify = Label(self.admin_ai_frame, text=' Room' , bg='lavender',font=font_type4)
        self.room_modify.place(x=280,y=390)
        
        self.modify_room_entry = Entry(self.admin_ai_frame,width='30')
        self.modify_room_entry.place(x=400,y=390)



        self.admin_modify_button = Button(self.admin_ai_frame, text="Add",bg='grey',fg='white',cursor='hand2',width='10',command=self.ai_modify_funct)
        self.admin_modify_button.place(x=410, y=470)

        self.ai_modify_to_main_btn = Button(self.admin_ai_frame,text="<-",cursor='hand2',command=self.ai_modify_to_main)
        self.ai_modify_to_main_btn.place(x=20,y=10)

    def ai_modify_to_main(self):
        self.admin_ai_frame.destroy()
        Ma = admin_departments(root)

    def ai_modify_funct(self):

        self.name = self.modify_name_entry.get()
        self.position =  self.modify_position_entry.get()
        self.block = self.modify_block_entry.get()
        self.floor = self.modify_floor_entry.get()
        self.room = self.modify_room_entry.get()

        cursor.execute(f"SELECT name FROM ai_table WHERE name = '{self.name}'")
        self.data = cursor.fetchone()

        if len(self.name)!=0:
            if len(self.position)!=0:
                if len(self.block)!=0:
                    if len(self.floor)!=0:
                        if len(self.room)!=0:
                            if self.data is None:
                                query = "INSERT INTO ai_table (name, position, block, floor, room) VALUES (%s, %s, %s, %s, %s)"
                                values = (self.name, self.position, self.block,self.floor,self.room)
                                cursor.execute(query, values)
                                conn.commit()
                                messagebox.showinfo('SAVED','ADDED SUCCESSFULLY')
                                self.admin_ai_frame.destroy()
                                camp = admin_departments(root)
                            elif self.data is not None:
                                messagebox.showinfo('error','data already exists')
                        else:
                            messagebox.showinfo('Missing Values', 'Enter room Number!')
                    else:
                        messagebox.showinfo('Missing values','Please enter Floor')
                else:
                    messagebox.showinfo('Missing values','Please enter Block')
            else:
                messagebox.showinfo('Missing values','Please enter Position')
        else:
            messagebox.showinfo('Missing values','Please enter Name')



    

        

    def admin_ai_to_select(self):
        self.admin_ai_frame.destroy()
        camp = admin_departments(root)

class admin_places:
    def __init__(self,root):
        self.root = root
        self.root.title('Modify places')
        self.admin_places_frame = Frame(self.root, width=900, height=600,bg='#5390A6')
        self.admin_places_frame.place(x=0,y=0)

        self.white_modify = Label(self.admin_places_frame, text='' , bg='lavender',width=60,height=30)
        self.white_modify.place(x=280,y=50)

        self.admin_places_modify = Label(self.admin_places_frame, text='Update' , bg='Lavender',font=font_type3)
        self.admin_places_modify.place(x=420,y=90)

        self.places_name_modify = Label(self.admin_places_frame, text=' name' , bg='lavender',font=font_type4)
        self.places_name_modify.place(x=280,y=140)

        self.modify_places_name_entry = Entry(self.admin_places_frame,width='30')
        self.modify_places_name_entry.place(x=400,y=140)
   
        self.places_block_modify = Label(self.admin_places_frame, text=' Block' , bg='lavender',font=font_type4)
        self.places_block_modify.place(x=280,y=210)

        self.modify_places_block_entry = Entry(self.admin_places_frame,width='30')
        self.modify_places_block_entry.place(x=400,y=210)

        self.places_room_modify = Label(self.admin_places_frame, text=' Room' , bg='lavender',font=font_type4)
        self.places_room_modify.place(x=280,y=270)
        
        self.modify_places_room_entry = Entry(self.admin_places_frame,width='30')
        self.modify_places_room_entry.place(x=400,y=270)

        self.places_floor_modify = Label(self.admin_places_frame, text=' Floor' , bg='lavender',font=font_type4)
        self.places_floor_modify.place(x=280,y=320)
        
        self.modify_places_floor_entry = Entry(self.admin_places_frame,width='30')
        self.modify_places_floor_entry.place(x=400,y=320)

        self.places_landmark_modify = Label(self.admin_places_frame, text=' Landmarks' , bg='lavender',font=font_type4)
        self.places_landmark_modify.place(x=280,y=370)
        
        self.modify_places_landmarks_entry = Entry(self.admin_places_frame,width='30')
        self.modify_places_landmarks_entry.place(x=400,y=370)


        self.admin_places_modify_button = Button(self.admin_places_frame, text="Add",bg='grey',fg='white',cursor='hand2',width='10',command=self.places_modify_funct)
        self.admin_places_modify_button.place(x=440, y=470)

        self.ai_modify_to_main_btn = Button(self.admin_places_frame,text="<-",cursor='hand2',command=self.places_modify_to_main)
        self.ai_modify_to_main_btn.place(x=20,y=10)

    def places_modify_to_main(self):
        self.admin_places_frame.destroy()
        Ma = admin(root)

    def places_modify_funct(self):
        self.name = self.modify_places_name_entry.get()
        self.block =  self.modify_places_block_entry.get()
        self.floor = self.modify_places_floor_entry.get()
        self.room = self.modify_places_room_entry.get()
        self.landmarks = self.modify_places_landmarks_entry.get()

        cursor.execute(f"SELECT name FROM places WHERE name = '{self.name}'")
        self.data = cursor.fetchone()

        if len(self.name)!=0:
            if len(self.block)!=0:
                if len(self.room)!=0:
                    if len(self.floor)!=0:
                        if len(self.landmarks)!=0:
                            if self.data is None:
                                query = "INSERT INTO places (name, block, room, floor, landmarks) VALUES (%s, %s, %s, %s, %s)"
                                values = (self.name, self.block, self.room, self.floor, self.landmarks)
                                cursor.execute(query, values)
                                conn.commit()
                                messagebox.showinfo('SAVED','ADDED SUCCESSFULLY')
                                self.admin_places_frame.destroy()
                                camp = admin_departments(root)
                            elif self.data is not None:
                                messagebox.showinfo('error','data already exists')
                        else:
                            messagebox.showinfo('Missing Values', 'please enter landmarks! if none enter NONE')
                    else:
                        messagebox.showinfo('Missing values','Please enter Floor')
                else:
                    messagebox.showinfo('Missing values','Please enter Room number')
            else:
                messagebox.showinfo('Missing values','Please enter Block')
        else:
            messagebox.showinfo('Missing values','Please enter name')

class admin_off_campus:
    def __init__(self,root):
        self.root = root
        self.root.title('Modify Off Campus')
        self.admin_off_campus_frame = Frame(self.root, width=900, height=600,bg='#5390A6')
        self.admin_off_campus_frame.place(x=0,y=0)

        self.white_modify = Label(self.admin_off_campus_frame, text='' , bg='lavender',width=60,height=30)
        self.white_modify.place(x=280,y=50)

        self.admin_off_campus_modify = Label(self.admin_off_campus_frame, text='Update' , bg='Lavender',font=font_type3)
        self.admin_off_campus_modify.place(x=420,y=90)

        self.places_off_campus_name_modify = Label(self.admin_off_campus_frame, text=' name' , bg='lavender',font=font_type4)
        self.places_off_campus_name_modify.place(x=280,y=180)

        self.modify_off_campus_name_entry = Entry(self.admin_off_campus_frame,width='30')
        self.modify_off_campus_name_entry.place(x=400,y=180)
   
        self.places_off_campus_link_modify = Label(self.admin_off_campus_frame, text=' Link' , bg='lavender',font=font_type4)
        self.places_off_campus_link_modify.place(x=280,y=250)

        self.modify_off_campus_link_entry = Entry(self.admin_off_campus_frame,width='30')
        self.modify_off_campus_link_entry.place(x=400,y=250)

        self.places_off_campus_landmarks_modify = Label(self.admin_off_campus_frame, text=' Landmarks' , bg='lavender',font=font_type4)
        self.places_off_campus_landmarks_modify.place(x=280,y=320)
        
        self.modify_off_campus_landmarks_entry = Entry(self.admin_off_campus_frame,width='30')
        self.modify_off_campus_landmarks_entry.place(x=400,y=320)

        self.admin_places_modify_button = Button(self.admin_off_campus_frame, text="Add",bg='grey',fg='white',cursor='hand2',width='10',command=self.places_modify_funct)
        self.admin_places_modify_button.place(x=440, y=470)

        self.ai_modify_to_main_btn = Button(self.admin_off_campus_frame,text="<-",cursor='hand2',command=self.admin_off_campus_to_select)
        self.ai_modify_to_main_btn.place(x=20,y=10)

    def admin_off_campus_to_select(self):
        self.admin_off_campus_frame.destroy()
        Ma = admin(root)

    def places_modify_funct(self):
        self.name = self.modify_off_campus_name_entry.get()
        self.link =  self.modify_off_campus_link_entry.get()
        self.landmarks = self.modify_off_campus_landmarks_entry.get()

        cursor.execute(f"SELECT name FROM off_campus WHERE name = '{self.name}'")
        self.data = cursor.fetchone()

        if len(self.name)!=0:
            if len(self.link)!=0:
                if len(self.landmarks)!=0:
                    if self.data is None:
                        query = "INSERT INTO off_campus (name, links, landmarks) VALUES (%s, %s, %s)"
                        values = (self.name, self.link, self.landmarks)
                        cursor.execute(query, values)
                        conn.commit()
                        messagebox.showinfo('SAVED','ADDED SUCCESSFULLY')
                        self.admin_off_campus_frame.destroy()
                        camp = admin(root)
                    elif self.data is not None:
                        messagebox.showinfo('error','data already exists')
                else:
                    messagebox.showinfo('Missing Values', 'please enter landmarks! if none enter NONE')
            else:
                messagebox.showinfo('Missing values','Please paste Link')
        else:
            messagebox.showinfo('Missing values','Please enter Name')

root.title('College-Compass')
root.geometry('900x600+190+30')
root.resizable(False,False)
root.iconbitmap(r'D:\college_compass\assets\com.ico') 
main = main_page(root)
root.mainloop()