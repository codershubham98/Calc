#shubham's calculator
from tkinter import *
root = Tk()
root.geometry("500x300")
root.title("Shubham's Calculator")
label=Label(root,text="Shubham's Calculator",font=("Arial Black",10,'bold'))
label.grid()
textin=StringVar()
operator=""
def clickbut(numbers):
	global operator
	operator=operator+str(numbers)
	textin.set(operator)

def equlbut():
	global operator
	add=str(eval(operator))
	textin.set(add)
	operator=''

def equlbut():
	global operator
	sub=str(eval(operator))
	textin.set(sub)
	operator=''

def equlbut():
	global operator
	mul=str(eval(operator))
	textin.set(mul)
	operator=''

def equlbut():
	global operator
	div=str(eval(operator))
	textin.set(div)
	operator=''

def clr():
	textin.set('')

one=Button(root,text="1",bg="red",fg="black",command=lambda:clickbut(1),height=1,width=7)
one.grid(row=0,column=1,columnspan=1)
two=Button(root,text="2",bg="red",fg="black",command=lambda:clickbut(2),height=1,width=7)
two.grid(row=0,column=2,columnspan=1)
three=Button(root,text="3",bg="red",fg="black",command=lambda:clickbut(3),height=1,width=7)
three.grid(row=0,column=3,columnspan=1)
add=Button(root,text="+",bg="red",fg="black",command=lambda:clickbut("+"),height=1,width=7)
add.grid(row=0,column=4,columnspan=1)
four=Button(root,text="4",bg="red",fg="black",command=lambda:clickbut(4),height=1,width=7)
four.grid(row=1,column=1,columnspan=1)
five=Button(root,text="5",bg="red",fg="black",command=lambda:clickbut(5),height=1,width=7)
five.grid(row=1,column=2,columnspan=1)
six=Button(root,text="6",bg="red",fg="black",command=lambda:clickbut(6),height=1,width=7)
six.grid(row=1,column=3,columnspan=1)
sub=Button(root,text="-",bg="red",fg="black",command=lambda:clickbut("-"),height=1,width=7)
sub.grid(row=1,column=4,columnspan=1)
seven=Button(root,text="7",bg="red",fg="black",command=lambda:clickbut(7),height=1,width=7)
seven.grid(row=2,column=1,columnspan=1)
eight=Button(root,text="8",bg="red",fg="black",command=lambda:clickbut(8),height=1,width=7)
eight.grid(row=2,column=2,columnspan=1)
nine=Button(root,text="9",bg="red",fg="black",command=lambda:clickbut(9),height=1,width=7)
nine.grid(row=2,column=3,columnspan=1)
mult=Button(root,text="*",bg="red",fg="black",command=lambda:clickbut("*"),height=1,width=7)
mult.grid(row=2,column=4,columnspan=1)
clear=Button(root,text="Clear",highlightcolor="yellow",bg="red",fg="black",command=lambda:clr(),height=1,width=7)
clear.grid(row=3,column=1,columnspan=1)
zero=Button(root,text="0",bg="red",fg="black",command=lambda:clickbut(0),height=1,width=7)
zero.grid(row=3,column=2,columnspan=1)
div=Button(root,text="/",bg="red",fg="black",command=lambda:clickbut("/"),height=1,width=7)
div.grid(row=3,column=3,columnspan=1)
eq=Button(root,text="=",activebackground="black",bg="red",fg="black",command=lambda:equlbut(),height=1,width=7)
eq.grid(row=3,column=4,columnspan=1)
entry=Entry(root,textvar=textin,bg="yellow",bd=5,fg="green")
entry.grid(columnspan=4)
root.mainloop()