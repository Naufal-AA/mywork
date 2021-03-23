from tkinter import *
from tkinter import messagebox
import os
import random

# assign each one have value using dictionary
game = {
	"0" : "rock",
	"1" : "paper",
	"2" : "scissor"
}

# for counting user and system point, initialize the both variable
count_pc = 0
count_you = 0

# for performing rock condition
def rock():
	global count_pc
	global count_you
	
	# take random one using random class and take the value of condition from dictonary
	pc = game[str(random.randint(0,2))]

	you_label.config(text = "You")
	system_label.config(text = "System")
	vs.config(text = "V/S")
	
	if pc == "rock":
		your_move.config(text = "")
		system_move.config(text = "")
		trophy.config(text = "")
		congrats.config(text = "")
		draw.config(text = "Match Draw")
		won.config(text = "")
		you.config(text = count_you)
		system.config(text = count_pc)

	elif pc == "scissor":
		your_move.config(text = "")
		system_move.config(text = "")
		trophy.config(text = "")
		draw.config(text = "")
		congrats.config(text = "Congratulations!")
		won.configure(text = "You Win!")
		count_you += 1
		you.config(text = count_you)
		system.config(text = count_pc)
	
	else:
		your_move.config(text = "")
		system_move.config(text = "")
		trophy.config(text = "")
		draw.config(text = "")
		congrats.config(text = "Congratulations!")
		won.configure(text = "Computer Win!")
		count_pc += 1
		you.config(text = count_you)
		system.config(text = count_pc)

# for performing paper condition
def paper():
	global count_pc
	global count_you

	pc = game[str(random.randint(0,2))]

	you_label.config(text = "You")
	system_label.config(text = "System")
	vs.config(text = "V/S")
	
	if pc == "paper":
		your_move.config(text = "")
		system_move.config(text = "")
		trophy.config(text = "")
		congrats.config(text = "")
		draw.config(text = "Match Draw")
		won.config(text = "")
		you.config(text = count_you)
		system.config(text = count_pc)

	elif pc == "scissor":
		your_move.config(text = "")
		system_move.config(text = "")
		trophy.config(text = "")
		draw.config(text = "")
		congrats.config(text = "Congratulations!")
		won.configure(text = "Computer Win!")
		count_pc += 1
		you.config(text = count_you)
		system.config(text = count_pc)
	
	else:
		your_move.config(text = "")
		system_move.config(text = "")
		trophy.config(text = "")
		draw.config(text = "")
		congrats.config(text = "Congratulations!")
		won.configure(text = "You Win!")
		count_you += 1
		you.config(text = count_you)
		system.config(text = count_pc)

# for performing scissor condition
def scissor():
	global count_pc
	global count_you
	pc = game[str(random.randint(0,2))]

	you_label.config(text = "You")
	system_label.config(text = "System")
	vs.config(text = "V/S")
	
	if pc == "scissor":
		your_move.config(text = "")
		system_move.config(text = "")
		trophy.config(text = "")
		congrats.config(text = "")
		draw.config(text = "Match Draw")
		won.config(text = "")
		you.config(text = count_you)
		system.config(text = count_pc)

	elif pc == "rock":
		your_move.config(text = "")
		system_move.config(text = "")
		trophy.config(text = "")
		draw.config(text = "")
		congrats.config(text = "Congratulations!")
		won.configure(text = "Computer Win!")
		count_pc += 1
		you.config(text = count_you)
		system.config(text = count_pc)
	
	else:
		your_move.config(text = "")
		system_move.config(text = "")
		trophy.config(text = "")
		draw.config(text = "")
		congrats.config(text = "Congratulations!")
		won.configure(text = "You Win!")
		count_you += 1
		you.config(text = count_you)
		system.config(text = count_pc)

# for reseting game
def reset():
	global count_pc
	global count_you

	count_pc = 0
	count_you = 0
	
	you_label.config(text = "")
	system_label.config(text = "")
	vs.config(text = "")
	your_move.config(text = "")
	system_move.config(text = "")
	trophy.config(text = "")
	draw.config(text = "")
	congrats.config(text = "")
	won.configure(text = "")
	you.config(text = count_you)
	system.config(text = count_pc)


