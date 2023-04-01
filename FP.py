import tkinter as t 
from tkinter import *
from PIL import Image, ImageTk 
import datetime as dt

def admin(): 
    import CODE
    frontpage.destroy()

def customer():
    import CUSTOMER 
    frontpage.destroy()

frontpage=t.Tk()


C = Canvas(frontpage, bg="blue", height=250, width=300) 
filename = PhotoImage(file = r"C:\Users\vishn\OneDrive\Desktop\Programs\PROJEKT\welcome.jpg")
background_label = Label(frontpage, image=filename) 
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = Frame(frontpage, width=176, height=224) 
frame.pack()
frame.place(anchor='nw', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("reddy.png"))
label = Label(frame, image = img) 
label.pack()

frontpage.title('MAINPAGE') 
frontpage.configure(bg="SteelBlue1") 
frontpage.geometry('958x599')
date = dt.datetime.now()
label1 = t.Label(frontpage, text="WELCOME TO REDDY STORES",bg='white',fg='red', font="Times, 25") 
label1.pack()
label = t.Label(frontpage, text=f"{date:%A, %B %d,%Y}",bg='white',fg="blue", font="Calibri, 12") 
label.pack(pady=10)

button1= t.Button(frontpage,activebackground="blue", text="ADMIN",bd=8, width=25, font=("Times", 14),command=admin)
button1.pack(side=RIGHT)


button2= t.Button(frontpage,activebackground="blue", text="CUSTOMER",bd=8, width=25, font=("Times", 14),command=customer) 
button2.pack(side=LEFT,padx=100, pady=50)

shopname=t.Label(frontpage,text='WELCOME TO OUR STORE',font="Times, 20")
 
frontpage.mainloop()