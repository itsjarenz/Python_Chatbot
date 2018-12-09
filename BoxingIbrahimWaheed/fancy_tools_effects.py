#by Ibrahim waheed
import pyttsx3 #https://pyttsx3.readthedocs.io/en/latest/ for the TextToSpeech Effect
# maybe instead of pyttsx3 could have use gttsx a google cloud base text to speech'
# google one require internet!
# the below import is for the fancy typo effect!
import wikipedia # will allow the bot to search on wikipedia
import sys #importing system
import  webbrowser # for text to speech search google
from time import sleep
# Below import is for the news api
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
    # the below is the fancy text typo effect
    for char in text:  #
        sleep(0.001)  # for testing put 0.01
        sys.stdout.write(char)
        sys.stdout.flush()
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
#https://wikipedia.readthedocs.io/en/latest/code.html THE BEST API ON THE PLANET
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


def PlaySportRadio(keep):
    '''This will play sport radio'''

    talkSportLinK = 'http://radio.talksport.com/stream2'
    quickFix='' #a quick fix
    # define VLC instance , basically with invoke the vlc
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

    # Define VLC player
    player = instance.media_player_new()

    # Define VLC media
    media = instance.media_new(talkSportLinK)

    # Set player media
    player.set_media(media)
    # Play the media
    if keep == "stop":
        player.pause()
    else:
        player.play()








#https://linuxconfig.org/how-to-play-audio-with-vlc-in-python
#https://wiki.videolan.org/LibVLC/






