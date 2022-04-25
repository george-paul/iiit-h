CREATE DATABASE IF NOT EXISTS ustadhotel;

USE ustadhotel;

-- Create Tables ------------------------------------------------------------------------------


CREATE TABLE Reservation(
PhoneNo varchar(10) NOT NULL UNIQUE,
Name varchar(50) NOT NULL,
Start_DateTime datetime NOT NULL,
TableNum int NOT NULL);

CREATE TABLE Start_End (
Start_DateTime datetime NOT NULL,
End_DateTime datetime NOT NULL);

CREATE TABLE Customer (
CustNumber int NOT NULL,
ResPhone varchar(10) NOT NULL,
Arrived bit(1));

CREATE TABLE Tbl (
TableNumber int NOT NULL,
Capacity int NOT NULL);

CREATE TABLE Ord (
OrderNo int NOT NULL,
TakenTime time NOT NULL,
TotalPrice int NOT NULL);

CREATE TABLE Taken_ETA (
TakenTime time NOT NULL,
ETA time NOT NULL);

CREATE TABLE Employee (
EmpID varchar(10) NOT NULL,
EmpName varchar(50) NOT NULL,
JobType varchar(10),
PartTime bool NOT NULL);

CREATE TABLE Specialities (
EmpID varchar(10) NOT NULL,
Speciality varchar(20) NOT NULL);

CREATE TABLE Making (
CookID varchar(10) NOT NULL,
DishNo int NOT NULL,
TableNo int NOT NULL);

CREATE TABLE Dish (
DishNo int NOT NULL,
TableNum int NOT NULL,
ItemName varchar(50) NOT NULL,
Status varchar(9) NOT NULL);

CREATE TABLE Preferences (
DishNo int NOT NULL,
TableNum int NOT NULL,
Preference varchar(20) NOT NULL);

CREATE TABLE Ordered (
OrderNo int NOT NULL,
DishNo int NOT NULL,
WaiterID varchar(10) NOT NULL);

CREATE TABLE Table_Orders (
OrderNo int NOT NULL,
TableNum int NOT NULL);

CREATE TABLE Menu_Item (
ItemName varchar(50) NOT NULL,
ItemPrice float NOT NULL);

CREATE TABLE Ingredient (
IngName varchar(20) NOT NULL,
Qty float NOT NULL,
IngPrice float NOT NULL,
SupPhno varchar(10) NOT NULL);

CREATE TABLE Supplier (
SupPhno varchar(10) NOT NULL,
SupName varchar(20) NOT NULL);

CREATE TABLE ConsistsOf (
ItemName varchar(50) NOT NULL,
IngName varchar(20) NOT NULL);

ALTER TABLE Reservation
ADD PRIMARY KEY(PhoneNo);

ALTER TABLE Start_End
ADD PRIMARY KEY(Start_DateTime);

ALTER TABLE Customer
ADD PRIMARY KEY(CustNumber, ResPhone);

ALTER TABLE Tbl
ADD PRIMARY KEY(TableNumber);

ALTER TABLE Ord
ADD PRIMARY KEY(OrderNo);

ALTER TABLE Taken_ETA
ADD PRIMARY KEY(TakenTime);

ALTER TABLE Employee
ADD PRIMARY KEY(EmpID);

ALTER TABLE Specialities
ADD PRIMARY KEY(EmpID, Speciality);

ALTER TABLE Making
ADD PRIMARY KEY(CookID, DishNo, TableNo);

ALTER TABLE Dish
ADD PRIMARY KEY(DishNo, TableNum);

ALTER TABLE Preferences
ADD PRIMARY KEY(DishNo, TableNum, Preference);

ALTER TABLE Ordered
ADD PRIMARY KEY(OrderNo, DishNo);

ALTER TABLE Table_Orders
ADD PRIMARY KEY(OrderNo);

ALTER TABLE Menu_Item
ADD PRIMARY KEY(ItemName);

ALTER TABLE Ingredient
ADD PRIMARY KEY(IngName);

ALTER TABLE Supplier
ADD PRIMARY KEY(SupPhno);

ALTER TABLE ConsistsOf
ADD PRIMARY KEY(ItemName, IngName);

ALTER TABLE Reservation
ADD FOREIGN KEY(Start_DateTime) REFERENCES Start_End(Start_DateTime) ON DELETE CASCADE;

ALTER TABLE Customer
ADD FOREIGN KEY(ResPhone) REFERENCES Reservation(PhoneNo) ON DELETE CASCADE;

ALTER TABLE Ord
ADD FOREIGN KEY(TakenTime) REFERENCES Taken_ETA(TakenTime) ON DELETE CASCADE;

ALTER TABLE Making
ADD FOREIGN KEY(DishNo) REFERENCES Dish(DishNo) ON DELETE CASCADE;

ALTER TABLE Making
ADD FOREIGN KEY(TableNo) REFERENCES Tbl(TableNumber) ON DELETE CASCADE;

