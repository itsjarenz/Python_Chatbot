from NBA_API import *  # importing all the code from NBA_API file and running it
from Extra_Effects_For_Me import *  # importing all the code from Extra_Effects_For_Me file and running it
from sqlDB import *  # importing all the code from sqlDB file and running it
from random import *  # import the random module
import random  # import the random module
import time  # import the time module

"""
Lists containing possible user inputs and potential corresponding program outputs
"""
greetings = ['hello', 'hi', 'hey', 'sup', 'yo', 'How YOU doin']

tQuestions = ["who is your favourite team?", "which is the best team?",
              "which is the worst team?", "which team will be champions?"]

pQuestions = ["who is your favourite player?", "who is your least favourite player?",
              "who is the tallest player?", "who is the heaviest player?"]

dbQuestions = ["#Enter any team name in the league to find out more about them eg.'!miami heat'",
               "#Enter any player name in the league to find out more about them eg.'!LeBron James'",
               "Search all players who are height ___ (ft)", "Search all players who are weight ___ (lbs)",
               "Search all players who play for ___ (team)", "Search all players who play as ___ (position)",
               "Search all players who wear ___ (number)"]

print()
say("Welcome to NBA Basketball Chat-Bot!")
time.sleep(1)  # program stops for a second

def menu():
    """Prints the main menu for the program"""
    print("""
    ---------------------------------------------------------------------------------------------------
    |1. Talk about NBA Players                                        *Enter 'exit' to exit           |
    |2. Talk about NBA Teams and NBA itself                           *Enter 'help' for commands      |
    |3. Search through the NBA database                               *Enter 'menu' to view this menu |
    |4. Web search information about NBA using an API                                                 |
    |                                                                                                 |
    |Or just say hi! :)                                                                               |
    ---------------------------------------------------------------------------------------------------
    """)

def NBATeamMenu():
    """Menu for the user to choose a player or enter something else to determine what the program will do"""
    say("What would you like to know?")
    while True:  # keep looping until stop condition met
        userInput=input(">>>")
        ex=userInput[0].find("!")  # Check if user input starts with and exclamation mark
        if userInput =='exit':
            break  # End loop
        else:
            if ex:  # If user input does not start with exclamation mark then do this
                if userInput in tQuestions:  # check if user input matches question in tQuestion list
                    num = randint(1, 30)  # generate a random number
                    OneTeamView("SELECT * FROM tblTeams WHERE teamID = " + str(num) + "")  # Call function OneTeamView
                else:
                    say("I did not understand what you said, rephrase or say something else.")
                    print()
            else:  # If user input starts with exclamation mark then do this
                WikiSearchSummary(userInput[1:])  # Call function WikiSearchSummary without exclamation mark

def NBAPlayerMenu():
    """Menu for the user to choose a player or enter something else to determine what the program will do"""
    say("What would you like to know?")
    while True:
        userInput = input(">>>")
        ex = userInput[0].find("!")
        if userInput == 'exit':
            break
        else:
            if ex:
                if userInput in pQuestions:  # check if user input matches question in pQuestion list
                    num = randint(1, 493)
                    OnePlayerView("SELECT * FROM tblPlayers WHERE playerID = " + str(num) + "")
                else:
                    say("I did not understand what you said, rephrase or say something else.")
                    print()
            else:
                KnowAboutPlayer(userInput[1:])  # Call function KnowAboutPlayer without exclamation mark

def dbQueryMenu():
    """Prints a menu of things the user can do"""
    print("""
    1. View all of the teams in the NBA
    2. View all of the players in the NBA
    3. Search all players who are height ___ (ft)
    4. Search all players who are weight ___ (lbs)
    5. Search all players who play for ___ (team)
    6. Search all players who play as ___ (position)
    7. Search all players who wear ___ (number)
    
    *Enter a number to proceed, or exit.
    """)

def dbMenu():
    """Menu for the user to choose a player or enter something else to determine what the program will do"""
    dbQueryMenu()  # Call function to print menu
    say("What would you like to know?")
    while True:
        userChoice = input(">>>")
        if userChoice == 'exit':
            break
        elif userChoice == '1':
            ViewAllTeams("SELECT * FROM tblTeams")
        elif userChoice == '2':
            ViewPlayersTableForm("SELECT * FROM tblPlayers")
        elif userChoice == '3':
            print("Enter height(ft.)")
            userInput = input(">>>")
            sql="SELECT * FROM tblPlayers WHERE height = '" + userInput + "'"  # Create sql command
            valid=dbCheck(sql)  # call function to check if it is valid in database passing sql command as argument
            if valid:
                ViewPlayersTableForm(sql)  # if valid, then call function passing sql command as argument
            else:
                say("Could not find any matching results.")
        elif userChoice == '4':
            print("Enter weight(lbs.)")
            userInput = input(">>>")
            sql = "SELECT * FROM tblPlayers WHERE weight = '" + userInput + "'"
            valid = dbCheck(sql)
            if valid:
                ViewPlayersTableForm(sql)
            else:
                say("Could not find any matching results.")
        elif userChoice == '5':
            print("Enter team")
            userInput = input(">>>")
            sql = "SELECT * FROM tblPlayers WHERE teamName = '" + userInput + "'"
            valid = dbCheck(sql)
            if valid:
                ViewPlayersTableForm(sql)
            else:
                say("Could not find any matching results.")
        elif userChoice == '6':
            print("Enter position")
            userInput = input(">>>")
            sql = "SELECT * FROM tblPlayers WHERE position = '" + userInput + "'"
            valid = dbCheck(sql)
            if valid:
                ViewPlayersTableForm(sql)
            else:
                say("Could not find any matching results.")
        elif userChoice == '7':
            print("Enter number")
            userInput = input(">>>")
            sql = "SELECT * FROM tblPlayers WHERE shirtNum = '" + userInput + "'"
            valid = dbCheck(sql)
            if valid:
                ViewPlayersTableForm(sql)
            else:
                say("Could not find any matching results.")
        else:
            say("I did not understand what you said, rephrase or say something else.")
            print()

def ViewCommands():
    """Menu for the user to choose a player or enter something else to determine what the program will do"""
    print()
    print("---Team Questions---")
    for x in tQuestions:  # Go though entire list and print each element from the list
        print(x)
    print()
    print("---Player Questions---")
    for y in pQuestions:
        print(y)
    print()
    print("---Extra Other Questions---")
    for z in dbQuestions:
        print(z)

def KnowAboutPlayer(bPlayer):
    """Takes a player as input and searches player in database and wikipedia"""
    bPlayer=bPlayer.lower()  # change the parameter to lowercase
    ViewPlayer("SELECT * FROM tblPlayers WHERE playerName = '"+bPlayer+"'")
    WikiSearchSummary(bPlayer)

def main():
    """Menu for the user to choose a player or enter something else to determine what the program will do"""
    menu()  # call function to display menu
    while True:
        userInput = input(">>>")
        userInput = userInput.lower()
        if userInput == "exit":
            break
        elif userInput == "help":
            say("Here are some commands you can ask me")
            ViewCommands()
        elif userInput == "menu":
            menu()
        elif userInput in greetings:  # Checks if user input is in list
            random_greeting = random.choice(greetings)  # Pick a random response from list
            say(random_greeting)
        elif userInput == "1":
            NBAPlayerMenu()
            menu()
        elif userInput == "2":
            NBATeamMenu()
            menu()
        elif userInput == "3":
            dbMenu()
            menu()
        elif userInput == "4":
            apiMenu()
            menu()
        else:
            say("I did not understand what you said, rephrase or say something else.")
            say("Enter 'help' for commands")
            print()

main()