import mysql.connector
import tabulate
from datetime import date
import random
print("*"*86)
print("*"*30,"DENTAL MANAGEMENT SYSTEM","*"*30)
print("*"*86)
#Login details
Username=input("Enter Username: ")
Password=int(input("Enter Password: "))
while True:
    if Username=='Admin' and Password==12345:
        print("Dental Management Dashboard")
        print("1.Staff")
        print("2.Patient")
        print("3.Invoice")
        print("4.Reports")
        choice=int(input("Choose the field: "))
    while True:
        if choice==1:
            print("STAFF DASHBOARD")
            print("1.Create Staff")
            print("2.Manage Staff")
            choice2=int(input("Type 1 for creation and type 2 for management of staff: "))
            if choice2==1:
                StaffID=int(input("Staff ID: "))
                print("*"*10,"CREATE STAFF","*"*10)
                Name=input("Name: ")
                Age=input("Age: ")
                Address=input("Address: ")
                EmailID=input("EmailID: ")
                Mobile=input("Mobile number: ")
                print("Data Entered successfully")
                sqlCon=mysql.connector.connect(host='localhost',user='root',password='root',database='dental')
                cur =sqlCon.cursor()
                cur.execute("insert into Staff values('{}','{}','{}','{}','{}','{}')".format(StaffID,Name, Age, Address,EmailID,Mobile ))
                sqlCon.commit()
                sqlCon.close()
            elif choice2==2:
                StaffID=int(input("Enter StaffID to proceed: "))
                print("*"*10,"UPDATE STAFF","*"*10)
                Name=input("Name: ")
                Age=input("Age: ")
                Address=input("Address: ")
                EmailID=input("EmailID: ")
                Mobile=input("Mobile number: ")
                print("Record Updated Successfully")
                sqlCon = mysql.connector.connect(host ="localhost",user="root",password="root",database="dental")
                cur = sqlCon.cursor()
                cur.execute("update Staff set Name=%s,Age=%s,Address=%s,EmailID=%s,Mobile=%s where StaffID=%s",( Name, Age, Address,EmailID, Mobile,StaffID  ))
                sqlCon.commit()
                sqlCon.close()
        elif choice==2:
            print("PATIENT RECORD")
            print("1.Create Patient")
            print("2.Manage Patient")
            choice2=int(input("Type 1 for creation and type 2 for management of Patient: "))    
            if choice2==1:
                Name=input("Name: ")
                Age=input("Age: ")
                Address=input("Address: ")
                EmailID=input("EmailID: ")
                Mobile=input("Mobile number: ")
                print("Data Entered successfully")
                
                sqlCon=mysql.connector.connect(host='localhost',user='root',password='root',database='dental')
                cur =sqlCon.cursor()
                cur.execute("insert into Patient values('{}','{}','{}','{}','{}')".format(Name, Age, Address,EmailID,Mobile))
                sqlCon.commit()
                sqlCon.close()
            elif choice2==2:
                Mobile=input("Enter Mobile to proceed: ")
                print("*"*10,"UPDATE PATIENT","*"*10)
                Name=input("Name: ")
                Age=input("Age: ")
                Address=input("Address: ")
                EmailID=input("EmailID: ")
                print("Record Updated Successfully")
                sqlCon = mysql.connector.connect(host ="localhost",user="root",password="root",database="dental")
                cur = sqlCon.cursor()
                cur.execute("update Patient set Name=%s,Age=%s,Address=%s,EmailID=%s where Mobile=%s",( Name ,Age,Address,EmailID,Mobile))
                sqlCon.commit()
                sqlCon.close()
        elif choice == 3:
            Name2 = input("Enter your name: ")
            Address2 = input("Enter your Address: ")
            Phone = input("Enter your phone number: ")
            print("*"*10, "Service Details", "*"*10)
            print("Description: \
            1.Replacement of missing teeth \
            2.Cavity Filling \
            3.Teeth Whitening or Bleaching \
            4.Orthodontic Treatment \
            5.Cosmetic Procedures")
            print("*********************INVOICE*****************")
            print("Bill from: ARYAN DENTAL CLINIC")
            print(" Bill to: ")
            print("Name: ", Name2)
            print("Address: ",Address2)
            print("Phone Number: ", Phone)
            desc = int(input("Enter your choice: "))
            if desc == 1:
                print("Description: 1.Replacement of missing teeth")
                a = 1200
                print("Appointment time: ")
                start_dt = date.today().replace(day=1, month=1).toordinal()
                end_dt = date.today().toordinal()
                random_day = date.fromordinal(random.randint(start_dt, end_dt))
                print(random_day)
                print("Price= ",a)
            elif desc==2:
                print("Description: 2.Cavity Filling")
                a=1500
                print("Appointment time: ")
                start_dt = date.today().replace(day=1, month=1).toordinal()
                end_dt =date.today().toordinal()
                random_day = date.fromordinal(random.randint(start_dt, end_dt))
                print(random_day)
                print("Price= ",a)
            elif desc==3:
                print("Description: 3.Teeth Whitening or Bleaching")
                a=2500
                print("Appointment time: ")
                start_dt = date.today().replace(day=1, month=1).toordinal()
                end_dt = date.today().toordinal()
                random_day = date.fromordinal(random.randint(start_dt, end_dt))
                print(random_day)
                print("Price= ",a)
            elif desc==4:
                print("Description: 4.Orthodontic Treatment")
                a=3000
                print("Appointment time: ")
                start_dt = date.today().replace(day=1, month=1).toordinal()
                end_dt = date.today().toordinal()
                random_day = date.fromordinal(random.randint(start_dt, end_dt))
                print(random_day)
                print("Price= ",a)
            elif desc==5:
                print("Description: 5.Cosmetic procedures")
                a=5000
                print("Appointment time: ")
                start_dt = date.today().replace(day=1, month=1).toordinal()
                end_dt = date.today().toordinal()
                random_day = date.fromordinal(random.randint(start_dt, end_dt))
                print(random_day)
                print("Total= ",a)
            else:
                print("Sorry Service not provided")
                print("******************************THANK YOU VISIT AGAIN*********************************")      
        elif choice == 4:
            print("*"*10, "REPORTS", "*"*10)
            print("1.View Staff Reports")
            print("2.View Patient Reports")
            choice3 = int(input("Type 1 for Staff Reports and type 2 for Patient Reports: "))
            if choice3 == 1:
                sqlCon = mysql.connector.connect(host='localhost', user='root', password='root', database='dental')
                cur = sqlCon.cursor()
                query = "select * from staff"
                cur.execute(query)
                result = cur.fetchall()
                row = ['StaffID', 'Name', 'Age', 'Address', 'EmailID', 'Mobile']
                for row in result:
                    print(row)
                sqlCon.close()
            elif choice3 == 2:
                sqlCon = mysql.connector.connect(host='localhost', user='root', password='root', database='dental')
                cur = sqlCon.cursor()
                query = "select * from patient"
                cur.execute(query)
                result = cur.fetchall()
                row = ['Name', 'Age', 'Address', 'EmailID', 'Mobile']
                for row in result:
                    print(row)
                sqlCon.close()
            else:
                print("Invalid choice for Reports")

    else:
        print("Enter Valid Details")

    