ALTER TABLE Reservation
ADD FOREIGN KEY(TableNum) REFERENCES Tbl(TableNumber) ON DELETE CASCADE;

ALTER TABLE Dish
ADD FOREIGN KEY(TableNum) REFERENCES Tbl(TableNumber) ON DELETE CASCADE;

ALTER TABLE Dish
ADD FOREIGN KEY(ItemName) REFERENCES Menu_Item(ItemName) ON DELETE CASCADE;

ALTER TABLE Preferences
ADD FOREIGN KEY(TableNum) REFERENCES Tbl(TableNumber) ON DELETE CASCADE;

ALTER TABLE Ordered
ADD FOREIGN KEY(DishNo) REFERENCES Dish(DishNo) ON DELETE CASCADE;

ALTER TABLE Ordered
ADD FOREIGN KEY(WaiterID) REFERENCES Employee(EmpID) ON DELETE CASCADE;

ALTER TABLE Making
ADD FOREIGN KEY(CookID) REFERENCES Employee(EmpID) ON DELETE CASCADE;

ALTER TABLE Specialities
ADD FOREIGN KEY(EmpID) REFERENCES Employee(EmpID) ON DELETE CASCADE;

ALTER TABLE Table_Orders
ADD FOREIGN KEY(TableNum) REFERENCES Tbl(TableNumber) ON DELETE CASCADE;

ALTER TABLE Ingredient
ADD FOREIGN KEY(SupPhno) REFERENCES Supplier(SupPhno) ON DELETE CASCADE;

ALTER TABLE ConsistsOf
ADD FOREIGN KEY(ItemName) REFERENCES Menu_Item(ItemName) ON DELETE CASCADE;

ALTER TABLE ConsistsOf
ADD FOREIGN KEY(IngName) REFERENCES Ingredient(IngName) ON DELETE CASCADE;


-- Insert Sample Data ------------------------------------------------------------------------------

INSERT INTO Menu_Item
VALUES ("Dosa", 15.0);

INSERT INTO Menu_Item
VALUES ("Idli", 20.0);

INSERT INTO Menu_Item
VALUES ("Sambar", 10.0);

INSERT INTO Menu_Item
VALUES ("Minimeal", 75.0);

INSERT INTO Menu_Item
VALUES ("Meal", 125.0);

INSERT INTO Menu_Item
VALUES ("Paneer", 40.0);

INSERT INTO Menu_Item
VALUES ("Porotta", 50.0);

INSERT INTO Menu_Item
VALUES ("Aloo", 25.0);

INSERT INTO Menu_Item
VALUES ("Puri", 20.0);

-- ----------------------------------------------------------------

INSERT INTO Supplier
VALUES ("1234567890", "Sup1");

INSERT INTO Supplier
VALUES ("9876543210", "Sup2");

-- ----------------------------------------------------------------

INSERT INTO Ingredient
VALUES ("Urad dal", 10, 500, "1234567890");

INSERT INTO Ingredient
VALUES ("Potato", 50, 4350, "1234567890");

INSERT INTO Ingredient
VALUES ("Mustard", 50, 4350, "1234567890");

INSERT INTO Ingredient
VALUES ("Paneer", 5, 1600, "9876543210");

INSERT INTO Ingredient
VALUES ("Porotta", 100, 1000, "9876543210");

INSERT INTO Ingredient
VALUES ("Flour", 5, 100, "9876543210");

-- ----------------------------------------------------------------

INSERT INTO ConsistsOf
VALUES ("Dosa", "Urad dal");

INSERT INTO ConsistsOf
VALUES ("Idli", "Urad dal");

INSERT INTO ConsistsOf
VALUES ("Sambar", "Potato");

INSERT INTO ConsistsOf
VALUES ("Sambar", "Mustard");

INSERT INTO ConsistsOf
VALUES ("Paneer", "Paneer");

INSERT INTO ConsistsOf
VALUES ("Porotta", "Porotta");

INSERT INTO ConsistsOf
VALUES ("Aloo", "Potato");

INSERT INTO ConsistsOf
VALUES ("Puri", "Flour");

INSERT INTO ConsistsOf
VALUES ("Minimeal", "Flour");

INSERT INTO ConsistsOf
VALUES ("Minimeal", "Porotta");

INSERT INTO ConsistsOf
VALUES ("Minimeal", "Paneer");

INSERT INTO ConsistsOf
VALUES ("Meal", "Flour");

INSERT INTO ConsistsOf
VALUES ("Meal", "Porotta");

INSERT INTO ConsistsOf
VALUES ("Meal", "Paneer");

-- ----------------------------------------------------------------

INSERT INTO Start_End
VALUES ("2021-10-20 09:00:00", "2021-10-20 10:30:00");

INSERT INTO Start_End
VALUES ("2021-10-20 09:30:00", "2021-10-20 11:00:00");

