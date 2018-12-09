from fancy_tools_effects import *
from BoxingIbrahimWaheed.BoxingFunctions import *
from BoxingIbrahimWaheed.UFCFunctions import *
import webbrowser
import SportTalkBot as SportBot

# import the fuction text to speech
# allows users to chat with guru kate
#Note the chatbot is rule base , if questions are anwsered incorrently then system will prompt you to repeat process!
#did not want to do a rule base i've struggle with the tensorflow AI bot ( see tensorflow AI failed)

def TellAllMaleBoxersNames():
    WikiLinksBoxer()
def TellAllFemaleBoxerNames():
    WikiLinksFeMaleBoxer()

def SearchBoxer(text):
    # lstrip remove the @ symbol
    WikiSearch(text)  # Only problem is that the search can be about anything...



def BoxerConvo(keep):
    SearchBoxer(keep)
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
    # Not done due to time !
    pass

# Create a new menu function , as i added various changes to the def main#
def main():
    # main just display text , as the storedata is doing the if statements!

    '''The menu system that allows user to interact with chatbot kate'''
    print ('''
    
    Welcome to the all-inclusive, Combat Sport Talk bot. 
    I am chatbot Kate, I can search for any boxer, MMA, wrestlers.
    To Chat with me type Main
    I can also provide list of each UFC fighters, Boxers 
    Other task i can do is:
        Tell you live combat sport news 
        Open website fighters articles
        Search for boxer with @Boxer name
        Search for UFC with !UFC name
        
    Type 5 or Back to go to the main menu
        
    ''')
    bg_tts("say hi to start")


    News= ["give news", "play sports news" , "tell me the news" , "play news"]
    userInput=str(input(">>>>"))
    if userInput[0].lower() == "@":
        clean= userInput.lstrip("@")
        print(clean)
        BoxerConvo(clean)
    elif userInput.lower() == "5" or userInput.lower() =="back":
        SportBot.SportTalk()

    elif userInput in News:
       PlaySportRadio()









