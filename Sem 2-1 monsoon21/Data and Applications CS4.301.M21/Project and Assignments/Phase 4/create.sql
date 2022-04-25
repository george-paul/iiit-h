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
