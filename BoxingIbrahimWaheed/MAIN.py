
#from gwyn.py import *
from fancy_tools_effects import tts_typoEffect , bg_tts
#from joao.py import *
#from Jarence.py import *
#from shueb.py import *

###
#Main ChatBot Project Python File
###

#The main file will be a menu system of some sort , that will allow users to interactive and talk to different chatbots

def main():

    bg_tts("Talk to Guru Kate about sports")

    tts_typoEffect("Please choose Which sport you want to talk about")
    tts_typoEffect("Boxing Type 1")
    tts_typoEffect("Rugby Type 2 ")
    userType = input("Talk to Guru Kate about sports").lower()
    if userType=="combat sport":
        print("function")
    elif userType=="rugby":
        print("function")
    elif userType=="cricket":
        print("function")
    elif userType == "swimming":
        print("function")

main()
