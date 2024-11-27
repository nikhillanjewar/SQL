a)	Commands :

-- SQL DDL(Data Defination Langauge) Commands 

-- LIST THE AVAILABLE DATABASES 
SHOW DATABASES;
	
-- CREATE THE DATA BASE 
CREATE DATABASE Students;

-- USE THE MyDB DATABASE 
USE Students;

-- CREATE TABLE INSIDE THE MyDB DataBase 
CREATE TABLE Studenttable(Roll_Number int,Named_of_the_Student varchar(255),Department varchar(255),Year varchar(255),Section varchar(255),Contact_number varchar(255),Email_ID varchar(255));

-- Alter the table Columns 
ALTER TABLE Employee_table 
    	ADD(CGPA varchar(255));


-- See The Logical Structure Of Students Table 
SHOW Columns from Student_table;


-- Rest of the commands are integrated with pyth0n3 script 

 



b)	Code : 

import mysql.connector 
# Registering the user 
Students= mysql.connector.connect(
  host="localhost",
  user="oem",
  password="Nikhil8975",
  database="Students"
)
print(Students)
query = Students.cursor()
sql_query = "INSERT INTO Stu-dents(Roll_Number,Name_of_the_Student,Department,Year,Section,Contact_number,Email_ID,CGPA) values (%s,%s,%s,%s,%s,%s,%s,%s)"

#query.execute()
data = list()
int_entry = int(input("[+]Enter how many entries you want to enter : "))
int_index = int(1)
while int_entry > 0 :
    print(f"Student Entry  : {int_index}")
    roll_number = int(input("Enter Roll_Number : "))
    name = input("Enter Name_of_the_Student : ")
    department = input("Enter Deaprtment: ")
    year = int(input("Enter the Year : "))
    section = input("Enter the Section : ")
    contact = input("Enter the Contact_Number : ")
    email = input("Enter the Email_ID : ")
    cgpa = float(input("Enter the CGPA : "))
 da-ta.append((Roll_Number,Name_of_the_Student,Department,Year,Section,Contact_number,Email_ID,CGPA))
    int_entry -= 1 
    int_index += 1

query.executemany(sql_query,data)
mydb.commit()
mydb.close()

