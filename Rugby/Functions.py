import wikipedia
import webbrowser
import random
from bs4 import BeautifulSoup


greetings = ['hello', 'hi', 'hey', 'sup', 'yo', 'How are you?']


def uinput():
#asks  for input and returns as a string
    text = input(":")
    text = str(text.lower())
    return text


def rugby():
    # gives a greeting and a summary of rugby
    print(random.choice(greetings) + " Welcome to the rugby Chatbot")
    print(wikipedia.summary("rugby union", 4))
    print("""
    Ask me about teams, players etc.

    Type 'exit' to talk about another topic
    To see what you can ask me about type 'help'""")

def help():
#gives list of things user can ask about
    print("""
    You can ask me about:
        Leagues
        Teams
        Players
        Fixtures
        Results
        Tables
        Anything(gets summary of of anything)

    Type 'exit' to talk about another topic
    To see what you can ask me about type 'help'""")


def league():
#gives summary of league that user inputs
    print("What league are you interested in?")
    print(wikipedia.summary(uinput()))


def player():
#gives summary of player that user inputs
    print("What player are you interested in and what team does he play for?")
    print(wikipedia.summary(uinput()))


def teams():
#gives summary of team that user inputs
    print("What team are you interested in?")
    print(wikipedia.summary(uinput()))


def fixtures():
#takes user to page showing fixtures of input league
    print("Of which league?")
    text = uinput()
    if "pro" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/pro12/fixtures")
    elif "top" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/top-14/fixtures")
    elif "prem" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/english-premiership/fixtures")


def tables():
#takes user to page showing table of input league
    print("Of which league?")
    text = uinput()
    if "pro" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/pro12/table")
    elif "top" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/top-14/table")
    elif "prem" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/english-premiership/table")


def results():
#takes user to page showing results of input league
    print("Of which league?")
    text = uinput()
    if "pro" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/pro12/results")
    elif "top" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/top-14/results")
    elif "prem" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/english-premiership/results")


def anySummary():
#returns a summary of input
    print("get a summary of anything")
    print(wikipedia.summary(uinput()))
