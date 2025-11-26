def signin():
    import pickle
    st=[]
    found=False
    f=open("user.dat","rb+")
    a=input('USER NAME:')
    b=input('PHONE No.:')
    try:
        while True:
            p=f.tell()
            st=pickle.load(f)
            if st['phone_no']==b:
                found=True
                print("\t\t-------------------------------------------------------------------------------")
                print("\t\t\t LOGIN SUCCESSFUL")
                print("\t\t-------------------------------------------------------------------------------")
                break
        if found==True:
            main()
    except EOFError:
        if found==False:
            print("ACCOUNT DOES NOT EXISTS or WRONG ENTRY")
        f.close()
# FUNCTION DEFINITION
def signup():
    import pickle
    f=open("user.dat","ab")
    n=input('ENTER YOUR FULL NAME:')
    ph=input('ENTER YOUR PHONE No.:')
    a=input("ENTER  YOUR AGE:")
    print("MALE->M","FEMALE->F")
    g=input("ENTER YOUR GENDER (M/F):")
    print("ENTER YOUR DATE OF BIRTH:")
    d=input("date(dd):")
    m=input("month(mm):")
    y=input("year(yyyy):")
    dob=y+'/'+m+'/'+d
    s={"username":n,"phone_no":ph,"age":a,"gender":g,"date_of_birth":dob}
    pickle.dump(s,f)
    f.close()
    print("\t\t-------------------------------------------------------")
    print("\t\t\tSIGN UP SUCCESSFUL")
    print("\t\t-------------------------------------------------------")
    main()

#FUNCTION DEFINITION
def main():
    while True:
        print("\t\t---------------------------------------------------")
        print("\t\t\t---------MENU---------")
        print("\t\t\t 1.TRAIN DETAILS")
        print("\t\t\t 2.CHECK SEAT AVAILABILITY")
        print("\t\t\t 3.TICKET BOOKING")
        print("\t\t\t 4.VIEW TICKET")
        print("\t\t\t 5.TICKET CANCELLATION")
        print("\t\t\t 6.CHECK PNR STATUS")
        print("\t\t\t 7.ADD TRAIN DETAILS")
        print("\t\t\t 8.DELETE TRAIN DETAILS")
        print("\t\t\t 9.LOG OUT")
        print("\t\t---------------------------------------------------")
        ch=int(input("ENTER YOUR CHOICE(1/2/3/4):"))
        if ch==1:
            display()
            
        elif ch==2:
            seat_availability()
            
        elif ch==3:
            ticket_booking()
        
        elif ch==4:
            tickets_checking()
            
        elif ch==5:
            tickets_cancellation()
            
        elif ch==6:
            pnr_check()
            
        elif ch==7:
            add_tdetails()

        elif ch==8:
            del_train()
            
        elif ch==9:
            log_out()
            break
        
        else:
            print("ERROR 404 PAGE NOT FOUND")

#FUNCTION DEFINITION
def ticket_booking():
    n=input('ENTER YOUR FULL NAME:')
    ph=input('ENTER YOUR PHONE No.:')
    a=int(input("ENTER  YOUR AGE:"))
    print("MALE->M","FEMALE->F")
    g=input("ENTER YOUR GENDER (M/F):")
    f=input("ENTER THE DEPARTURE PLACE")
    k=input("ENTER THE ARRIVAL PLACE:")
    tn=input("ENTER THE TRAIN NAME:")
    print("ENTER THE DATE OF JOURNEY")
    d=input("date(dd):")
    m=input("month(mm):")
    y=input("year(yyyy):")
    
    import random
    r=random.randint(1000,10000)
    sr=n[0]+str(r)
    doj=y+'/'+m+'/'+d
    
    s="insert into records (name,phno,age,gender,from_f,to_t,date_of_reservation,train_name,pnr) values ('{}','{}',{},'{}','{}','{}','{}','{}','{}')".format(n,ph,a,g,f,k,doj,tn,sr)
    cur.execute(s)
    print("\t\t---------------------------------------------------")
    print("\t\t\tTICKET BOOKED SUCCESSFULLY")
    print("\t\t---------------------------------------------------")
    main()

#FUNCTION DEFINITION
def tickets_checking():
    ph=input("ENTER YOUR REGISTERED PHONE No.")
    try:
        s=("select*from records where phno='{}'".format(ph))
        cur.execute(s)
        data=cur.fetchone()
        y=list(data)
        w=['NAME','PHONE No.','AGE','GENDER','STARTING POINT','DESTINATION','DATE','TRAIN_NAME','PNR No.']
        for i in range(0,len(w)):
            print(w[i],"-->",y[i])
    except:
        print("TICKETS DOES NOT EXISTS")
        main()

