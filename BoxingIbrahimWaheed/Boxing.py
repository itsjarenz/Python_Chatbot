from fancy_tools_effects import *
from WikiBoxingFunctions import *
from UFCFunctions import *
#import TextToCLIWidget as tk
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



def StoreData(keep):

    # some dodge method to block the text from overlapping the c
    '''The data is store for the extra functionalties of the bot'''
    #This method is dodge , as i wanted to use this as a function....
    # Maybe in week4 i will fix it
    #but for now it works and does the job :)

    #If statement for the converstation points
    #put while loop to make this more robust
    data = keep
    text = str(data)
    if text == "main":
       print ('''
    Type in boxer for boxing related topics
    Type in MMA for MMA related topics
    Type in Wrestlers or WWE for its related topics
    ''')

    userInput =input(">>> ")
    if  userInput in "boxer" :
        BoxerConvo(text)

    elif  userInput in "/":
        # test with conor mcgregor
        ufc_text = str(data).lstrip("/")
        ufcSearch(ufc_text)# create a check if user input is wrong
    elif  userInput in "W:":
        print("Wrestler function")
        print("In progress!")

    if  userInput in "wow":
        webbrowser.open("http://radiowav.live/",new=2)
        tts_typoEffect("Cool")


def BoxerConvo(keep):

    '''this is for the boxer button'''

    data = keep
    if data =="boxer": print("Welcome to Boxing topic")
    print ("Type in the @Boxer for the name or ListBoxer for the list ")
    userInput = input(">>> ")
    clean = userInput.lstrip("@")
    if userInput[0] in "@":
        # to store The boxer name
        SearchBoxer(clean)
        tts_typoEffect("type in more for more info on {}".format(clean))
        userInput = input(">>> ")
        if  userInput == "more":
            WikiMoreInfoBoxer(clean)
            bg_tts("if you want the BoxRec i can give it to you , just type Yes : ")
            user_input=str(input(">>>>>"))
            if user_input.lower() == "yes":
                fristName, secondName = clean.split(" ",1)
                print (fristName , secondName)  # this is for the formant the boxrec site works
                GiveWebsiteBoxing(forename, lastname)


def MMAConvo(keep):
    s = keep
    print(s)


def WreslerConvo(keep):
    s = keep
    print (s)

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
        Can also tell you the weather
    ''')

    userInput=str(input(">>>>"))
    if userInput.lower() == "main":
        StoreData(userInput)








# replace def main wth python way of main
if __name__ == '__main__':

    BoxerConvo("boxer")


   # main()  # run the chatbot interface
   # tk.TextPageApp().run() In protype phase .....



