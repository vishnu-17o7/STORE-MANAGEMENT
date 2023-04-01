from tkinter import *
from tkinter import messagebox 
import mysql.connector
import PIL
passwd=str(input("ENTER THE DATABASE PASSWORD: "))
mydb = mysql.connector.connect(host= "localhost",user = "root",passwd= passwd,database='Store_Mgmt')
my_cursor = mydb.cursor() #================================================#
my_cursor.execute("create database if not exists Store_Mgmt") 
my_cursor.execute("use Store_Mgmt")
my_cursor.execute("create table if not exists inventory (item_code int Primary Key, item_name varchar(50) not null unique,item_brand varchar(50), item_quantity int, item_price float)") #================================================#
root = Tk()
root.title("Reddy Cloth Store") 
root.configure(width=1500,height=600,bg="SteelBlue1") #================================================# #FUNCTIONS#
def additem(): 
    try: 
        e1=entry1.get() 
        e2=entry2.get()
        e3=entry3.get() 
        e4=entry4.get() 
        e5=entry5.get()
        sql = "INSERT INTO inventory (item_code, item_name, item_brand, item_quantity, item_price) VALUES (%s, %s, %s, %s, %s)"
        val = (e1,str(e2),str(e3),e4,e5) 
        my_cursor.execute(sql,val) 
        mydb.commit() 
        entry1.delete(0, END) 
        entry2.delete(0, END) 
        entry3.delete(0, END) 
        entry4.delete(0, END) 
        entry5.delete(0, END)
        messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY	!!!")
    except (mysql.connector.Error,mysql.connector.Warning) as e: messagebox.showerror("DUPLICATE","You are trying to insert a item which is already present in database")
def delete1(): 
     try:
        e6 = entry6.get()
        my_cursor.execute("delete from inventory where item_code = '{0}'".format(e6))
        mydb.commit()
        messagebox.showinfo("DELETE ITEM", "ITEM DELETED SUCCESSFULLY	!!!")            
     except (mysql.connector.Error,mysql.connector.Warning) as e: messagebox.showerror("ERROR","You are trying to delete a item which is not present in database")
 


messagebox.showerror("BLANK","Please Enter Item Code To Delete")

def showdatabase(): 
    root1 = Tk()
    root1.configure(bg="White") 
    root1.title("Cloth Store Database") 
    my_cursor.execute("select * from inventory") 
    mytext1 = my_cursor.fetchall()
    mytext = Text(root1,width=90,height= 20 ,bg= "White",fg="black", font=("Times", 12))
    mytext.insert(END," Item_Code \t\tItem_Name \t\tItem_Brand\t\tItem_Quantity \t\tItem_Price \n")
    mytext.insert(END,"\t\t\t\t\t\t\t\t\n")
    for row in mytext1:
        mytext.insert(END,"	{0} \t\t	{1} \t\t	{2} \t\t	{3} \t\t{4}\n".format(row[0],row[1],row[2],row[3],row[4])) 
        mytext.pack( side = LEFT)
def searchitem(): 
    entry1.delete(0, END) 
    entry2.delete(0, END) 
    entry3.delete(0, END) 
    entry4.delete(0, END) 
    entry5.delete(0, END) 
    e6 = entry6.get()
    if e6 == "Enter the Item Name To Search" or "":
        messagebox.showinfo("Warning","Please first enter Item name for search") 
        my_cursor.execute("select * from inventory where item_name = '{0}'".format(str(e6)))
    mytext1 = my_cursor.fetchone() 
    entry1.insert(0,mytext1[0]) 
    entry2.insert(0,mytext1[1]) 
    entry3.insert(0,mytext1[2]) 
    entry4.insert(0,mytext1[3]) 
    entry5.insert(0,mytext1[4]) 
    entry6.delete(0, END)
    entry6.insert(0,"Enter the Item Name To Search") 

def actualupdate():
    e1 = entry1.get() 
    e2 = entry2.get()
    e3 = entry3.get() 
    e4 = entry4.get()
    e5 = entry5.get() 
    e6 = entry6.get()
    my_cursor.execute
    ("select * from inventory where item_code = '{0}'".format(e6))
    line = my_cursor.fetchone() 
    iname = line[0]
    iprice = line[1]
    iquantity = line[2]
    icategory = line[3] 
    idiscount = line[4] 
    if e1!="Update": 
        icode=e1
    if e2!="Update" :
        iname=e2
    if e3!="Update" :
        ibrand=e3
    if e4!="Update" :
        iquantity=e4
    if e5!="Update" :
        iprice=e5
    sql = "update inventory set item_code = %s, item_name = %s, item_brand =%s, item_quantity = %s, item_price = %s where item_code = %s" 
    val = (icode,str(iname),str(ibrand),iquantity,iprice,e6)
    my_cursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("UPDATE ITEM", "ITEM UPDATED SUCCESSFULLY	!!!")
    entry1.delete(0, END) 
    entry2.delete(0, END) 
    entry3.delete(0, END) 
    entry4.delete(0, END) 
    entry5.delete(0, END) 
    entry6.delete(0, END)
    entry6.insert(0,"Enter the Item Code To Update")


