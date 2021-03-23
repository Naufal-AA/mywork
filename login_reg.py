from tkinter import *
import os
from tkinter import messagebox

def register():
	global register_screen
	global username
	global password
	global username_entry
	global password_entry

	register_screen = Toplevel(main_screen)
	register_screen.title("Register")
	register_screen.geometry("400x600")
	register_screen.configure(bg = "#ebebeb")  

	username = StringVar()
	password = StringVar()

	Label(register_screen, text = "REGISTER",  bg = "#383838", fg = "#ddd", width=100, height=2,  font = ("segoe ui", 14)).pack()
	Label(register_screen, text = "", bg= "#ebebeb").pack(pady = 20)
	Label(register_screen, text = "", bg= "#ebebeb").pack()

	username_label = Label(register_screen, text = "Username *", bg = "#ebebeb", width = 40, font = ("segoe ui", 12), anchor = W)
	username_label.pack(fill=X, padx=100, pady=5)

	username_entry = Entry(register_screen, textvariable = username, bg= "#ebebeb", width= 20, font = ("segoe ui", 14), relief = "solid")
	username_entry.pack(pady = 10)

	password_label = Label(register_screen, text = "Password *", bg = "#ebebeb", width = 40, font = ("segoe ui", 12), anchor = W)
	password_label.pack(fill=X, padx=100, pady=5)

	password_entry = Entry(register_screen, textvariable = password, show = "*", bg= "#ebebeb", width= 20, font = ("segoe ui", 14), relief = "solid")
	password_entry.pack()

	Label(register_screen, text = "", bg= "#ebebeb").pack()
	Button(register_screen, text = "register", width = 22, height = 1, font = ("segoe ui", 12), relief = "solid", command = register_user).pack()
	


def login():
	global login_screen
	global username_verify
	global password_verify
	global username_login_entry
	global password_login_entry

	login_screen = Toplevel(main_screen)
	login_screen.geometry("400x600")
	login_screen.title("Login")
	login_screen.configure(bg = "#ebebeb")

	username_verify = StringVar()
	password_verify = StringVar()

	Label(login_screen, text = "SIGN IN",  bg = "#383838", fg = "#ddd", width=100, height=2,  font = ("segoe ui", 14)).pack(pady = 20)
	Label(login_screen, text = "", bg= "#ebebeb").pack(pady=10)
	Label(login_screen, text = "Please enter the details", bg= "#ebebeb", width = 40, font = ("segoe ui", 8), anchor = W).pack(fill=X, padx=100)
	
	Label(login_screen, text = "Username *", bg = "#ebebeb", width = 40, font = ("segoe ui", 12), anchor = W).pack(fill=X, padx=100, pady=5)
	username_login_entry = Entry(login_screen, textvariable = username_verify, bg= "#ebebeb", width= 20, font = ("segoe ui", 14), relief = "solid")
	username_login_entry.pack()
	Label(login_screen, text = "", bg = "#ebebeb").pack()

	Label(login_screen, text = "Password *", bg = "#ebebeb", width = 40, font = ("segoe ui", 12), anchor = W).pack(fill=X, padx=100)
	password_login_entry = Entry(login_screen, textvariable = password_verify, show = "*",  bg= "#ebebeb", width= 20, font = ("segoe ui", 14), relief = "solid")
	password_login_entry.pack()

	Label(login_screen, text = "", bg = "#ebebeb").pack()
	Button(login_screen, text = "Login", width = 22, height = 1, font = ("segoe ui", 12), relief = "solid", command = login_verify).pack()


def register_user():
	username_info = username.get()
	password_info = password.get()

	file = open("register1", "w+")
	file.write(username_info + "\n")
	file.write(password_info)
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)
	Label(register_screen, text = "Register Success", fg = "green", font = ("callibri", 11)).pack()

	if len(username_info) == 0 or len(password_info) == 0:
		messagebox.showerror("Error", "Please fill the credentials")
	else:
		messagebox.showinfo("Register Success", "Successfully Registered")


def login_verify():
	username_info = username_verify.get()
	password_info = password_verify.get()

	file = open("register1", "r")
	read_user = file.read()
	list_user = read_user.split("\n")
	file.close()

	username_login_entry.delete(0, END)
	password_login_entry.delete(0, END)

	if len(username_info) == 0 or len(password_info) == 0:
		messagebox.showerror("Error", "Invalid Credential")
	else:
		if username_info == list_user[0] and password_info == list_user[1]:
			messagebox.showinfo("Success", "Successfully Logged in")
		else:
			messagebox.showerror("Error", "Invalid Credential")


# main screen
main_screen = Tk()   
main_screen.title("Account Login")   
main_screen.geometry("400x600")
main_screen.configure(bg = "#ebebeb")   

Label(main_screen, text = "SIGN IN", bg = "#383838", fg = "#ddd", width=100, height=2,  font = ("segoe ui", 14)).pack()
Label(main_screen, text="").pack()

Label(main_screen, text = "", bg= "#ebebeb", fg="#383838",  font = ("Font Awesome 5 Free Regular", 72)).pack(pady=20)
Button(main_screen, text = "Register", width = 20, height = 2, font = ("segoe ui", 12), relief = "solid",  command = register).pack(padx = 10) 
Button(main_screen, text = "Login", width = 20, height = 2, font = ("segoe ui", 12), relief = "solid", command = login).pack(padx = 20, pady = 20) 
 
main_screen.mainloop() 
