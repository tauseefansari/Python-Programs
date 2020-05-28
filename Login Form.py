from tkinter import *
from tkinter import messagebox
def clear():
	user.delete(0,END)
	paswd.delete(0,END)
def msg():
	if paswd.get()=="admin":
		messagebox.showinfo("Form","Welcome "+user.get())
	else:
		messagebox.showinfo("Form","Invalid User")
root=Tk()
root["bg"]="cyan"
heading=Label(root,text="Login Form", font=("Arial",30,"italic"), fg="red",bg="cyan")
heading.place(x=100,y=30)
u=Label(root,text="Enter Username : ",fg="blue",bg="cyan")
u.place(x=20,y=60)
user=Entry(root)
user.place(x=200,y=60)
p=Label(root,text="Enter Password : ",fg="blue",bg="cyan")
p.place(x=40,y=80)
paswd=Entry(root,show="*")
paswd.place(x=200,y=80)
bs=Button(root,text="Submit",command=msg)
bs.place(x=100,y=100)
bc=Button(root,text="Clear",command=clear)
bc.place(x=130,y=100)
clo=Button(root,text="Exit",command=quit)
clo.place(x=160,y=100)
root.mainloop()
