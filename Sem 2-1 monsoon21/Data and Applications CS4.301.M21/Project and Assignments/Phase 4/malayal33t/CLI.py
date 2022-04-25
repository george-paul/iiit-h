import pymysql
from tabulate import tabulate

# ---------------------- functional reqs ----------------------

# 1. Update Customer when a customer arrives
def customerArrive():
	phno = input("Enter Reservation Phone Number: ")

	# check whether phno exists in reservation
	que = ("select * from Reservation where PhoneNo = '{phno}'")
	cur.execute(que.format(phno = phno))
	tups = cur.fetchall()
	if(len(tups) <= 0):
		print("No reservation under that phone number!")
		return

	# Select all customers in that party
	que = ("select CustNumber "
	"from Customer "
	"where Arrived = 0 and ResPhone = '{phno}' "
	"order by CustNumber")
	cur.execute(que.format(phno = phno))
	tups = cur.fetchall()

	# check if there are even any customers yet to arrive
	if(len(tups) <= 0):
		print("All customers have arrived")
		return
	
	# set n customers to arrived
	n = int(input("How many customers arrived? "))
	que = ("update Customer set Arrived = 1 "
	"where CustNumber = {t}")
	# if n greater than number of customers in that party set n to that
	if(n>len(tups)): n = len(tups)
	for i in range(0,n):
		cur.execute(que.format(t = tups[i][0]))
	print(f"Set {n} customers to arrived in reservation under {phno}")


# 2. Postponed Reservation
def reservationpostponed():
	resphoneno=input("Enter phone number of the reserved person: ")

	# check whether phno exists in reservation
	que = "select * from Reservation where PhoneNo = '{phno}'"
	cur.execute(que.format(phno = resphoneno))
	tups = cur.fetchall()
	if(len(tups) <= 0):
		print("No reservation under that phone number!")
		return

	newtime=input("Enter the time to be changed to (YYYY-MM-DD HH:MM:SS): ")
	print(newtime)
	que="select * from Start_End where Start_DateTime = '{newtime}'"
	cur.execute(que.format(newtime=newtime))
	trialtups=cur.fetchall()
	if(len(trialtups)==0):
		que0="insert into Start_End values ('{newtime}',TIMESTAMPADD(HOUR,2,'{newtime}'))"
		cur.execute(que0.format(newtime=newtime))
	# newtime="'"+newtime+"'"
	que1="update Reservation set Start_DateTime = '{newtime}' where PhoneNo={resphoneno}"
	cur.execute(que1.format(newtime=newtime,resphoneno=resphoneno))
	print("Updated reservations:\n")
	que2 = "select * from Reservation where PhoneNo={resphoneno}"
	cur.execute(que2.format(resphoneno=resphoneno))
	tups = cur.fetchall()
	print("changed reservation as:")
	print(tabulate(tups,headers=["PhoneNo","Name","Start_DateTime","TableNum"]))
	# for r in tups:
	#     print(r[0].strip("'"),",",r[1].strip("'"),",",r[2],",",r[3])
		# print(r)


# 3. Dish is delivered
def dishdelivered():
	DishNo=input("Enter Dishnumber delivered: ")

	# check whether dishno exists in Dish
	que = "select * from Dish where DishNo = '{DishNo}'"
	cur.execute(que.format(DishNo = DishNo))
	tups = cur.fetchall()
	if(len(tups) <= 0):
		print("No such dish number!")
		return

	TableNum=input("Enter tablenumber: ")
	que="Update Dish set Status = 'Delivered' where DishNo={Dish} and TableNum={TableN}"
	# que = ("Update Dish"
	# "set Status = 'Delivered'"
	# "where DishNo={DishNo} and TableNum={TableNum}")
	cur.execute(que.format(Dish=DishNo,TableN=TableNum))
	# print("Updated Dish:\n")
	que2 = "select * from Dish where TableNum={TableN} and DishNo={DishNo}"
	cur.execute(que2.format(TableN=TableNum, DishNo=DishNo))
	tups = cur.fetchall()
	if(len(tups)==0):
		print("Error: Dish already delivered/ doesnt exist")
	else:
		print("Changed dish status as :")
		print(tabulate(tups,headers=["DishNo","TableNum","ItemName","Status"]))
		# for r in tups:
		#     print(r[0],",",r[1],",",r[2].strip("'"),r[3].strip("'"))


