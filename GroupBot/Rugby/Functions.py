import wikipedia
import webbrowser
import random
from bs4 import BeautifulSoup


greetings = ['hello', 'hi', 'hey', 'sup', 'yo', 'How are you?']


def uinput():
    text = input(":")
    text = str(text.lower())
    return text


def rugby():
    print(random.choice(greetings) + " Welcome to the rugby Chatbot")
    print(wikipedia.summary("rugby union", 4))
    print("""
    Ask me about teams, players etc.
    Type 'exit' to talk about another topic
    To see what you can ask me about type 'help'""")

def help():
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
    print("What league are you interested in?")
    print(wikipedia.summary(uinput()))


def player():
    print("What player are you interested in and what team does he play for?")
    print(wikipedia.summary(uinput()))


def teams():
    print("What team are you interested in?")
    print(wikipedia.summary(uinput()))


def fixtures():
    print("Of which league?")
    text = uinput()
    if "pro" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/pro12/fixtures")
    elif "top" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/top-14/fixtures")
    elif "prem" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/english-premiership/fixtures")


def tables():
    print("Of which league?")
    text = uinput()
    if "pro" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/pro12/table")
    elif "top" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/top-14/table")
    elif "prem" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/english-premiership/table")


def results():
    print("Of which league?")
    text = uinput()
    if "pro" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/pro12/results")
    elif "top" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/top-14/results")
    elif "prem" in text:
        webbrowser.open("https://www.bbc.co.uk/sport/rugby-union/english-premiership/results")


def anySummary():
    print("get a summary of anything")
    print(wikipedia.summary(uinput()))