def update(): 
    entry1.delete(0, END) 
    entry2.delete(0, END) 
    entry3.delete(0, END) 
    entry4.delete(0, END)
    entry5.delete(0, END) 
    entry6.delete(0, END) 
    entry1.insert(0, "Existing/Update") 
    entry2.insert(0, "Existing/Update") 
    entry3.insert(0, "Existing/Update") 
    entry4.insert(0, "Existing/Update") 
    entry5.insert(0, "Existing/Update")
    entry6.insert(0, "Enter the Item Code To Update")
    button8= Button(root,highlightcolor="blue",activebackground="green", text="UPDATE ITEM",bd=8, bg="#49D810", fg="black", width=25, font=("Times", 14),command=actualupdate)
    button8.grid(row=5,column=2, padx=10, pady=10)




def clearitem(): 
    entry1.delete(0, END) 
    entry2.delete(0, END) 
    entry3.delete(0, END) 
    entry4.delete(0, END) 
    entry5.delete(0, END) 
    entry6.delete(0, END)

def qExit():
    qExit= messagebox.askyesno("QUIT SYSTEM"," Do you want to quit?\nThank You...") 
    if qExit > 0:
        root.destroy()
        return
 #=========================#
#LABLE ENTRIES AND PLACE
label0= Label(root,text="WELCOME TO REDDY CLOTH STORE",bg="SteelBlue1",fg="Red",font=("Copperplate Gothic Bold", 26))
label1=Label(root,text="ENTER ITEM CODE",bg="black",relief="groove",fg="white",bd=12,font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 12),bd=8,width=25,bg="white") 
label2=Label(root, text="ENTER ITEM NAME",relief="groove",height="1",bg="black",bd=12,fg="white", font=("Times", 12),width=25)
entry2= Entry(root, font=("Times", 12),bd=8,width=25,bg="white") 
label3=Label(root, text="ENTER ITEM BRAND", relief="groove", bg="black", bd=12,fg="white", font=("Times", 12),width=25) 
entry3= Entry(root, font=("Times", 12),bd=8,width=25,bg="white")
label4=Label(root, text="ENTER ITEM QUANTITY", relief="groove", bg="black",bd=12,fg="white", font=("Times", 12), width=25)
entry4= Entry(root, font=("Times", 12),bd=8,width=25,bg="white") 
label5=Label(root, text="ENTER ITEM PRICE", bg="black",relief="groove",fg="white",bd=12, font=("Times", 12), width=25) 
entry5= Entry(root, font=("Times", 12),bd=8,width=25,bg="white") 
buttoncolor="grey"
red="#FF0000"
redfg="#EEEEF1" 
buttonfg="black"
 


button1= Button(root,activebackground="green", text="ADD ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 14),command=additem)
button2= Button(root,activebackground="red", text="DELETE ITEM", bd=8, bg=red, fg=redfg, width =25, font=("Times", 14), command=delete1) 
button3= Button(root,activebackground="green", text="VIEW ITEMS", bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 14),command=showdatabase)
button4= Button(root,activebackground="green", text="SEARCH ITEM", bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 14),command=searchitem)
button5= Button(root,activebackground="green", text="CLEAR SCREEN", bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 14),command=clearitem)
button6= Button(root,activebackground="red", text="EXIT",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 14), command=qExit)
entry6= Entry(root, font=("Times", 12), justify='left',bd=8, width=25, bg="#EEEEF1")
entry6.insert(0,"Enter the Item Name To Search")
button7= Button(root,activebackground="green", text="UPDATE ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 14),command=update) #===============================================# ########POSITION OF ALL BUTTONS AND ENTRIES#######
label0.grid(columnspan=6, padx=10, pady=10) 
label1.grid(row=1,column=0, padx=10, pady=10) 
label2.grid(row=2,column=0, padx=10, pady=10) 
label3.grid(row=3,column=0, padx=10, pady=10)
 


label4.grid(row=4,column=0, padx=10, pady=10) 
label5.grid(row=5,column=0, padx=10, pady=10) 
entry1.grid(row=1,column=1, padx=10, pady=10) 
entry2.grid(row=2,column=1, padx=10, pady=10) 
entry3.grid(row=3,column=1, padx=10, pady=10) 
entry4.grid(row=4,column=1, padx=10, pady=10) 
entry5.grid(row=5,column=1, padx=10, pady=10) 
entry6.grid(row=1,column=2, padx=10, pady=10) 
button1.grid(row=6,column=0, padx=10, pady=10) 
button2.grid(row=6,column=1, padx=10, pady=10) 
button3.grid(row=3,column=2, padx=10, pady=10) 
button4.grid(row=2,column=2, padx=10, pady=10) 
button5.grid(row=4,column=2, padx=10, pady=10)
button6.grid(row=6,column=2, padx=10, pady=10) 
button7.grid(row=5,column=2, padx=10, pady=10) 
root.mainloop()
