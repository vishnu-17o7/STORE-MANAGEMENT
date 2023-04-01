import LOGIN
import datetime as dt
import mysql.connector as sql
from sys import exit
passwd = str(input("ENTER THE DATABASE PASSWORD: "))
# =====================================================#
12
conn = sql.connect(host='localhost', user='root',
                   passwd=passwd, database='Store_Mgmt')
cur = conn.cursor()
# =================================#
print('WELCOME TO OUR CLOTH STORE')
print(dt.datetime.now())
print()
print('1.REGISTER')
print('2.LOGIN')
print('3.EXIT')
print()
# ===============================#
n = int(input('PLEASE ENTER YOUR CHOICE: '))
print()
if n == 1:
    name = input('Enter a Username: ')
    print()
    passwd = int(input('Enter a Password: '))
    print()
    V_SQLInsert = "insert into user_table (passwrd,username) values (" + str
    (passwd) + ",' " + name + " ') "
    cur.execute(V_SQLInsert)
    conn.commit()
    print()
    print('!!!USER SUCCESSFULLY CREATED!!! :)')
if n == 2:
    import LOGIN
if n == 3:
    exit()