# main screen
main_screen = Tk()   
main_screen.title("Rock Paper Scissor")   
main_screen.geometry("1280x800")
main_screen.configure(bg = "#283137")   

# Title
Label(main_screen, text = "ROCK PAPER SCISSOR", bg = "#283137", fg = "#e8e9ea", width=90, height=2,  font = ("Montserrat Medium", 14), anchor=E).pack()

#your score Board
Label(main_screen, text="YOU:", bg = "#283137", fg= "#599dc7", font = ("poppins", 12)).place(x = 1025, y = 40)
you = Label(main_screen, text="0", bg = "#283137", fg= "#e8e9ea", font = ("poppins", 12))
you.place(x = 1075, y = 40)

#System score board
Label(main_screen, text="SYSTEM:", bg = "#283137", fg= "#599dc7", font = ("poppins", 12), anchor=E).place(x = 1125, y = 40)
system = Label(main_screen, text="0", bg = "#283137", fg= "#e8e9ea", font = ("poppins", 12), anchor=E)
system.place(x = 1200, y = 40)

#play again 
Button(main_screen, text = "", bg = "#283137", fg = "#e8e9ea", activebackground = "#283137", activeforeground = "#104670", 
		font = ("Font Awesome 5 Free Regular", 14), cursor="circle #b3401d", relief = "flat", command = reset).place(x = 1230, y = 35)

#choose options
Button(main_screen, text = "", bg = "#283137", fg = "#e8e9ea", activebackground = "#283137", activeforeground = "#104670", 
		font = ("Font Awesome 5 Free Regular", 100), cursor="circle #b3401d", relief = "flat", command = rock).place(x = 250, y = 180)
Button(main_screen, text = "", bg = "#283137", fg = "#e8e9ea", activebackground = "#283137", activeforeground = "#104670", 
		font = ("Font Awesome 5 Free Regular", 100), cursor="circle #b3401d", relief = "flat", command = paper).place(x = 525, y = 180)
Button(main_screen, text = "", bg = "#283137", fg = "#e8e9ea", activebackground = "#283137", activeforeground = "#104670", 
		font = ("Font Awesome 5 Free Regular", 100), cursor="circle #b3401d", relief = "flat", command = scissor).place(x = 800, y = 180)

Label(main_screen, text = "Choose your weapon", width = 30, bg = "#104670", fg= "#e8e9ea", font = ("poppins", 16)).place(x = 460, y = 430)

#result showing 
you_label = Label(main_screen, text = "", width = 10, bg = "#283137", fg= "#e8e9ea", font = ("poppins", 14))
you_label.place(x = 505, y = 515)
system_label =Label(main_screen, text = "", width = 10, bg = "#283137", fg= "#e8e9ea", font = ("poppins", 14))
system_label.place(x = 700, y = 515)

#choosen by you
your_move = Label(main_screen, text = "", width = 10, bg = "#283137", fg= "#e8e9ea", font = ("Font Awesome 5 Free Regular", 18))
your_move.place(x = 490, y = 550)

vs = Label(main_screen, text = "", width =10, bg = "#283137", fg= "#e8e9ea", font = ("poppins", 16))
vs.place(x = 590, y = 550)

#choosen by System
system_move = Label(main_screen, text = "", width = 10, bg = "#283137", fg= "#e8e9ea", font = ("Font Awesome 5 Free Regular", 18))
system_move.place(x = 680, y = 550)

trophy = Label(main_screen, text = "", width = 10, bg = "#283137", fg= "#e8e9ea", font = ("Font Awesome 5 Free Solid", 48))
trophy.place(x = 470, y = 620)
congrats = Label(main_screen, text = "", bg = "#283137", fg= "#e8e9ea", font = ("Pacifico", 16))
congrats.place(x = 540, y = 700) 

#show winner
won = Label(main_screen, text = "", bg = "#283137", fg= "#e8e9ea", font = ("Pacifico", 16))
won.place(x = 700, y = 700)

#match draw
draw = Label(main_screen, text = "", bg = "#283137", fg= "#e8e9ea", font = ("Pacifico", 22))
draw.place(x = 580, y = 620)


main_screen.mainloop() 