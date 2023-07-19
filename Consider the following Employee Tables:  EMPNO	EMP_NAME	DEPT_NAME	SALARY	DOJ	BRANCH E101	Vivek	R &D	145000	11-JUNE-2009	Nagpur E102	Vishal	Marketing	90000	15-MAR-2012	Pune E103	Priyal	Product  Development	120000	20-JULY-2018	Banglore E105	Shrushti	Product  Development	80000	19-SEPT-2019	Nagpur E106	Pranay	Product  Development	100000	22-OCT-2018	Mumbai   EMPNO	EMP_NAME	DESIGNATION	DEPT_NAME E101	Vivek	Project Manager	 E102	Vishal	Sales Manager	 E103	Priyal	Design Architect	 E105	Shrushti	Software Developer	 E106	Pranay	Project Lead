PROGRAM :

--CREATE DATABASE
CREATE DATABASE EMP;
USE EMP;


-- Create the Employee_Table
CREATE table Emp_tb(EMPNO varchar(255), EMP_NAME varchar(255), DEPT_NAME varchar(255), SALARY int, DOJ varchar(255), BRANCH varchar(255));

-- Create the Employee_Details Table
CREATE table Emp_Details_table(EMPNO varchar(255), EMP_NAME varchar(255), DESIGNATION varchar(255), DEPT_NAME varchar(255));

-- Insert all entries in Employee Table
INSERT INTO Emp_tb
VALUES("E101","Vivek","R&D",145000,"11-JUNE-2009","Nagpur");
VALUES("E102","Vishal","Marketing",90000,"15-MAR-2012","Pune");
VALUES("E103","Priyal","Product Development",12000,"20-JULY-2018","Banglore");
VALUES("E105","Shrushti","Product Development",80000,"19-SEPT-2019","Nagpur");
VALUES("E106","Pranay","Product Development",10000,"22-OCT-2018","Mumbai");


-- Insert all entries in Employee_Details_Table
INSERT INTO Emp_Details_table(EMPNO, EMP_NAME, DESIGNATION)
VALUES("E101","Vivek","Project Manager");
VALUES("E102","Vishal","Sales Manager");
VALUES("E103","Priyal","Design Architect");
VALUES("E105","Shrushti","Software Developer");
VALUES("E106","Pranay","Project Lead");
 
-- Display all entries from the Employee Table
SELECT*from Emp_tb;

-- Display all entries from the Employee_Details_Table
SELECT*from Emp_Details_table;


-- Display the number of employees 
SELECT COUNT(*) as Employee_Count FROM Emp_tb;


-- Retriving the Employee_no with their respective salary
SELECT EMPNO, salary FROM Emp_tb;

-- Total Salary Of All Employees 
SELECT SUM(SALARY)as Sum_of_all_Employee_salary FROM Emp_tb;

-- Average Salary Of Employee 
SELECT Avg(SALARY)as Average_Salary_of_Employee FROM Emp_tb

-- Displaying the name of the Employees in the Descending Order 
SELECT EMP_NAME as Employee_Name_In_Descending_order FROM Emp_tb ORDER BY EMP_NAME DESC;


-- Retrieve the name of employees and their dept name 
-- Update the EmployeeDetails tables, replace all NULL values in the dept_name 

-- Rec-01 
UPDATE Emp_Details_table  
SET DEPT_NAME="IT" 
WHERE EMPNO='E101';

-- Rec-02 
UPDATE Emp_Details_table  
SET DEPT_NAME="Marketing" 
WHERE EMPNO='E102';

-- Rec-03 
UPDATE Emp_Details_table  
SET DEPT_NAME="Testing" 
WHERE EMPNO='E103';

-- Rec-04 
UPDATE Emp_Details_table  
SET DEPT_NAME="Developer" 
WHERE EMPNO='E105';

-- Rec-05
UPDATE Emp_Details_table  
SET DEPT_NAME="App Tester" 
WHERE EMPNO='E106';

-- Printing the table content in JSON Format 

SELECT CONCAT (GROUP_CONCAT ('{"EMP_NAME":"',Emp_tb.EMP_NAME,'","DEPT_NAME":"',Emp_Details_table.DEPT_NAME,'"}')) as EmployeeeNameAndDeptInJSON FROM Emp_tb JOIN Emp_Details_table ON Emp_tb.EMPNO=Emp_Details_table.EMPNO;


