from tkinter import Frame, Label , Entry, Button, FLAT
from PIL import Image, ImageTk

from login_package.functions import functions

class Layout(functions):
    def window(self):
        self.root.title('Login Scorpion')
        self.root.configure(background = '#8470ff')
        self.root.geometry('1080x720')
        self.root.resizable(False, False)

    def frames(self):
        self.frame = Frame(self.root, background= '#8470ff')
        self.frame.place(relx=0.05)

        self.background_png = Image.open("login_package/template/background1.png")
        self.img_background = ImageTk.PhotoImage(self.background_png)
        self.panel_background = Label(self.root, image = self.img_background, background = '#8470ff')
        self.panel_background.pack(fill='both', expand='yes')

        self.frame1 = Frame(self.root, background= '#8470ff')
        self.frame1.place(relx=0.55, rely = 0.2, relwidth = 0.35, relheight=0.50)

        self.frame2 = Frame(self.root, background= '#8470ff')
        self.frame2.place(relx =0.1, rely=0.2, relwidth= 0.45, relheight=0.50)

    def image(self):
        self.png = Image.open("login_package/template/login.png")
        self.resize_png = self.png.resize((400 ,400))
        self.img = ImageTk.PhotoImage(self.resize_png)
        self.panel = Label(self.frame1, image = self.img, background='#8470ff')
        self.panel.pack()

        self.png_login = Image.open("login_package/template/hyy.png")
        self.resize_png_login = self.png_login.resize((140,100))
        self.img_login = ImageTk.PhotoImage(self.resize_png_login)
        self.panel_login = Label(self.frame2, image = self.img_login, background = '#8470ff')
        self.panel_login.place(relx = 0.37, rely = 0.05)

        self.png_username = Image.open('login_package/template/username_icon.png')
        self.resize_username = self.png_username.resize((23,23))
        self.img_username = ImageTk.PhotoImage(self.resize_username)
        self.panel_username = Label(self.frame2, image = self.img_username, background='#8470ff')
        self.panel_username.place(relx= 0.25, rely=0.40)

        self.png_password = Image.open('login_package/template/password_icon.png')
        self.resize_password = self.png_password.resize((23,23))
        self.img_password = ImageTk.PhotoImage(self.resize_password)
        self.panel_password = Label(self.frame2, image = self.img_password, background='#8470ff')
        self.panel_password.place(relx= 0.25, rely=0.55)  


    def Labels(self):
        self.lb_login = Label(self.frame2 , text= 'Login', background='#8470ff' ,font=('yu gothic ui', 18, 'bold'))
        self.lb_login.place(relx=0.45, rely=0.32)

        self.lb_username = Label(self.frame2, text = 'Username', background = '#8470ff', foreground ='#353535',  font=('yu gothic ui', 12, 'bold'))
        self.lb_username.place(relx=0.30, rely= 0.40)

        self.lb_password = Label(self.frame2, text = 'Password', background = '#8470ff', foreground ='#353535',  font=('yu gothic ui', 12, 'bold'))
        self.lb_password.place(relx=0.30, rely= 0.55)

        self.login_png = Image.open('login_package/template/btn1.png')
        self.login_png = self.login_png.resize((250, 40))
        photo = ImageTk.PhotoImage(self.login_png)
        self.lb_login = Label(self.frame2 , text = 'Login' , image=photo, bg='#8470ff')
        self.lb_login.image = photo
        self.lb_login.place(relx=0.25, rely=0.7)

    def entrys(self):
        self.login_entry = Entry(self.frame2 , highlightthickness=0, relief=FLAT ,  fg='#353535')
        self.login_entry.place(relx=0.25, rely=0.47, relwidth=0.55)

        self.password_entry = Entry(self.frame2, show="*")
        self.password_entry.place(relx=0.25, rely=0.62, relwidth=0.55)

    def buttons(self):
        self.show_image = Image.open('login_package/template/show.png')
        self.photo = ImageTk.PhotoImage(self.show_image)

        self.btn_show = Button(self.frame2, image=self.photo, bg = 'white' , background='#8470ff', activebackground='#8470ff', cursor='hand2', bd=0, command=self.show)
        self.btn_show.image= self.photo
        self.btn_show.place(relx=0.75, rely=0.56)

        self.btn_login = Button(self.lb_login , text = 'LOGIN',font=('yu gothic ui', 12, 'bold'), cursor='hand2', width= 25 ,bd=0 ,
                                 bg='#3047ff', activebackground='#3047ff', fg='white' , command = self.login_authentication)
        self.btn_login.place(relx=0.07, rely=0.25, relwidth = 0.85, relheight= 0.5)
        
        self.btn_forgot = Button(self.frame2, text= 'Forgot Password?',background='#8470ff' ,activebackground='#8470ff' , font=('yu gothic ui', 8, 'bold underline') , bd=0, cursor='hand2')
        self.btn_forgot.place(relx= 0.5, rely=0.85)

        self.btn_create = Button(self.frame2, text= 'Sign up now!',background='#8470ff' ,activebackground='#8470ff' , font=('yu gothic ui', 8, 'bold underline') , bd=0, cursor='hand2')
        self.btn_create.place(relx= 0.35, rely=0.85)

    def show(self):
        self.hide_image = Image.open('login_package/template/hide.png')
        self.photo = ImageTk.PhotoImage(self.hide_image)
        self.btn_hide = Button(self.frame2, image=self.photo, bg = 'white' , background='#8470ff', activebackground='#8470ff', cursor='hand2', bd=0, command= self.hide)
        self.btn_hide.image= self.photo
        self.btn_hide.place(relx=0.75, rely=0.56)
        self.password_entry.configure(show='')

    def hide(self):
        self.show_image = Image.open('login_package/template/show.png')
        self.photo = ImageTk.PhotoImage(self.show_image)
        self.btn_show = Button(self.frame2, image=self.photo, bg = 'white' , background='#8470ff', activebackground='#8470ff', cursor='hand2', bd=0, command=self.show)
        self.btn_show.image= self.photo
        self.btn_show.place(relx=0.75, rely=0.56)
        self.password_entry.configure(show='*')