from fancy_tools_effects import *
from BoxingFunctions import *
from UFCFunctions import *
import webbrowser

#import TextToCLIWidget as tk
# import the fuction text to speech
# allows users to chat with guru kate
#Note the chatbot is rule base , if questions are anwsered incorrently then system will prompt you to repeat process!
#did not want to do a rule base i've struggle with the tensorflow AI bot ( see tensorflow AI failed)

def TellAllMaleBoxersNames():
    WikiLinksBoxer()
    print("To go back type b")
    userInput = input(">>>>")
    if userInput.lower() == "b":
        main()
def TellAllFemaleBoxerNames():
    WikiLinksFeMaleBoxer()
    print("To go back type b")
    userInput = input(">>>>")
    if userInput.lower() == "b":
        main()

def SearchBoxer(text):
    # lstrip remove the @ symbol
    WikiSearch(text)  # Only problem is that the search can be about anything...



def BoxerConvo(keep):
    tts_Effect("do you want me to search on google for this boxer")
    userInput=input("type yes or no")
    if userInput.lower() in "yes":
        searchGoogle = "https://www.google.com/search?q=" + keep +" boxer"
        webbrowser.open(searchGoogle, new=2)
        print("To go back type b")
        userInput=input(">>>>")
        if userInput.lower() == "b":
            main()
    elif userInput.lower() =="no":
        main()



def MMAConvo(keep):
   pass


def wrestlersConvo(keep):
    pass

# Create a new menu function , as i added various changes to the def main#
def main():
    # main just display text , as the storedata is doing the if statements!

    '''The menu system that allows user to interact with chatbot kate'''
    print ('''
    
    Welcome to the all-inclusive, Combat Sport Talk bot. 
    I am chatbot Kate, I can search for any boxer, MMA, wrestlers.
    To Chat with me type Main
    I can also provide list of each UFC fighters, Boxers and wrestler s(from the WWE).
    Other task i can do is:
        Tell you live combat sport news 
        Open website fighters articles
        Search for boxer with @Boxer name
        To Give All male boxer name or female type ListMale/ListFemale
        
    ''')



    News= ["give news", "play sports news" , "tell me the news" , "play news" , "play radio"]
    userInput=str(input(">>>>"))
    if userInput[0].lower() == "@":
        clean= userInput.lstrip("@")
        print(clean)
        SearchBoxer(clean)
        sleep(2)
        BoxerConvo(clean)
    elif userInput in News:
       PlaySportRadio("NONE")
       print("To stop radio type STOP")
       userInput = str(input(">>>>"))
       if userInput.lower() == "stop":
           PlaySportRadio("stop")
    elif userInput.lower() == "listmale":
        TellAllMaleBoxersNames()
    elif userInput.lower() == "listfemale":
        TellAllFemaleBoxerNames()

# replace def main wth python way of main

if __name__ == '__main__':
   main()  # run the chatbot interface




