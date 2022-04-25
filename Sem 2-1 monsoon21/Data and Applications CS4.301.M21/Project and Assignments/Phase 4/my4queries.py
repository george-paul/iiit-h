import pymysql
from tabulate import tabulate

con = pymysql.connect(host="localhost",
                              user="root",
                              port=3306,
                              password="jimbajumba",
                              database='UstadHotel')

if(con.open):
    print("Connected")
else:
    print("Not Connected")

cur = con.cursor()

def viewmenuitems():
    que = "select * from Menu_Item"
    cur.execute(que)
    tups = cur.fetchall()
    # print("tups:",type(tups)) tups is a tuple of tuples
    print(tabulate(tups,headers=["Menuitem","Cost"]))
    # for r in tups:
    #     # print("r:",type(r))   r is a tuple
    #     print(r[0].strip("'"),"-",r[1])

def viewreservations():
    que = "select * from Reservation"
    cur.execute(que)
    tups = cur.fetchall()
    print(tabulate(tups,headers=["PhoneNo","Name","Start_DateTime","TableNum"]))
    # for r in tups:
    #     print(r[0].strip("'"),",",r[1].strip("'"),",",r[2],",",r[3])


def dishdelivered():
    DishNo=input("Enter Dishnumber delivered: ")
    TableNum=input("Enter tablenumber: ")
    que="Update Dish set Status = 'Delivered' where DishNo={Dish} and TableNum={TableN}"
    # que = ("Update Dish"
    # "set Status = 'Delivered'"
    # "where DishNo={DishNo} and TableNum={TableNum}")
    cur.execute(que.format(Dish=DishNo,TableN=TableNum))
    # print("Updated Dish:\n")
    que2 = "select * from Dish where TableNum={TableN}"
    cur.execute(que2.format(TableN=TableNum))
    tups = cur.fetchall()
    if(len(tups)==0):
        print("Error: Dish already delivered/ doesnt exist")
    else:
        print("Changed dish status as :")
        print(tabulate(tups,headers=["DishNo","TableNum","ItemName","Status"]))
        # for r in tups:
        #     print(r[0],",",r[1],",",r[2].strip("'"),r[3].strip("'"))

def reservationpostponed():
    resphoneno=input("Enter phone number of the reserved person: ")
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


print("Menuitems:\n")
viewmenuitems()

print("Reservations:\n")
viewreservations()

print("Postponing reservation\n")
reservationpostponed()

print("dishdelivered\n")
dishdelivered()

# que = "select * from INVINDEX"
# cur.execute(que)
# tups = cur.fetchall()

# for r in tups:
#     print(r)

# con.commit()
con.close()
