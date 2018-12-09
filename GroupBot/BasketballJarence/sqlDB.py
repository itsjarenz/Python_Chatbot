from BasketballJarence.Extra_Effects_For_Me import *   # importing all the code from Extra_Effects_For_Me file and running it
import sqlite3  # importing sqlite3 package

def connectionToDatabase(sqlCommand):
    """Takes an sql command and executes the command to a database"""
    connection = sqlite3.connect('nba.db')  # Open database file and connect to it
    cursor = connection.cursor()  # Create cursor object which will execute the sql command
    cursor.execute(sqlCommand)  # Execute sql command
    connection.commit()  # Write and save changes to database
    connection.close()  # Close database file

sqlCommandCreateTeamTable ="""CREATE TABLE tblTeams
(
teamID integer NOT NULL,
teamName text NOT NULL,
primary key (teamID)
)"""  # sql command to create table in database

sqlCommandCreatePlayerTable ="""CREATE TABLE tblPlayers
(
playerID integer NOT NULL,
playerName text NOT NULL,
teamName text NOT NULL,
shirtNum integer NOT NULL,
position text NOT NULL,
height integer NOT NULL,
weight integer NOT NULL,
primary key (playerID)
)"""  # sql command to create table in database

##connectionToDatabase(sqlCommandCreateTeamTable)
##connectionToDatabase(sqlCommandCreatePlayerTable)

def newPlayer():
    """Will create a new record for a new player in the database file using user input to create new record"""
    conn = sqlite3.connect("nba.db")
    cursor = conn.cursor()
    newRec = []  # Create empty list
    playerName = input ("Enter name of player: ").lower()
    teamName = input ("Enter team player plays for: ").lower()
    shirtNum = input ("Enter player shirt number: ")
    position = input ("Enter player position: ").lower()
    height = input ("Enter player height: ")
    weight = input ("Enter player weight: ")
    newRec.append(playerName)  # Append user inputs into the empty list
    newRec.append(teamName)
    newRec.append(shirtNum)
    newRec.append(position)
    newRec.append(height)
    newRec.append(weight)
    cursor.execute("INSERT INTO tblCars VALUES (NULL,?,?,?,?,?,?)",newRec)  # Execute command with input values
    conn.commit()
    newRec = []  # Empty the list
    conn.close()

def ViewTeamTableForm(sql):
    """Takes sql command as input and prints database table in nice format"""
    connection = sqlite3.connect("nba.db")
    cursor = connection.cursor()
    print("%-10s %-20s" %("TeamID","Name\n"))  # Determines how much space each column will be
    for row in cursor.execute(sql):
        teamID, teamName = row  # Assigns column name in as header for the table and prints what is in each row
        print ("%-10s %-20s" %(row))

def ViewPlayersTableForm(sql):
    """Takes sql command as input and prints database table in nice format"""
    connection = sqlite3.connect("nba.db")
    cursor = connection.cursor()
    print("%-10s %-20s %-25s %-15s %-15s %-10s %-10s" \
          %("PlayerID","Name","Team","Number","Position",\
            "Height(ft)","Weight(lbs)\n"))
    for row in cursor.execute(sql):
        playerID, playerName, teamName, shirtNum, position, \
        height, weight = row
        print ("%-10s %-20s %-25s %-15s %-15s %-10s %-10s" %(row))

def ViewAllTeams(sql):
    """Takes sql command as input and prints all teams in the database table"""
    connection = sqlite3.connect("nba.db")
    cur = connection.execute(sql)
    cur = cur.fetchall()
    for row in cur:
        print(row[1])  # Only print the team name not the teamID

def ViewPlayer(sql):
    """Takes sql command as input and prints player record in a nice format"""
    connection = sqlite3.connect("nba.db")
    cur = connection.execute(sql)
    for row in cur:
        print("---PROFILE---")
        print("* Name: ", row[1])
        print("* Team: ", row[2])
        print("* Shirt Number: ", row[3])
        print("* Position: ", row[4])
        print("* Height(ft): ", row[5])
        print("* Weight(lbs): ", row[6])
    print()

def OneTeamView(sql):
    """Takes sql command as input and prints one team in the database table"""
    connection = sqlite3.connect("nba.db")
    cur = connection.execute(sql)
    for row in cur:
        say(row[1])

def OnePlayerView(sql):
    """Takes sql command as input and prints one player in the database table"""
    connection = sqlite3.connect("nba.db")
    cur = connection.execute(sql)
    for row in cur:
        say(row[1])

def dbCheck(sql):
    """Takes sql command as input and and will check if certain information is in the database or not
    Then output is boolean of true or false"""
    success = 0
    while success == 0:
        with sqlite3.connect("nba.db") as db:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()  # Fetch all data in the database based of sql command
            if results:  # If results is not none then return True else, return False
                return True
            else:
                return False