#_________________________________________________________________________________________________________________
#-------------------------------------------Importing Required Package(API)---------------------------------------
#-----------------------------------------------------------------------------------------------------------------
from tkinter import Label, Button
from PIL import ImageTk
from tkinter import messagebox, Frame, Entry, END, Tk
import pymysql

#_________________________________________________________________________________________________________________
#-----------------------------------------------------FRONT END CODE----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
class Admin_login_class:


   #=====Function===========
    def __init__(self,Admin_login_Window):
        self.Admin_login_Window=Admin_login_Window
        self.Admin_login_Window.title("ConsoleLancer")
        self.Admin_login_Window.geometry("1350x740")
        #________________________________________________________________
        #-------------------------Frame And Background-------------------
        #----------------------------------------------------------------
        #===main-Background===
        self.bg=ImageTk.PhotoImage(file="bg.png")
        bg=Label(self.Admin_login_Window,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #===Sub-Background=====
        self.left=ImageTk.PhotoImage(file="Sub_bg.png")
        left=Label(self.Admin_login_Window,image=self.left).place(x=80,y=100,width=400,height=500)

        #===Register freame=====
        frame1=Frame(self.Admin_login_Window,bg="white")
        frame1.place(x=480,y=100,width=800,height=500)

        #===Form Heading=======
        title=Label(frame1,text="ADMIN SIGN IN", font=("time new roman",20,"bold"),bg="white",fg="#838786")
        title.place(x=270,y=100)

        #________________________________________________________________
        #---------------Entry feilds and Headings -----------------------
        #----------------------------------------------------------------

        # =======E-mail or Number Text And Field===========
        email = Label(frame1, text="E-Mail Or Number", font=("time new roman", 15, "bold"), bg="white", fg="gray")
        email.place(x=150, y=180)
        self.email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.email.place(x=400, y=180, width=250)

        # ==========Password Text And Field=========
        passw = Label(frame1, text="Password", font=("time new roman", 15, "bold"), bg="white", fg="gray")
        passw.place(x=150, y=230)
        self.passw = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.passw.place(x=400, y=230, width=250)

        #_________________________________________________________________
        #-----------------------Buttons-----------------------------------
        #-----------------------------------------------------------------

        # =====Regester or Signin button======


        # =======Singin Button======
        self.signin_btn = ImageTk.PhotoImage(file="Sign_In.png")
        sigin = Button(frame1,image=self.signin_btn,activebackground="#ffffff",command=self.log_in,bd=0,bg="#ffffff",cursor="hand2")
        sigin.place(x=265, y=300)
        # =======Signup Button======
        self.signup_btn = ImageTk.PhotoImage(file="Sign_Up.png")
        sigup = Button(self.Admin_login_Window,image=self.signup_btn,activebackground="#013c74",command=self.sign_up,bg="#013a71",cursor="hand2",bd=0)
        #sigup.place(x=160,y=500)

        #=======Read More Button======
        self.read_more = ImageTk.PhotoImage(file="Read_More.png")
        read_more = Button(self.Admin_login_Window, text="Read More",activebackground="#013c74", image=self.read_more, command=self.read_More_page, bg="#013c74",
                           bd=0, cursor="hand2")
        read_more.place(x=220, y=455)

#___________________________________________________________________________________________________________________
#-----------------------------------------------BACK END CODE-------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------


    #========Function for going to sign in page=============
    def log_in(self):
        if self.email.get()=="" or self.passw.get()=="":
            messagebox.showerror("Error","Please Enter User Name And Password",parent=self.Admin_login_Window)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="aug")
                cur=con.cursor()
                cur.execute("select * from adminTab where admin=%s and password=%s",(self.email.get(),self.passw.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid User Name and Password",parent=self.Admin_login_Window)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.Admin_login_Window)
                    self.Admin_login_Window.destroy()
                    import Admin_DashBoard
                    con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.Admin_login_Window)

    # =======Function for Going to Sign up page========================
    def sign_up(self):
        self.Admin_login_Window.destroy()

   #====Function to delete current page and jump on Read More Page=====
    def read_More_page(self):
        self.Admin_login_Window.destroy()

   # ==========function to clear the fields after success===============
    def clear(self):
        self.email.delete(0, END)
        self.passw.delete(0, END)


Admin_login_Window=Tk()
Admin_login_Object=Admin_login_class(Admin_login_Window)
Admin_login_Window.resizable(False, False)
Admin_login_Window.mainloop()

