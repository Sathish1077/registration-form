from tkinter import *
from PIL import ImageTk, Image
import re


root=Tk()
root.geometry('700x500')
load=Image.open('C:\\Users\\SATHISHKUMAR M\\Downloads\\image2.jpg')
render=ImageTk.PhotoImage(load)
img= Label(root,image=render)
img.place(x=0,y=0 )

def submit_value():
    print("Registration Sucessfully Done")


Label(root, text="Registration Form",font="arial 15 bold").grid(row=0,column=3)

name_user=Label (root,text="User Name")
name_user.grid(row=1,column=2)

password_user=Label(root,text="Password")
password_user.grid(row=2,column=2)

cpass_user=Label(root,text="Confirm Password")
cpass_user.grid(row=3,column=2)

no_user=Label(root,text="Mobile Number")
no_user.grid(row=4,column=2)

name_value = StringVar
password_value = StringVar
cpass_value = StringVar
no_value = StringVar
check_value= IntVar

name_box=Entry(root, textvariable=name_value)
name_box.grid(row=1,column=3)

password_box=Entry(root, textvariable=password_value,show = "*")
password_box.grid(row=2,column=3)

cpass_box=Entry(root,textvariable=cpass_value,show = "*")
cpass_box.grid(row=3,column=3)


no_box=Entry(root,textvariable=no_value)
no_box.grid(row=4,column=3)

check_box = Checkbutton(text="Forget Password!!",variable=check_value)
check_box.grid(row=6,column=3)

Button(text="SUBMIT" , command=submit_value).grid(row=7,column=3)




root.mainloop()
