import tkinter as tk
from tkinter import messagebox
def call():
	messagebox.showinfo("Hello","Welcome "+e.get())
top=tk.Tk()
top.title("Name Input")
l=tk.Label(top,text="Enter Your Name : ")
l.grid(row=1,column=1)
e=tk.Entry(top, bd=5)
e.grid(row=1,column=2)
b=tk.Button(top,text="Press",command=call)
b.grid(columnspan=3,rowspan=3)
top.mainloop()
