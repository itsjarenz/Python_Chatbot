# This chatbot is for cricket information
#key-nqBj0KWp0tSRa6sPq5Bc348ZfF92
import random 
import time
from api import *
from extra_effects_by_IbrahimB import *


grettings = ["Hi", "Hey", "Hello", "Hiya"]
print (random.choice(grettings))
time.sleep(1.5)
print("My name is Cricbot")
time.sleep(1.5)
print("I can help you with crickter's information, Live score")
time.sleep(2.5)

print('''
              A- Player information
              B- Today's matches
              D- Latest news''')

def chatbot_main():
    user_choice=str(input("Please write your option here \n")).upper()
    if user_choice == "A" or user_choice == "player information": 
        wiki()
    elif user_choice  == "B" or user_choice == "Today's matches":
        todayMatches()
    #elif user_choice == "D" or user_choice == "Latest news":
       # c = cricbuzz()
       # matches = c.matches()
        #print (json.dumps(parsed,indent=4))
chatbot_main()