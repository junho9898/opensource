import turtle
import random
import sqlite3

con = sqlite3.connect("C:/Dev/sqlite/turtleDB")
cur = con.cursor()

cur.execute("CREATE TABLE turtleTable(ID int,R float,G float,B float,sequence int,curX int,curY int)")

con.commit()
con.close()

# 변수선언

swidth,sheight,pSize,exitCount = 300,300,3,0
r,g,b,angle, dist, curX,curY =[0]*7
id = 0
count = 1

# 함수

def insertData(userid,r,g,b,seq,x,y):

    d1,d2,d3,d4,d5,d6,d7 = "","","","","","",""

    con = sqlite3.connect("C:/Dev/sqlite/turtleDB")
    cur = con.cursor()

    d1 = str(userid)
    d2 = str(r)
    d3 = str(g)
    d4 = str(b)
    d5 = str(seq)
    d6 = str(x)
    d7 = str(y)

    cur.execute("INSERT INTO turtleTable VALUES('"+ d1 +"','"+ d2 +"','"+ d3 +"','"+ d4 +"','"+ d5 +"','"+ d6 +"','"+ d7 +"')")

    con.commit()
    con.close()

def selectData():
    d1, d2, d3, d4, d5, d6, d7 = "", "", "", "", "", "", ""
    row = None

    con = sqlite3.connect("C:/Dev/sqlite/turtleDB")
    cur = con.cursor()

    cur.execute("SELECT * FROM turtleTable")

    print("선분ID     색상R         색상G          색상B        순번          X좌표          Y좌표 ")
    print("--------------------------------------------------------------------------------")

    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        d1 = row[0]
        d2 = row[1]
        d3 = row[2]
        d4 = row[3]
        d5 = row[4]
        d6 = row[5]
        d7 = row[6]

        print("%5d        %5.1f      %5.1f      %5.1f       %5d       %5d        %5d" % (d1,d2,d3,d4,d5,d6,d7))

    con.close()

def reverseTurtle():

    d1, d2, d3, d4, d5, d6, d7 = "", "", "", "", "", "", ""
    row = None

    con = sqlite3.connect("C:/Dev/sqlite/turtleDB")
    cur = con.cursor()
    cur.execute("SELECT * FROM turtleTable")

    while True:
        row = cur.fetchone()
        if row == None:
            break;

        d1 = row[0]
        d2 = row[1]
        d3 = row[2]
        d4 = row[3]
        d5 = row[4]
        d6 = row[5]
        d7 = row[6]

    for d1 in range(3, -1, 1):
        while d5 != 1:
            r = d2
            g = d3
            b = d4
            turtle.pencolor((r, g, b))
            turtle.pendown()
            turtle.goto(d6, d7)
            d5 -= 1


con.close()

# main

turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth,sheight)

con = sqlite3.connect("C:/Dev/sqlite/turtleDB")
cur = con.cursor()
cur.execute("SELECT * FROM turtleTable")

while True:
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor((r,g,b))

    angle = random.randrange(0,360)
    dist = random.randrange(1,100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()


    insertData(id+1,r,g,b,count,curX,curY)

    if(-swidth/2<=curX and curX<=swidth/2) and (-swidth/2<=curY and curY<=swidth/2):
        count += 1
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        exitCount+=1

        if exitCount>=2:
            id += 1
            count=1

    if id >= 3:
        break

selectData()
turtle.reset()

reverseTurtle()


turtle.done()




