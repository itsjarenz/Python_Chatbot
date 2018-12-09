import pyttsx3 
import wikipedia 
import sys 
import time
def tts_typoEffect(name):
    # the below is the fancy text typo effect
    for char in text:#
        sleep(0.10)#for testing put 0.01
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    # below is the tts= test to speech effect
    speech_engine = pyttsx3.init()#invoking the pyttsx engine
    voice = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voice[2].id)
    speech_engine.say(text)# passing the parameter text ( which would be used on the various chatbots convos)
    speech_engine.runAndWait()


def bg_tts(text):
    '''To play sound but no typo effect'''
    speech_engine = pyttsx3.init()  # invoking the pyttsx engine
    voice = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voice[2].id)
    speech_engine.say(text)  # passing the parameter text ( which would be used on the various chatbot)
    speech_engine.runAndWait()

# fix for the TypeError: bg_tts() takes 1 positional argument but 2 were given
#https://wikipedia.readthedocs.io/en/latest/code.html THE BEST API ON THE PLANET
def WikiSearch(text):
    '''Will allow the bot to grab data from wikipedia and say it to the user!'''
    try:
     tts_typoEffect(wikipedia.summary(text,sentences=1))
    except wikipedia.DisambiguationError:
        tts_typoEffect("Not found !")
    #might have to create a force string for individual topic



### Any more function effect will be below


def PlaySportRadio():
    '''This will play sport radio'''

    # the above link really helped me understand how the mediaplay works!

    radio = vlc.MediaPlayer('talksport2.m3u')# This used the vlc mediaplayer -
    #mp3 that is listed
    while True:
        radio.play()