#FUNCTION DEFINITION
def tickets_cancellation():
    phno=input("ENTER YOUR REGISTERED PHONE No.")
    s=("select*from records where phno='{}'".format(phno))
    cur.execute(s)
    data=cur.fetchone()
    if data[1]==phno:
        s1="delete from records where phno='{}'".format(phno)
        cur.execute(s1)
        print("\t\t---------------------------------------------------")
        print("\t\t\tTICKET CANCELED SUCCESSFULLY")
        print("\t\t---------------------------------------------------")
    else:
        print("TICKETS DOES NOT EXISTS or WRONG ENTRY")
        main()

#FUNCTION DEFINITION
def add_tdetails():
    
    lst=[]
    tn=input('ENTER THE TRAIN NAME:')
    lst.append(tn)
    tno=input('ENTER THE TRAIN No.:')
    lst.append(tno)
    a=input("ENTER THE SOURCE OF TRAIN:")
    lst.append(a)
    d=input("ENTER THE DESTINATION OF TRAIN:")
    lst.append(d)
    e=int(input("ENTER TOTAL No. OF SEATS IN THE TRAIN:"))
    lst.append(e)
    s="select*from train_details where t_no='{}'".format(tno)
    cur.execute(s)
    data=cur.fetchall()
    if is_empty(data)==True:

        s="insert into train_details (t_name,t_no,source,destination,seat) values (%s,%s,%s,%s,%s)"
        cur.execute(s,lst)
        print("\t\t---------------------------------------------------")
        print("\t\t\tDETAILS ADDED SUCCESSFULLY")
        print("\t\t---------------------------------------------------")
    else:
        print("------------------------------")
        print("\t\tDUPLICATE ENTRY, train with same train_no. already exist")
        print("------------------------------")
#FUNCTION DEFINITION
def display():
    a=1
    s="select*from train_details;"
    cur.execute(s)
    data=cur.fetchall()
    if is_empty(data)==True:
        print("\t\t---------------------------------------------------")
        print("\t\t\t TRAIN DETAILS NOT FOUND")
        print("\t\t---------------------------------------------------")
    else:
        print("\t\t\tTRAIN DETAILS:")
        print("\t\t---------------------------------------------------")
        print(" ")
        for i in data:
            print("\t\t",a,":",i)
            a+=1
        print(" ")
        print("\t\t---------------------------------------------------")

#FUNCTION DEFINITION
def pnr_check():
    found=False
    pno=input('ENTER YOUR PNR No.:')
    s="select pnr from records;"
    cur.execute(s)
    data=cur.fetchall()
    for i in data:
        if pno in i:
            found=True
            break
        else:
            found=False
    if found==True:
        s1="select t_no from records,train_details where pnr='{}'".format(pno)
        cur.execute(s1)
        data=cur.fetchall()
        tno=data[0][0]
        s=("select seat from train_details where t_no='{}'".format(tno))
        cur.execute(s)
        d=cur.fetchone()
        s="select t_no,count(*) from train_details GROUP BY t_no having t_no='{}'".format(tno)
        cur.execute(s)
        data=cur.fetchone()

        if int(data[1])<int(d[0]):
            print("\t\t---------------------------------------------------")
            print("\t\t PNR STATUS :- CONFIRMED\t\t\t")
            print("\t\t---------------------------------------------------")
        else:
            print("\t\t---------------------------------------------------")
            print("\t\t" ,'PNR STATUS:- WAITING',"\t\t\t")
            print("\t\t---------------------------------------------------")
    elif found==False:
        print("PNR NOT FOUND")
        
#FUNCTION DEFINITION
def seat_availability():
    found=False
    tno=input('ENTER THE TRAIN No.:')
    s="select t_no from train_details;"
    cur.execute(s)
    data=cur.fetchall()
    for i in data:
        if tno in i:
            found=True
            break
        else:
            found=False
            
    if found==True:
        s=("select seat from train_details where t_no='{}'".format(tno))
        cur.execute(s)
        d=cur.fetchone()
        s1=("select t_name from train_details where t_no='{}'".format(tno))
        cur.execute(s1)
        q=cur.fetchall()
        tname=q[0][0]
        s="select train_name,count(*) from records GROUP BY train_name having train_name='{}'".format(tname)
        cur.execute(s)
        data=cur.fetchall()
        
        if is_empty(data)==True:
            print("\t\t---------------------------------------------------")
            print("\t\t NO SEAT RESERVED OUT OF ",int(d[0]),"\t\t\t")
            print("\t\t---------------------------------------------------")
        else:
            if int(data[0][1])<int(d[0]):
                print("\t\t---------------------------------------------------")
                print("\t\t",int(data[0][1]),"SEAT(S) RESERVED OUT OF ",int(d[0]),"\t\t\t")
                print("\t\t---------------------------------------------------")
            else:
                print("\t\t---------------------------------------------------")
                print("ALL THE SEATS RESERVED")
                print("\t\t---------------------------------------------------")
    else:
        print("TRAIN No. NOT FOUUND")

