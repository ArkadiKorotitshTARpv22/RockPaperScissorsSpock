from operator import truediv
from tkinter import *
import random
import tkinter
import emoji
user = int
computer = int
win = 0
lose = 0
canvas = 1
def rps(win, lose, user):
    computer = random.randrange(1,6)
    if user == computer:
        var.set(emoji.emojize("==:chains:== \n:cross_mark::minus::cross_mark:"))  
    elif user == 1 and computer == 3:
        var.set(emoji.emojize(":gem_stone:.:right_arrow:.:scissors:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 2:
        var.set(emoji.emojize(":gem_stone:.:left_arrow:.:roll_of_paper:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
          
    elif user == 2 and computer == 1:
        var.set(emoji.emojize(":roll_of_paper:.:right_arrow:.:gem_stone:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
          
    elif user == 2 and computer == 3:
        var.set(emoji.emojize(":roll_of_paper:.:left_arrow:.:scissors:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
        
    elif user == 3 and computer == 1:
        var.set(emoji.emojize(":scissors:.:left_arrow:.:gem_stone:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
         
    elif user == 3 and computer == 2:
        var.set(emoji.emojize(":scissors:.:right_arrow:.:roll_of_paper:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 3:
        var.set(emoji.emojize(":person_standing:.:right_arrow:.:scissors:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 1:
        var.set(emoji.emojize(":person_standing:.:right_arrow:.:gem_stone:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 5:
        var.set(emoji.emojize(":person_standing:.:left_arrow:.:lizard:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
        
    elif user == 4 and computer == 2:
        var.set(emoji.emojize(":person_standing:.:left_arrow:.:roll_of_paper:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
        
    elif user == 5 and computer == 1:
        var.set(emoji.emojize(":lizard:.:left_arrow:.:gem_stone:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
        
    elif user == 5 and computer == 2:
        var.set(emoji.emojize(":lizard:.:right_arrow:.:roll_of_paper:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 5 and computer == 3:
        var.set(emoji.emojize(":lizard:.:left_arrow:.:scissors:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
        
    elif user == 5 and computer == 4:
        var.set(emoji.emojize(":lizard:.:right_arrow:.:person_standing:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 4:
        var.set(emoji.emojize(":gem_stone:.:left_arrow:.:person_standing:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
        
    elif user == 2 and computer == 4:
        var.set(emoji.emojize(":roll_of_paper:.:right_arrow:.:person_standing:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 3 and computer == 4:
        var.set(emoji.emojize(":scissors:.:left_arrow:.:person_standing:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
        
    elif user == 5 and computer == 4:
        var.set(emoji.emojize(":lizard:.:right_arrow:.:person_standing:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 5:
        var.set(emoji.emojize(":gem_stone:.:right_arrow:.:lizard:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 2 and computer == 5:
        var.set(emoji.emojize(":roll_of_paper:.:left_arrow:.:lizard:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
        
    elif user == 3 and computer == 5:
        var.set(emoji.emojize(":scissors:.:right_arrow:.:lizard:\n:check_mark::minus::cross_mark:"))
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 5:
        var.set(emoji.emojize(":person_standing:.:left_arrow:.:lizard:\n:cross_mark::minus::check_mark:"))
        loses.set(loses.get() + 1)
        


    
top = tkinter.Tk()


top.wm_title("RPSLS")
top.minsize(width=600, height=300)
top.maxsize(width=600, height=300)
def change_color():
        top.configure(bg="white")
        B1.configure(bg="white",fg="grey20")
        B2.configure(bg="white",fg="grey20")
        B3.configure(bg="white",fg="grey20")
        B4.configure(bg="white",fg="grey20")
        B5.configure(bg="white",fg="grey20")
        l.configure(bg="white",fg="grey20")
        w.configure(bg="white",fg="grey20")
        w2.configure(bg="white",fg="grey20")
        labeled.configure(bg="white",fg="grey20")
        labeled2.configure(bg="white",fg="grey20")
        button2.configure(bg="white",fg="grey20")
        button3.configure(bg="white",fg="grey20")
def change_color2():
        top.configure(bg="grey14")
        B1.configure(bg="grey20",fg="white")
        B2.configure(bg="grey20",fg="white")
        B3.configure(bg="grey20",fg="white")
        B4.configure(bg="grey20",fg="white")
        B5.configure(bg="grey20",fg="white")
        l.configure(bg="grey14",fg="white")
        w.configure(bg="grey14",fg="white")
        w2.configure(bg="grey14",fg="white")
        labeled.configure(bg="grey14",fg="white")
        labeled2.configure(bg="grey14",fg="white")
        button2.configure(bg="grey20",fg="white")
        button3.configure(bg="grey20",fg="white")

def changelaunguageEST():
    B1.configure(text="Kivi")
    B2.configure(text="Paber")
    B3.configure(text="Käärid")
    B4.configure(text="Inimene")
    B5.configure(text="Sisalik")
    Brestart.configure(text="Taaskäivitage")
    labeled.configure(text="Mängija skoor:")
    labeled2.configure(text="Roboti skoor:")
    var.set("Keel muudetud\n Eesti keeleks")
    button.configure(text="Kerge")
    button1.configure(text="Tume")

def changelaunguageENG():
    B1.configure(text="Rock")
    B2.configure(text="Paper")
    B3.configure(text="Scissors")
    B4.configure(text="Person")
    B5.configure(text="Lizard")
    Brestart.configure(text="Restart")
    labeled.configure(text="Player Score:")
    labeled2.configure(text="Robot Score:")
    var.set("Language changed\n to English")
    button.configure(text="Light")
    button1.configure(text="Dark")

button=Button(bg="white",fg="grey20",text= "Light", font=('Helvetica 10 bold'), command=change_color)
button.grid(row=0,column=0)
button1=Button(bg="grey20",fg="white",text= "Dark", font=('Helvetica 10 bold'), command=change_color2)
button1.grid(row=0,column=4)
button2=Button(bg="white",fg="grey20",text= "Eesti", font=('Helvetica 10 bold'), command=changelaunguageEST)
button2.grid(row=6,column=0)
button3=Button(bg="white",fg="grey20",text= "English", font=('Helvetica 10 bold'), command=changelaunguageENG)
button3.grid(row=6,column=1)
def restartbtn():
    wins.set(wins.get() ==-1)
    loses.set(wins.get() ==-1)
    var.set(emoji.emojize("🔁.🔁.🔁"))
B1 = tkinter.Button(top, text ="Rock", command = lambda: rps(win, lose, 1))
B1.grid(row=0, column=1)
B2 = tkinter.Button(top, text ="Paper", command = lambda: rps(win, lose, 2))
B2.grid(row=0, column=2)
B3 = tkinter.Button(top, text ="Scissors", command = lambda: rps(win, lose, 3))
B3.grid(row=0, column=3)
B4 = tkinter.Button(top, text ="Person", command = lambda: rps(win, lose, 4))
B4.grid(row=1, column=1)
B5 = tkinter.Button(top, text ="Lizard", command = lambda: rps(win, lose, 5))
B5.grid(row=1, column=3)
Brestart = tkinter.Button(top,bg="red3",fg="white", text ="Restart", command = lambda: restartbtn())
Brestart.grid(row=5, column=2)

var = StringVar()
var.set(emoji.emojize(':waving_hand:.:waving_hand:.:waving_hand:'))
l = Label(top, textvariable = var)
l.grid(row=2, column=2)
l.configure(font=("helvetica bold", 26))
wins = IntVar()
wins.set(win)
loses=IntVar()
loses.set(lose)
w = Label(top, textvariable = wins,font=("helvetica bold", 15))
w.grid(row=4, column=1)
w2 = Label(top, textvariable = loses,font=("helvetica bold", 15))
w2.grid(row=4, column=3)
labeled = Label(top, text = "Player Score:",font=("helvetica bold", 15))
labeled.grid(row=3, column=1)
labeled2 = Label(top, text = "Robot Score:",font=("helvetica bold", 15))
labeled2.grid(row=3, column=3)
top.configure(bg="white")
B1.configure(bg="white",fg="grey20")
B2.configure(bg="white",fg="grey20")
B3.configure(bg="white",fg="grey20")
B4.configure(bg="white",fg="grey20")
B5.configure(bg="white",fg="grey20")
l.configure(bg="white",fg="grey20")
w.configure(bg="white",fg="grey20")
w2.configure(bg="white",fg="grey20")
labeled.configure(bg="white",fg="grey20")
labeled2.configure(bg="white",fg="grey20")
top.iconbitmap("RPSLS.ico")
top.mainloop()
