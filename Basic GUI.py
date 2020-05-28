from tkinter import *
from tkinter import messagebox
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
cursor = con.cursor()
# cursor.execute("insert into mytable(username,password) values ('Check','Data')")
con.commit()

def Register():
    root.withdraw()
    root2=Tk()
    root.title("Login Form")
    root2.geometry("512x340")
    root2.resizable(0, 0)
    root2.mainloop()

def ClearData():
    userNameInput.delete(0, END)
    passwordInput.delete(0, END)


def SubmitData():
    if userNameInput.get() != "" or passwordInput.get() != "":
        messagebox.showinfo("Login Form", "Welcome " + userNameInput.get().capitalize())
    else:
        messagebox.askretrycancel("Login Form", "Please Try Again !")


root = Tk()
root.title("Login Form")
root.geometry("512x340")
root.resizable(0, 0)
root.configure(background="lightgray")
user_name = StringVar()
heading = Label(root, text="Login Form", font=("Algerian", 30, "bold italic"), fg="blue", bg="lightgray").pack(pady=30)
userNameLabel = Label(root, text="Username : ", font=("Arial", 14, "italic"), fg="red", bg="lightgray").place(x=80,
                                                                                                              y=120)
userNameInput = Entry(root, font=("Arial", 14, "italic"))
userNameInput.place(x=210, y=120)
passwordLabel = Label(root, text="Password : ", font=("Arial", 14, "italic"), bg="lightgray", fg="red").place(x=80,
                                                                                                              y=180)
passwordInput = Entry(root, show="♦", font=("Arial", 14, "italic"))
passwordInput.place(x=210, y=180)
rememberMe = Checkbutton(root, text="Remember Me", offvalue=0, onvalue=1, font=("Arial", 10, "italic"),
                         bg="lightgray").place(x=210, y=210)
submitButton = Button(root, text="Submit", fg="white", bg="green", font=("Arial", 14, "italic"), relief=RIDGE,
                      command=SubmitData).place(x=150, y=250)
clearButton = Button(root, text="Clear", fg="white", bg="red", font=("Arial", 14, "italic"), relief=RIDGE,
                     command=ClearData).place(x=300, y=250)
register = Button(root, text="Register Here", font=("Arial", 10, "bold"), fg="blue", width=20, bg="orange",command=Register)
register.place(x=341, y=0)
root.mainloop()

root2.geometry