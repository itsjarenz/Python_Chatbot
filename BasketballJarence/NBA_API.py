from Extra_Effects_For_Me import *  # importing all the code from Extra_Effects_For_Me file and running it

"""https://sportsreference.readthedocs.io/en/latest/nba.html"""  # api documentation
from sportsreference.nba.teams import Teams  # importing api
from sportsreference.nba.boxscore import Boxscores  # importing api
from sportsreference.nba.roster import Player  # importing api
from sportsreference.nba.roster import Roster  # importing api
from sportsreference.nba.schedule import Schedule  # importing api

from datetime import datetime  # importing datetime
from pprint import pprint  # importing pretty print

teams = Teams()  # Creating a class instance from the api package

"""https://docs.python.org/3/library/pprint.html"""  # pprint documentation
def prettyPrint(object):
    """Takes object such as dictionary and print it in a nice format"""
    pprint(vars(object))  # vars() returns the __dict__ attribute of object passed

def apiTeam(team):
    """Takes a team as input then will call prettyprint function passing user input as argument"""
    say("Here is some in depth information about your chosen team")
    prettyPrint(teams(team))

teamsID = {}  #  create an empty dictionary
def apiTeamAbb():
    """Iterate through all the teams created from class instance and update the dictionary with
    team name as value and their abbreviation as keys"""
    for team in teams:
        teamsID[team.abbreviation] = team.name
apiTeamAbb()

def apiGameNow():
    """Fetch all games on now on the current day and display them"""
    games_today = Boxscores(datetime.today())
    print(games_today.games)

def apiPlayerInfo(playerID):
    """Takes playerID as input and fetches all relevant information from website and prints it"""
    say("Here is your chosen player information")
    chosenPlayer = Player(playerID)  # uses playerID to create a class instance for a player
    print(chosenPlayer.name)
    print("Total career points: "+str(chosenPlayer.points))
    print("-----DATA FRAME-----")
    print(chosenPlayer.dataframe)
    print("Total games started: " + str(chosenPlayer.games_started))
    print("Total career games played: " + str(chosenPlayer.games_played))
    print("Total minutes played: " + str(chosenPlayer.points))
    print("Total career earnings: " + str(chosenPlayer.salary))
    print("Player's contract by yearly wages: " + str(chosenPlayer.contract))
    print("Player's Position: " + str(chosenPlayer.position))
    print("Player's Birth Date: " + str(chosenPlayer.birth_date))
    print("Player's Height (ft.): " + str(chosenPlayer.height))
    print("Player's Weight (lbs): " + str(chosenPlayer.weight))
    print("Player's Nationality: " + str(chosenPlayer.nationality))

def apiPlayerIDs(chosenTeam):
    """Takes a team as input and print all players in the team their name and their playerID"""
    say("Gathering relevant data, this may take a while. Please wait.")
    team = Roster(chosenTeam)  # uses chosenTeam to create a class instance for a roster of a team
    say("Here is the list of players and their ID number for your specified team")
    for player in team.players:  # Iterate through every player in team
        print(player.name+" : "+player.player_id)

def apiChooseTeam():
    """Menu for the user to choose a team or enter something else to determine what the program will do"""
    while True:  # Keep iterating until stop condition is met
        say("Enter team abbreviation")
        say("Enter z to view all teams abbreviations")
        say("Enter exit to exit")
        choice = input(">>>")
        if choice == "z":
            pprint(teamsID)  # Call pprint module to print out teamsID(dictionary) as the argument in nice format
        elif choice == "exit":
            break  # End the loop
        else:
            if teamsID.get(choice):  # Check if choice is in the dictionary first
                apiPlayerIDs(choice)  # Call apiPlayerIDs function and passing choice as argument
            else:
                say("That abbreviation does not exist")

