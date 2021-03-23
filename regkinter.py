from tkinter import *
from tkinter import ttk 

# Window Initialization
root = Tk()
root.geometry("450x700")
root.configure(bg = "#2b2b2b")
root.title("Registration Form")

#Window Title
title = Label(root, text = "Registration Form", fg = '#ebebeb', bg = "#2b2b2b")
title.place(x = 40, y = 53)
title.configure(font = ("Poppins", 16))

# Name Entry
name = Entry(root)
name.insert(0, "Name")
name.config(width = 30, font = ('poppins', 12), fg = "#ebebeb", bg = "#383838")
name.place(x = 40, y = 120)

#Email Entry
email = Entry(root)
email.insert(0, "email")
email.config(width = 30, font = ('poppins', 12), fg = "#ebebeb", bg = "#383838")
email.place(x = 40, y = 180)

#Gender Entry (Radio button)
gender = Label(root, text = "Gender", font = ('poppins', 12), fg = "#ebebeb", bg = "#2b2b2b")
gender.place(x = 40, y = 230)

rad1 = IntVar()
Radiobutton(root, 
			text = "Male", 
			variable = rad1, 
			value = 1, 
			background = "#383838", 
			foreground = '#ebebeb',
            selectcolor = 'gray25', 
            font = ('poppins', 10),
            width = 9).place(x = 130, y = 230)

Radiobutton(root, 
			text = "Female", 
			variable = rad1, 
			value = 2, 
			background = "#383838", 
			foreground = '#ebebeb',
            selectcolor = 'gray25', 
            font = ('poppins', 10), width=9).place(x = 242, y = 230)


#Platform Entry (Checkbuttton)
check1, check2, check3, check4, check5 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar()

platform = Label(root, text = "Platform", font = ('poppins', 12), fg = "#ebebeb", bg = "#2b2b2b")
platform.place(x = 40, y = 280)

#Python checkbox
Checkbutton(root, 
			text = "Python", 
			variable = check1, 
			background = "#383838", 
			foreground = '#ebebeb',
            selectcolor = 'gray25', 
            font = ('poppins', 10)).place(x = 130, y = 280)

#Java Checkbox
Checkbutton(root, 
			text = "Java", 
			variable = check2, 
			background = "#383838", 
			foreground = '#ebebeb',
            selectcolor = 'gray25', 
            font = ('poppins', 10)).place(x = 130, y = 320)

#Asp.net checkbox
Checkbutton(root, 
			text = "ASP.net", 
			variable = check3, 
			background = "#383838", 
			foreground = '#ebebeb',
            selectcolor = 'gray25', 
            font = ('poppins', 10)).place(x = 130, y = 360)

#android checkbox
Checkbutton(root, 
			text = "Android(Java)", 
			variable = check4, 
			background = "#383838", 
			foreground = '#ebebeb',
            selectcolor = 'gray25', 
            font = ('poppins', 10)).place(x = 130, y = 400)

#digital checkbox
Checkbutton(root, 
			text = "Digital", 
			variable = check5, 
			background = "#383838", 
			foreground = '#ebebeb',
            selectcolor = 'gray25', 
            font = ('poppins', 10)).place(x = 130, y = 440)

#university Entry (dropdown)
university = Label(root, 
					text = "University", 
					font = ('poppins',12), 
					fg = "#ebebeb", 
					bg = "#2b2b2b")
university.place(x = 40, y = 485)

n = StringVar() 
college = ttk.Combobox(root, font = ('poppins', 10), textvariable = n) 
  
# combobox drop down list 
college['values'] = (' Anna University', 
                     ' University of Madras', 
                     ' Pondicherry University',
                     ' Alagappa University', 
                     ' Central University of Tamil Nadu', 
                     ' Indian Institute of Technology Madras', 
                     ' Thiruvalluvar University', 
                     ' VIT University') 
  
college.grid(column = 1, row = 1) 
college.place(x = 130, y = 490) 

Button(root, text = 'Submit',
                      fg = '#ebebeb',
                      bg = '#0b2b4f',
                      font =('poppins',10),
                      bd =  10, 
                      width = 35,
                      highlightthickness = 4, 
                      highlightcolor = "#ebebeb", 
                      highlightbackground = "#ebebeb", 
                      borderwidth = 3).place(x = 40, y = 540)
root.mainloop()
