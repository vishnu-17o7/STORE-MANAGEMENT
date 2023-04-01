import mysql.connector as sql
passwd=str(input("ENTER THE DATABASE PASSWORD: "))
conn=sql.connect(host='localhost',user='root',passwd=passwd,database='Store_Mgmt')
cur = conn.cursor()
#=====================================#
print('##PLEASE LOGIN WITH YOUR REGISTERED DETAILS##')
print()
name=input('Enter your Registered Username: ')
passwd=int(input('Enter your Password: '))
V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and username= ' " +name+ " ' "
cur.execute(V_Sql_Sel)
if cur.fetchone() is None:
    print()
    print('Invalid Username or Password')
else:
    print()
    print('!!!SUCCESSSFULLY LOGGED IN!!!')
    import CODE