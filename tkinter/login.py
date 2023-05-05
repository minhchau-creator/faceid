import ast
from tkinter import * 
#from database import *
from tkinter import messagebox





Login = Tk() # tạo frame login
Login.title("Login")
Login.geometry("925x500+300+200") #Hai tham số đầu tiên là kích thước cửa sổ, hai phương thức sau là vị trí của cửa sổ trên màn hình.
Login.configure(bg = "#fff")
Login.resizable(False,False)



#trang trí cho xinh xẻo ><
img = PhotoImage(file = "anh.png")
Label(Login,image=img, bg= "white").place(x=50,y=50)  

#
frame = Frame(Login,width=350,height=350,bg="white")
frame.place(x=480,y=70)



# sau khi ấn button
def btnLogin_click():
    user = tbUser.get()
    pwd = tbPass.get()
    if ( user == "admin" ):
        if ( pwd == "123"):
            messagebox.showinfo("THÔNG BÁO", "Đăng nhập thành công")
        elif ( pwd == "") : 
            messagebox.showerror("THÔNG BÁO", "Sai thông tin đăng nhập")
        else :
            messagebox.showerror("THÔNG BÁO", "Sai thông tin đăng nhập")
    elif ( user == ""):
        messagebox.showerror("THÔNG BÁO", "Sai thông tin đăng nhập")
    else :
        messagebox.showerror("THÔNG BÁO", "Sai thông tin đăng nhập")

def sign_up_click():
    SignUp = Toplevel(Login) # tạo frame sign up 
    SignUp.title("Sign Up")
    SignUp.geometry("925x500+300+200") #Hai tham số đầu tiên là kích thước cửa sổ, hai phương thức sau là vị trí của cửa sổ trên màn hình.
    SignUp.configure(bg = "#fff")
    SignUp.resizable(False,False)

    ######################################################################
    img2 = PhotoImage(file = "anh.png")
    Label(SignUp,image= img2, bg= "white").place(x=50,y=50)  

    frame = Frame(SignUp,width=350,height=350,bg="white")
    frame.place(x=480,y=70)
    #######################################################################

    heading2 = Label(SignUp, text = "Thank you for sign up! \n Please fill in your information ", font = ("Microsoft YaHei UI Light", 11), fg = "#57a1f8", bg ="white")
    heading2.place( x = 550, y = 140 )

    #########################################################################################

    def on_enter(e):
        newUser.delete(0,'end')
    def on_leave(e):
        name = newUser.get()
        if name == '':
            newUser.insert(0, 'Username')
    newUser = Entry(SignUp, width = 40, fg="black",border=2,bg="white",font = ("Microsoft YaHei UI Light", 11))
    newUser.place( x=500,y=190 )
    newUser.insert(0,"Username")
    newUser.bind('<FocusIn>', on_enter)
    newUser.bind('<FocusOut>', on_leave)

    def on_enter(e):
        new_id.delete(0,'end')
    def on_leave(e):
        name = new_id.get()
        if name == '':
            new_id.insert(0, 'ID number')
    new_id = Entry(SignUp, width = 40, fg="black",border=2,bg="white",font = ("Microsoft YaHei UI Light", 11))
    new_id.place(x=500,y=220)
    new_id.insert(0,"ID number")
    new_id.bind('<FocusIn>', on_enter)
    new_id.bind('<FocusOut>', on_leave)

    def on_enter(e):
        newPass.delete(0,'end')
    def on_leave(e):
        name = newPass.get()
        if name == '':
            newPass.insert(0, 'Password')
    newPass = Entry(SignUp, width = 40, fg="black",border=2,bg="white",font = ("Microsoft YaHei UI Light", 11))
    newPass.place( x=500,y=250 )
    newPass.insert(0,"Password")
    newPass.bind('<FocusIn>', on_enter)
    newPass.bind('<FocusOut>', on_leave)

    def on_enter(e):
        confirm_pass.delete(0,'end')
    def on_leave(e):
        name = confirm_pass.get()
        if name == '':
            confirm_pass.insert(0, 'Confirm Password')
    confirm_pass = Entry(SignUp, width = 40, fg="black",border=2,bg="white",font = ("Microsoft YaHei UI Light", 11))
    confirm_pass.place( x=500,y=280 )
    confirm_pass.insert(0,"Confirm Password")
    confirm_pass.bind('<FocusIn>', on_enter)
    confirm_pass.bind('<FocusOut>', on_leave)

    ################################### button Sign up #########################################3
    def btnSignUp_click():
        new_user = newUser.get()
        new_pwd = newPass.get()
        new_ID = new_id.get()
        confirm_pwd = confirm_pass.get()

        if new_user == " ":
            messagebox.showwarning("please fill in your name")
        if new_pwd == " ":
            messagebox.showwarning("Please fill in your password")
        if new_ID == " ":
            messagebox.showwarning("please fill in your ID")
        if new_pwd == confirm_pwd:
            try:
                file=open('dataset.txt', 'r+', encoding = 'utf8')
                d = file.read()
                r = ast.literal_eval(d)

                dict2={new_user : new_pwd}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('dataset.txt', 'w', encoding = 'utf8')
                w = file.write(str(r))

                messagebox.showinfo('SignUp', 'Sign up successful!')
            
            except : 
                file = open('dataset.txt', 'w')
                pp = str({new_user : new_pwd})
                file.write(pp)
                file.close()

        else : 
            messagebox.showerror('Invalid', "Both Password should match")

    

    
    btnSignUp = Button(SignUp, width = 46, pady= 7, text = "Sign up", bg="#57a1f8", fg = "white", border = 0, command = btnSignUp_click ).place (x=500,y=330)


heading = Label(Login, text = "Sign in", fg = "#57a1f8", font = ("Microsoft YaHei UI Light", 23, 'bold'), bg = "white")
heading.place(x=600,y=100)

######################################## Nhập Username  #################################################################
def on_enter(e):
    tbUser.delete(0,'end')
def on_leave(e):
    name = tbUser.get()
    if name == '':
        tbUser.insert(0, 'Username')

tbUser = Entry(Login, width = 40, fg="black",border=2,bg="white",font = ("Microsoft YaHei UI Light", 11))
tbUser.place(x=500,y=170)
tbUser.insert(0,"Username")
tbUser.bind('<FocusIn>', on_enter)
tbUser.bind('<FocusOut>', on_leave)
######################################## Nhập password  ############################################################################
def on_enter(e):
    tbPass.delete(0,'end')

def on_leave(e):
    name = tbPass.get()
    if name == '':
        tbPass.insert(0,'Password')

tbPass = Entry(Login, width = 40, fg="black",border=2,bg="white",font = ("Microsoft YaHei UI Light", 11))
tbPass.place(x=500,y=210)
tbPass.insert(0,"Password")

tbPass.bind('<FocusIn>', on_enter)
tbPass.bind('<FocusOut>', on_leave)


############################# LOGIN BUTTON ###################################

btnLogin = Button(Login, width = 46, pady= 7, text = "Sign in", bg="#57a1f8", fg = "white", border = 0, command = btnLogin_click ).place (x=500,y=250)



############################ nếu chưa có tài khoản #####################################################################################################
label = Label( Login, text = "Don't have an account ?", fg='#57a1f8', bg = "white", font = ("Microsoft YaHei UI Light", 9) )
label.place(x=550, y= 290)

sign_up = Button(Login, width = 6, text = "Sign up", border = 0, bg ="white", cursor = 'hand2', fg = "#57a1f8", font = ("Microsoft YaHei UI Light", 9), command = sign_up_click)
sign_up.place(x = 695, y = 290)


Login.mainloop()