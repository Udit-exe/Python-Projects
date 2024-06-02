import mysql.connector
import random

# Connect to MySQL database
db = input("Enter name of the database: ")

# Establishing connection to MySQL
mydb = mysql.connector.connect(host='localhost', user='root', password='uditsql')
if mydb.is_connected():
    print("Connection Successful..")
    mycursor = mydb.cursor()

    # Create database if not exists
    sql = "CREATE DATABASE IF NOT EXISTS {}".format(db)
    mycursor.execute(sql)
    print("Database created successfully")

    # Using the specified database
    mycursor.execute("USE {}".format(db))

    # Creating tables
    TableName = input("Name of Table to be created: ")
    TableName1 = input("Name of Table to be created: ")
    TableName2 = input("Name of Table to be created: ")
    TableName3 = input("Name of Table to be created: ")

    # Creating table queries
    query1 = "CREATE TABLE IF NOT EXISTS {} \
        (Name varchar(50), \
        Phone bigint, \
        No_Tickets integer, \
        Sex varchar(10), \
        First_Name varchar(50), \
        Last_Name varchar(50), \
        Email_ID varchar(100), \
        Mode_payment varchar(50))".format(TableName)
    mycursor.execute(query1)

    query2 = "CREATE TABLE IF NOT EXISTS {} \
        (Customer_ID varchar(50), \
        movie_name varchar(50), \
        Amount int)".format(TableName1)
    mycursor.execute(query2)

    query3 = "CREATE TABLE IF NOT EXISTS {} \
        (Customer_ID varchar(50), \
        movie_name varchar(50), \
        Amount int)".format(TableName2)
    mycursor.execute(query3)

    query4 = "CREATE TABLE IF NOT EXISTS {} \
        (Customer_ID varchar(50), \
        movie_name varchar(50), \
        Amount int)".format(TableName3)
    mycursor.execute(query4)

    if mydb.is_connected():
        print("Enter your choice as 1, 2, 3, or 4")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ POPFLIX THEATRE BOOKING $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4$$$$$$$$$$$$$$")
        print("YOUR SAFETY IS OUR PRIORITY")
        print("Use of masks")
        print("Sanitization after each show")
        print("Social distancing in cinema halls")
        print("Mandatory temperature checks")
        print("POPFLIX THEATRE")

        # Show details
        ch = input("do you want to check the show details(yes/no): ")
        if ch.lower() == 'yes':
            print("*" * 150)
            print("SHOW DETAILS")
            print("*" * 150)

            sh = input("Select Shows (a.Morning Show / b.Noon Show / c. Night Show): ")

            if sh == 'a':
                print("Time: 9:00 A.M")
                print("*" * 30, " Movies", "*" * 30)
                print("Screen 1. Ava")
                print("Screen 2. AquaMan")

            elif sh == 'b':
                print("Time: 1:00 P.M")
                print("*" * 30, " Movies", "*" * 30)
                print("Screen 1. After")
                print("Screen 2. Lucy")

            elif sh == 'c':
                print("Time: 10:00 P.M")
                print("*" * 30, " Movies", "*" * 30)
                print("Screen 1. Ava")
                print("Screen 2. Baywatch")

            print("**********************************************CUSTOMER DETAILS GATEWAY**********************************************************")

            # Gathering customer details
            v_mname = input("Enter the movie name: ")
            v_phone = input("Enter your Phone number: ")
            v_tic = input("Enter total tickets: ")
            v_sex = input("Enter your sex: ")
            v_fname = input("Enter your first name: ")
            v_lname = input("Enter your last name: ")
            v_Email_ID = input("Enter your Email ID: ")
            v_mpayment = input("Enter mode of payment(Debit or Credit card/UPI/Net Banking): ")

            # Generating customer ID
            print("Type OK to Generate your one-time Customer ID")
            m = input("Enter OK: ")
            if m.lower() == 'ok':
                choices = list(range(1000))
                random.shuffle(choices)
                print("Your Member_ID is", choices.pop())
                v_ins = "INSERT INTO {} VALUES('{}', {}, {}, '{}', '{}', '{}', '{}', '{}')".format(
                    TableName, v_mname, v_phone, v_tic, v_sex, v_fname, v_lname, v_Email_ID, v_mpayment
                )
                mycursor.execute(v_ins)
                mydb.commit()

                # Ticket booking options
                print("SCREEN AND SEAT BOOKING GATEWAY")
                print("1.GOLD [4dx] Ticket Booking")
                print(" Price per Ticket: Rs.1500 ")
                print("2.IMAX Ticket Booking")
                print(" Price per Ticket: Rs.850 ")
                print("3.Silver Ticket Booking")
                print(" Price per Ticket: Rs.500 ")
                choice = int(input("Enter your choice: "))

                # Ticket booking based on choice
                if choice == 1:
                    print("WELCOME TO GOLD 4DX CINEMA BOOKING")
                    a = input("Enter your one-time Customer ID: ")
                    c = input("Enter your movie name: ")
                    d = int(input("Enter the number of tickets: "))
                    total = d * 1500
                    print("Bill for the tickets:", total)
                    pswd = input("Your payment OTP: ")
                    sks = input("Your complimentary snacks(chips/popcorn/no): ")
                    dd = input("Your complementary drink(coke/pepsi/no): ")
                    v_dx = "INSERT INTO 4dx VALUES('{}', '{}', {})".format(a, c, total)
                    mycursor.execute(v_dx)
                    mydb.commit()
                    print("TICKET BOOKED")
                    print("ENJOY THE MOVIE AND HAVE FUN")

                elif choice == 2:
                    print("WELCOME TO IMAX TICKET BOOKING")
                    aa = input("Enter your one-time Customer ID: ")
                    cc = input("Enter your movie name: ")
                    dd = int(input("Enter number of tickets: "))
                    ttotal = dd * 850
                    print("Bill for the tickets:", ttotal)
                    pswd = input("Your payment OTP: ")
                    sks = input("Your complimentary snacks(chips/popcorn/no): ")
                    dd = input("Your complementary drink(coke/pepsi/no): ")
                    v_dy = "INSERT INTO imax VALUES('{}', '{}', {})".format(aa, cc, ttotal)
                    mycursor.execute(v_dy)
                    mydb.commit()
                    print("TICKET BOOKED")
                    print("ENJOY THE MOVIE AND HAVE FUN")

                elif choice == 3:
                    print("WELCOME TO SILVER TICKET BOOKING")
                    aaa = input("Enter your one-time Customer ID: ")
                    ccc = input("Enter your movie name: ")
                    ddd = int(input("Enter number of Tickets: "))
                    tttotal = ddd * 500
                    print("Bill for the tickets:", tttotal)
                    pswd = input("Your payment OTP: ")
                    v_dz = "INSERT INTO silver VALUES('{}', '{}', {})".format(aaa, ccc, tttotal)
                    mycursor.execute(v_dz)
                    mydb.commit()
                    print("TICKET BOOKED")
                    print("ENJOY THE MOVIE AND HAVE FUN")

                else:
                    print("Invalid choice. Thanks for visiting")

            else:
                print("Invalid choice. Thanks for visiting")
