import tkinter as tk 
from tkinter import ttk 
from tkinter import * 
import mysql.connector

def des():
    root.destroy() 
    return

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="store_mgmt")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT item_code,item_name,item_brand,item_price FROM inventory")
    records = mycursor.fetchall() #print(records)
    for i, (item_code,item_name,item_brand,item_price) in enumerate(records, start=1):
        listBox.insert("", "end", values=(item_code,item_name,item_brand,item_price))
        mysqldb.close()



root = tk.Tk() 
root.title("ITEMS") 
root.configure(bg="SteelBlue1")
label = tk.Label(root, text="ITEMS YOU CAN BUY IN OUR STORE",bg='SteelBlue1', font=("Arial",20)).grid(row=0, columnspan=3)
cols = ("ID","NAME","BRAND","PRICE")
listBox = ttk.Treeview(root, columns=cols, show='headings')


for col in cols: listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)
 




#closeButton = tk.Button(root, text="Close", width=15, command=des).grid(row=4, column=1)
show()


#entry6=Entry(root, font=("Times", 12),justify='left',bd=8,width=25,bg="#EEEEF1"). #entry6.insert(0,"Enter the Item Name To Search")

root.mainloop()
