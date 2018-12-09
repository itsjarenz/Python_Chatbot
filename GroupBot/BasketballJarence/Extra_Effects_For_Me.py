import pyttsx3  # https://pyttsx3.readthedocs.io/en/latest/ for the TextToSpeech Effect
import sys  # importing system
from time import sleep  # importing time
import wikipedia  # will allow the bot to search on wikipedia
import subprocess  # importing subprocess for the program to speak text.

"""https://stackoverflow.com/questions/22139394/python-text-to-speech-with-that-can-read-variables-contents"""
# say function reference link
def say(text):
    """Takes string as an input and will print string and turn it into speech too"""
    print(text)
    subprocess.call('say ' + text, shell=True)

"""Ibrahim Waheed code below"""
def tts_typoEffect(text):
    # the below is the fancy text typo effect
    for char in text:#
        sleep(0.01)#for testing put 0.01
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    # below is the tts= test to speech effect
    speech_engine = pyttsx3.init()#invoking the pyttsx engine
    voice = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voice[32].id)
    speech_engine.say(text)# passing the parameter text ( which would be used on the various chatbots convos)
    speech_engine.runAndWait()

#https://wikipedia.readthedocs.io/en/latest/code.html THE BEST API ON THE PLANET
def WikiSearchSummary(text):
    '''Will allow the bot to grab data from wikipedia and say it to the user!'''
    tts_typoEffect(wikipedia.summary(text))