import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
def show():
    messagebox.showinfo("Submitted","Welcome "+nameenter.get()+" "+lnameenter.get()+"\n You have Successfully Registered!")
m=tk.Tk()
m.minsize(600,200)
m.title("Python GUI Form")
heading=tk.Label(m,text="Registration From",fg="red",font="Verdana 20 bold italic",justify="center")
heading.grid(row=1,column=4,columnspan=6)
name=tk.Label(m,text="First Name : ")
name.grid(row=5,column=3)
nameenter=tk.Entry(m)
nameenter.grid(row=5,column=4)
lname=tk.Label(m,text="Last Name : ")
lname.grid(row=5,column=5)
lnameenter=tk.Entry(m)
lnameenter.grid(row=5,column=6)
gender=tk.Label(m,text="Gender : ")
gender.grid(row=6,column=3)
var=tk.BooleanVar()
rb1=tk.Radiobutton(m,text="Male",variable=var,value=True)
rb1.grid(row=6,column=4)
rb2=tk.Radiobutton(m,text="Female",variable=var,value=False)
rb2.grid(row=6,column=5)
subject=tk.Label(m,text="Subjects : ").grid(row=7,column=3)
m4var=tk.BooleanVar()
m4=tk.Checkbutton(m,text="Applied Mathematics IV",variable=m4var).grid(row=7,column=4)
pyvar=tk.BooleanVar()
python=tk.Checkbutton(m,text="Python Programming",variable=pyvar).grid(row=7,column=5)
javavar=tk.BooleanVar()
java=tk.Checkbutton(m,text="Java Programming",variable=javavar).grid(row=8,column=4)
cppvar=tk.BooleanVar()
cpp=tk.Checkbutton(m,text="C++ Programming",variable=cppvar).grid(row=8,column=5)
dept=tk.Label(m,text="Department : ").grid(row=9,column=3)
depart=ttk.Combobox(m,values=["Select Department...","Information Technology","Computer Engineering","Mechanical Engineering"]).grid(row=9,column=4)
submit=tk.Button(m,text="Submit",command=show).grid(row=12,column=4)
cancel=tk.Button(m,text="Quit",command=quit).grid(row=12,column=5)
m.mainloop()