# This chatbot is for cricket information
#key-nqBj0KWp0tSRa6sPq5Bc348ZfF92
import random 
import time
import wikipedia 
import requests 

def CricketMain():
    heading= 'CRICBOT'
    heading = heading.center(50) #https://www.tutorialspoint.com/python/string_center.htm
    print("\033[1;32;40m  \n"+ heading)#code copied from:- http://ozzmaker.com/add-colour-to-text-in-python/
    grettings = ["Hi", "Hey", "Hello", "Hiya"]
    print (random.choice(grettings))
    time.sleep(1.5)
    print("My name is Cricbot")
    time.sleep(1.5)
    print("I can help you with crickter's information, Live score")
    time.sleep(2.5)

    print('''
                  A - Player information
                  B - Today's matches
                  C - Match calander 
                  D - Cricket news
                  ''')

    while True:
        time.sleep(2.5)
        user_choice=str(input("Write your option here \n")).upper()
        if user_choice == "A" or user_choice == "player information":

            name = str(input("Please Write player's name here \n")).upper()
            player_search = wikipedia.search(name) #https://wikipedia.readthedocs.io/en/latest/code.html#module-wikipedia
            info = wikipedia.summary(name)
            print(info)
            # i used cricket apis
        elif user_choice  == "B" or user_choice == "Today's matches":
            info = requests.get('https://cricapi.com/api/matches?apikey=nqBj0KWp0tSRa6sPq5Bc348ZfF92').json()
            
            for data in info['matches']:
                print(data['team-1'])
                print("vs")
                print(data['team-2'])
                print(data['date'])
                print("\n")
           
            # copied from: https://www.cricapi.com/member-test.aspx
        elif user_choice  == "C" or user_choice == "Match Calander":
            info = requests.get('https://cricapi.com/api/matchCalendar?apikey=nqBj0KWp0tSRa6sPq5Bc348ZfF92').json()

            for match in info['data']:
                print(match['name'])
                print(match['date'])
                print('\n')
            
            # copied from: https://www.cricapi.com/member-test.aspx
        elif user_choice  == "D" or user_choice == "Cricket news":
            info = requests.get('https://newsapi.org/v2/top-headlines?sources=espn-cric-info&apiKey=d6291b918cd845e6a099bd6b5b91abe5').json()
            for data in info['articles']:
                print('Title \n' + data['title'])
                print('\n')
                print(data['description'])
                print('\n')
        # copied from: https://www.cricapi.com/member-test.aspx
CricketMain()