# 4. View all reservations
def viewreservations():
	que = "select * from Reservation"
	cur.execute(que)
	tups = cur.fetchall()
	print(tabulate(tups,headers=["PhoneNo","Name","Start_DateTime","TableNum"]))
	# for r in tups:
	#     print(r[0].strip("'"),",",r[1].strip("'"),",",r[2],",",r[3])


# 5. View all menu items
def viewmenuitems():
	que = "select * from Menu_Item"
	cur.execute(que)
	tups = cur.fetchall()
	# print("tups:",type(tups)) tups is a tuple of tuples
	print(tabulate(tups,headers=["Menuitem","Cost"]))
	# for r in tups:
	#     # print("r:",type(r))   r is a tuple
	#     print(r[0].strip("'"),"-",r[1])


# 6. Generate total for an order
def generateTotal():
	ordno = input("Order Number to generate total: ")

	# check whether the ordno exists
	que = ("select * from Ord where OrderNo = {ordno}")
	cur.execute(que.format(ordno=ordno))
	tups = cur.fetchall()
	if(len(tups) <= 0):
		print("Unrecognised Order number")
		return

	que = ("select sum(m.ItemPrice) "
	"from Dish as d, Menu_Item as m, Ordered as o "
	"where d.ItemName = m.ItemName and d.DishNo = o.DishNo and o.OrderNo = {ordno}")
	cur.execute(que.format(ordno=ordno))
	tups = cur.fetchall()
	totalAmt = int(tups[0][0])

	que = ("update Ord set TotalPrice = {totalAmt} "
	"where Ord.OrderNo = {ordno}")
	cur.execute(que.format(totalAmt=totalAmt, ordno=ordno))

	print(f"Total amount for order number {ordno} = {totalAmt}")


# 7. Get list of dishes for each order that are overdue
def overdueDishes():
	que = ("select Ord.OrderNo, Dish.DishNo "
	"from Ord join Taken_ETA on Ord.TakenTime = Taken_ETA.TakenTime "
	"join Ordered on Ordered.OrderNo = Ord.OrderNo "
	"join Dish on Dish.DishNo = Ordered.DishNo "
	"where ETA < NOW() and Dish.Status != 'Delivered'")
	cur.execute(que)
	tups = cur.fetchall()

	print("\nThe overdue dishes are:\nOrderNo | DishNo\n--------+-------")
	for t in tups:
		print(f"{t[0]:<7} | {t[1]:<6}")


# 8. Get total income for the day
def totalIncome():
	que = ("select sum(TotalPrice) from Ord")
	cur.execute(que)
	tups = cur.fetchall()

	print(f"Total income for today is {tups[0][0]}")


# -------------------------------------------- START --------------------------------------------
con = pymysql.connect(host="localhost",
	user="root",
	port=3306,
	password="harlequin",
	database="UstadHotel")

if(con.open):
	print("Connected")
else:
	print("Not Connected... Quitting application")
	exit()
cur = con.cursor()
while(1):
	print("""\n---------------------------- Menu ----------------------------
Updates: 
	1. Update Customer when a customer arrives
	2. Adjust a postponed Reservation
	3. Dish is delivered
Queries:
	4. View all reservations
	5. View all menu items
	6. Generate total for an order
	7. Get list of dishes for each order that are overdue
	8. Get total income for the day
9. Exit""")


	ch = int(input("Enter choice: "))
	if(ch == 1):
		customerArrive()
	elif(ch == 2):
		reservationpostponed()
	elif(ch == 3):
		dishdelivered()
	elif(ch == 4):
		viewreservations()
	elif(ch == 5):
		viewmenuitems()
	elif(ch == 6):
		generateTotal()
	elif(ch == 7):
		overdueDishes()
	elif(ch == 8):
		totalIncome()
	# Exit
	elif(ch == 9):
		break
	else:
		print("Invalid Choice")

	con.commit()

print("Closing connection...")
con.close()