INSERT INTO Start_End
VALUES ("2021-10-20 12:30:00", "2021-10-20 14:00:00");

-- ----------------------------------------------------------------

INSERT INTO Tbl
VALUES (3, 3);

INSERT INTO Tbl
VALUES (7, 4);

INSERT INTO Tbl
VALUES (5, 5);

-- ----------------------------------------------------------------

INSERT INTO Reservation
VALUES ("2718283141", "George", "2021-10-20 09:00:00", 3);

INSERT INTO Reservation
VALUES ("3141592718", "Abhijith", "2021-10-20 09:30:00", 7);

INSERT INTO Reservation
VALUES ("1618271314", "Amal", "2021-10-20 12:30:00", 5);

-- ----------------------------------------------------------------

INSERT INTO Customer
VALUES (1, "2718283141", True);

INSERT INTO Customer
VALUES (2, "2718283141", True);

INSERT INTO Customer
VALUES (3, "2718283141", True);

INSERT INTO Customer
VALUES (4, "3141592718", True);

INSERT INTO Customer
VALUES (5, "3141592718", True);

INSERT INTO Customer
VALUES (6, "3141592718", True);

INSERT INTO Customer
VALUES (7, "3141592718", True);

INSERT INTO Customer
VALUES (8, "1618271314", True);

INSERT INTO Customer
VALUES (9, "1618271314", True);

INSERT INTO Customer
VALUES (10, "1618271314", False);

INSERT INTO Customer
VALUES (11, "1618271314", False);

INSERT INTO Customer
VALUES (12, "1618271314", False);

-- ----------------------------------------------------------------

INSERT INTO Taken_ETA
VALUES ("09:15:00", "09:35:00");

INSERT INTO Taken_ETA
VALUES ("09:30:00", "09:50:00");

INSERT INTO Taken_ETA
VALUES ("10:00:00", "10:20:00");

INSERT INTO Taken_ETA
VALUES ("10:15:00", "10:35:00");

INSERT INTO Taken_ETA
VALUES ("12:30:00", "12:50:00");

-- ----------------------------------------------------------------

INSERT INTO Ord
VALUES (1, "09:15:00", 25);

INSERT INTO Ord
VALUES (2, "09:30:00", 30);

INSERT INTO Ord
VALUES (3, "10:00:00", 45);

INSERT INTO Ord
VALUES (4, "10:15:00", 40);

INSERT INTO Ord
VALUES (5, "12:30:00", 75);

-- ----------------------------------------------------------------

INSERT INTO Employee
VALUES (1, "Pratyaksh", 'C', False);

INSERT INTO Employee
VALUES (2, "Shashwat", 'C', False);

INSERT INTO Employee
VALUES (3, "Vamshi", 'C', False);

INSERT INTO Employee
VALUES (4, "Lakshmanan", 'W', False);

INSERT INTO Employee
VALUES (5, "Srijan", 'W', True);

-- ----------------------------------------------------------------

INSERT INTO Specialities
VALUES (1, "Puri"), (2, "Dosa");

-- ----------------------------------------------------------------

INSERT INTO Dish
VALUES (1, 3, "Dosa", "Delivered"), (2, 3, "Sambar", "Delivered"), (3, 3, "Idli", "Delivered"), (4, 3, "Sambar", "Delivered");

INSERT INTO Dish
VALUES (5, 7, "Puri", "Delivered"), (6, 7, "Aloo", "Delivered"), (7, 7, "Dosa", "Delivered"), (8, 7, "Aloo", "Delivered");

INSERT INTO Dish
VALUES (9, 5, "Minimeal", "Preparing");

INSERT INTO Dish
VALUES (10, 5, "Meal", "Prepared");

-- ----------------------------------------------------------------

INSERT INTO Making
VALUES (1, 1, 3), (3, 2, 3), (2, 3, 3), (3, 4, 3);

INSERT INTO Making
VALUES (1, 5, 7), (2, 6, 7), (3, 7, 7), (2, 8, 7);

INSERT INTO Making
VALUES (1, 9, 5), (3, 9, 5);

INSERT INTO Making
VALUES (2, 10, 5);

-- ----------------------------------------------------------------

INSERT INTO Preferences
VALUES (6, 7, "No chili");

INSERT INTO Preferences
VALUES (4, 5, "No potato") ;

-- ----------------------------------------------------------------

INSERT INTO Ordered
VALUES (1, 1, 4), (1, 2, 4), (2, 3, 4), (2, 4, 4);

INSERT INTO Ordered
VALUES (3, 5, 5), (3, 6, 5), (4, 7, 5), (4, 8, 5);

INSERT INTO Ordered
VALUES (5, 9, 4);

INSERT INTO Ordered
VALUES (5, 10, 5);

-- ----------------------------------------------------------------

INSERT INTO Table_Orders
VALUES (1, 3), (2, 3), (3, 7), (4, 7), (5, 5);

-- ----------------------------------------------------------------