#FUNCTION DEFINITION
def is_empty(lst):
    if lst==[]:
        return True
    else:
        return False

#FUNCTION DEFINITION
def del_train():
    x=input("ENTER THE TRAIN No.:")
    s=("select*from train_details where t_no='{}'".format(x))
    cur.execute(s)
    data=cur.fetchone()
    
    if data[1]==x:
        s1="delete from train_details where t_no='{}'".format(x)
        cur.execute(s1)
        print("\t\t---------------------------------------------------")
        print("\t\t\tTRAIN DETAILS REMOVED SUCCESSFULLY")
        print("\t\t---------------------------------------------------")
    else:
        print("TRAIN NOT FOUND or WRONG ENTRY")

#FUNCTION DEFINITION
def log_out():
    print("\t\t---------------------------------------------------")
    print("\t\t\tTHANK YOU")
    print("\t\t\tLOGGED OUT SUCCESSFULLY")
    print("\t\t---------------------------------------------------")

#_MAIN_
import mysql.connector as sql
con=sql.connect(host="localhost",user="root",passwd="123456",autocommit=True)
cur=con.cursor()


#DATABASE CREATION IF NOT EXISTS
s1="create database if not exists railway;"
cur.execute(s1)
s1="use railway;"
cur.execute(s1)
con.commit()

#TABLE CREATION IF NOT EXISTS
s1="create table if not exists records (name varchar(100),phno varchar(10) primary key,age int(4),\
gender varchar(100),from_f varchar(50),to_t varchar(50),date_of_reservation date,train_name varchar(100),pnr varchar(100));"
cur.execute(s1)
con.commit()

#TABLE CREATION IF NOT EXISTS
s1="create table if not exists user (u_name varchar(100),u_phno varchar(10) primary key,u_age int(4),\
u_gender varchar(100),dob date);"
cur.execute(s1)
con.commit()

print("________________________________________________________________________")

# TABLE CREATION IF NOT EXISTS
s1="create table if not exists train_details (t_name varchar(50) not null,t_no varchar(50) primary key,source varchar(100),destination varchar(100),seat int);"
cur.execute(s1)
con.commit()

s1=("select * from train_details;")
cur.execute(s1)
data=cur.fetchall()
if is_empty(data)==True:
    s="insert into train_details (t_name,t_no,source,destination,seat) values ('JAMMU TAVI','12367','KATRA','DELHI',90);"
    cur.execute(s)
    s="insert into train_details (t_name,t_no,source,destination,seat) values ('MUMBAI RAJDHANI','12952','DELHI','MUMBAI',100);"
    cur.execute(s)
    s="insert into train_details (t_name,t_no,source,destination,seat) values('VANDE BHARAT','22436','NEW DELHI','VARANASI',120);"
    cur.execute(s)
    s="insert into train_details (t_name,t_no,source,destination,seat) values('MAHAKAL SUPERFAST EXP.','82401','VARANASI','UJJAIN',80);"
    cur.execute(s)
    con.commit()

while True:
    print("\t\tWELCOME TO RAILWAY RESERVATION SYSTEM")
    print("-----------------------------------------------------------------------------------")
    print("\t\t\t 1. SIGN IN")
    print("\t\t\t 2. SIGN UP")
    print("\t\t\t 3. EXIT")
    print("----------------------------------------------------------------------------------")
    print("------PLEASE ENTER ALLTHE INFORMATION IN CAPITAL LETTERS---------")
    ch=int(input("enter your choice (1/2/3) :"))
    
    if ch==1:
        signin()
        
    elif ch==2:
        signup()
        
    elif ch==3:
        print('\t\t----------------------------------------------------')
        print('\t\t\t THANK YOU')
        print('\t\t\tYOU ARE EXITED')
        print("\t\t---------------------------------------------------")
        break
    
    else:
        print("ERROR 404 PAGE NOT FOUND" )
        break