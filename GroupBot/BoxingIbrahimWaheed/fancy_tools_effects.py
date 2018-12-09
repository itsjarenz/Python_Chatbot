#by Ibrahim waheed all of the module and any code that was not my have been commented
import pyttsx3 #https://pyttsx3.readthedocs.io/en/latest/ for the TextToSpeech Effect
# maybe instead of pyttsx3 could have use gttsx a google cloud base text to speech'
# google one require internet! and API key
# the below import is for the fancy typo effect!
import wikipedia # will allow the bot to search on wikipedia
import sys #importing system
import  webbrowser # for text to speech search google
from time import sleep
# importing audio module will need for text to speech week4
import vlc
#import TextToCLIWidget as gui



# The text to speech module is using a third party module from Pyttx3
# I just created a function which can be used by the team
# The problem with the pyttsx3 is that it relies on the system native text to speech voices
# Therefore voices will be different on different os -
# This function is good for cmd/GUI desktop base apps
# It might not work with facebook/twitter API sevices
# All comments must be transfer to git repo
def tts_Effect(text):
    '''To play sound but and have a typo effect'''
    for char in text:  #
        sleep(0.001)  # for testing put 0.01
        sys.stdout.write(char) # will print each char one by one
        sys.stdout.flush() # allows the char to be print one by one

    print("\n")
    # below is the tts= test to speech effect
    speech_engine = pyttsx3.init()  # invoking the pyttsx engine
    voice = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voice[2].id)
    speech_engine.say(text)  # passing the parameter text ( which would be used on the various chatbots convos)
    speech_engine.runAndWait()



def bg_tts(text):
    '''To play sound but no typo effect'''

    speech_engine = pyttsx3.init()  # invoking the pyttsx engine
    voice = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voice[2].id)
    speech_engine.say(text)  # passing the parameter text ( which would be used on the various chatbot)
    speech_engine.setProperty('rate', 300)
    sleep(4)
    speech_engine.runAndWait()

# fix for the TypeError: bg_tts() takes 1 positional argument but 2 were given
#https://wikipedia.readthedocs.io/en/latest/code.html , This is a simple web api
# I really liked this API , as it was really easy to create functions.
#
def WikiSearch(text):
    '''Will allow the bot to grab data from wikipedia and say it to the user!'''
    try:
        data = wikipedia.summary(text, sentences=1)
        f = open("hold.txt","w", encoding="utf-8") # This fix is done as the problem were occuring on some string data
        f.write(data)
        f.close()

    except wikipedia.DisambiguationError:
        tts_Effect("Not found !")
    #might have to create a force string for individual topic



### Any more function effect will be below


def PlaySportRadio():
    '''This will play sport radio'''

    # this variable is my own , it will send the link to the radio
    talkSportLinK = 'http://radio.talksport.com/stream2'

    # below the code is from  https://linuxconfig.org/how-to-play-audio-with-vlc-in-python -
    # and the https://wiki.videolan.org/LibVLC/
    # The only problem with this code is that you cannot stop the radio
    # i've tried various solutions , the only one i can think of it using a loop and making it sleep
    # however that does not solve the solution , but give an illusion that the radio is stopped.

    # define VLC instance , basically with invoke the vlc
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

    # Define VLC player
    player = instance.media_player_new()

    # Define VLC media
    media = instance.media_new(talkSportLinK)

    # Set player media
    player.set_media(media)

    # Play the media
    player.play()