def choosePlayer():
    """Menu for the user to choose a player or enter something else to determine what the program will do"""
    while True:  # Keep iterating until stop condition is met
        say("What player would you like to know about? Enter their ID")
        say("Enter z to find out a players ID")
        say("Enter exit to exit")
        choice = input(">>>")
        if choice == "z":
            apiChooseTeam()  # Call apiChooseTeam function
        elif choice == "exit":
            break  # End the loop
        else:
            try:  # Try this code first, if works continue
                apiPlayerInfo(choice)  # Call apiPlayerInfo function passing choice as argument
            except:  # If code does not work then do this
                say("That player ID does not exist")

def calculateOppScore(game):
    """Takes game as input, works out the opposition's total points and outputs the total amount of points"""
    onePointers = game.opp_free_throws
    twoPointers = game.opp_field_goals*2
    threePointers = game.opp_three_point_field_goals
    total = onePointers + twoPointers + threePointers
    return total

def apiGamesInfo(team):
    """Takes team as input and will fetch teams recent game history and prints it"""
    say("Here is your teams recent game history")
    teamSchedule = Schedule(team)  # uses team to create a class instance for a schedule of a team game history
    for game in teamSchedule:  # For every game played, print information about each game
        print(game.date + " : " + game.result)
        print("========= " + team + " vs " + game.opponent_abbr + " ================")
        oppPoints = calculateOppScore(game)  # Call function and assign return value to variable
        print(str(game.points_scored) + "\t POINTS \t\t" + str(oppPoints))
        print(str(game.blocks) + "\t BLOCKS \t\t" + str(game.opp_blocks))
        print(str(game.free_throws) + "\t FREE THROWS \t\t" + str(game.opp_free_throws))
        print(str(game.field_goals) + "\t TWO POINTERS \t\t" + str(game.opp_field_goals))
        print(str(game.three_point_field_goals) + "\t THREE POINTERS \t" + str(game.opp_three_point_field_goals))
        print(str(game.steals) + "\t STEALS \t\t" + str(game.opp_steals))
        print(str(game.turnovers) + "\t TURNOVERS \t\t" + str(game.opp_turnovers))
        print("="*37)  # prints 37 equal signs
        print()

def apiPickATeam():
    """Ask the user to input a team abbreviation and then output the user's input if it is valid"""
    say("What team would you want to view?")
    say("Enter the teams abbreviation to proceed")
    say("Enter z to view all the teams abbreviations or exit to exit")
    while True:
        userInput = input(">>>")
        if userInput == "exit":
            break
        elif userInput == "z":
            pprint(teamsID)
        else:
            if teamsID.get(userInput):  # Check if userInput is in the dictionary first
                return userInput
            else:
                say("That abbreviation does not exist")

def apiMenuDisplay():
    """Prints a menu of things the user can do"""
    print("""
    1. See what games are on today?
    2. Find out about a team's recent game history?
    3. Find out more about a certain player?
    4. Find out more about a certain team?
    *Enter exit to exit
    *Enter z to this view menu again
    """)

def apiMenu():
    """Menu for the user to choose a player or enter something else to determine what the program will do"""
    apiMenuDisplay()
    say("What would you like to know?")
    say("Enter a number to proceed or exit to exit")
    while True:
        userInput = input(">>>")
        if userInput == "exit":
            break
        elif userInput == "z":
            apiMenuDisplay()
        elif userInput == "1":
            apiGameNow()
        elif userInput == "2":
            teamChoice = apiPickATeam()  # Call function and assign return value to variable
            if teamChoice:  # Check if teamChoice is not an empty string
                apiGamesInfo(teamChoice)
                apiMenuDisplay()
            else:  # What happens if teamChoice is an empty string
                apiMenuDisplay()
        elif userInput == "3":
            choosePlayer()
            apiMenuDisplay()
        elif userInput == "4":
            teamChoice = apiPickATeam()
            if teamChoice:
                apiTeam(teamChoice)
                apiMenuDisplay()
            else:
                apiMenuDisplay()
        else:
            say("I did not understand what you said, rephrase or say something else.")