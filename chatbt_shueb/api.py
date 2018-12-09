import requests
import wikipedia 
from extra_effects_by_Ibrahim import *
def todayMatches():
    response = requests.get('https://cricapi.com/api/matches?apikey=nqBj0KWp0tSRa6sPq5Bc348ZfF92')
    info = response.json()
    print(info)

def wiki():
     name = str(input("Please Write player's name here \n")).upper()
     player_search = wikipedia.search(name)
     info = wikipedia.summary(name)
     print(info)
     
  