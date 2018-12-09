import webbrowser # this will allow me open websites! #https://docs.python.org/2/library/webbrowser.html
from time import sleep
# make the quickfix for the bot to slow down...should do it in fancy tool module
from fancy_tools_effects import tts_typoEffect
# import the fuction text to speech
import ListGuruKate as ChatWithGuruServices #calls the fuction from another file
# allows users to chat with guru kate
#Note the chatbot is rule base , if questions are anwsered incorrently then system will prompt you to repeat process!
#did not want to do a rule base i've struggle with the tensorflow AI bot ( see tensorflow AI failed)


# For now this , but 2week will done via twitter/kik/tinder/facebook using flask(creating fake accounts and so on)


def user_details():
    '''The user will give details and base upon data the Guru Kate will give some advice'''
    tts_typoEffect("Please provide personal details")
    tts_typoEffect("As this will be required, for me to make a decision for you")
    try:
        userage_input=int(input("Your age please: "))
    except Exception:
        print(tts_typoEffect("Please enter numbers only!"))
        user_details()

    usersingle_input=input("Are you Single (Y/N): ").upper()
    usergender_input=input("Are you and Male or Female (M/F): ").upper()

    dataList=[userage_input,usersingle_input[0],usergender_input[0]]



    if dataList[0]>16<18 and dataList[1]=="Y" and dataList[2]=="M":
        tts_typoEffect("Well it seem from the data we collected you have dating anxiety")
        tts_typoEffect("So please watch this video to help you overcome your dating  problem ") #need to plan the speech!
        GuruKatePointA()
    elif dataList[0]>16<18  and dataList[1] == "N" and dataList[2] == "F":
            tts_typoEffect("Well it seem from the data we collected , you need some quite time")
            tts_typoEffect(
                "So please watch this video to help you overcome your  dating  problem ")  # need to plan the speech!
            GuruKatePointA()
    elif dataList[0]>16<18 and dataList[1] == "N" and dataList[2] == "M":
            tts_typoEffect("Well it seem from the data we collected , you need some quite time")
            tts_typoEffect(
                "So please watch this video to help you overcome your  dating  problem ")  # need to plan the speech!
            GuruKatePointA()
    elif dataList[0]>16<18 and dataList[1] == "Y" and dataList[2] == "M":
        tts_typoEffect("Well it seem from the data we collected , you need some quite time")
        tts_typoEffect(
            "So please watch this video to help you overcome your  dating  problem ")  # need to plan the speech!
        GuruKatePointA()
    elif dataList[0]<16 and dataList[1] == "Y" or dataList[1]=="N" or dataList[2] == "M" or dataList[2]=="F":
        tts_typoEffect("Please leave this service , as i do not tailor my services towards teenagers under 16!")

# Need to find a effective way....
# next if section for 18 to 25
    if dataList[0]>18<25 and dataList[1]=="Y" and dataList[2]=="M":
        tts_typoEffect("Well it seem from the data we collected you have dating anxiety")
        tts_typoEffect("So please watch this video to help you overcome your dating  problem ") #need to plan the speech!
        guru_kate_point_b_male()
    elif dataList[0]>18<25  and dataList[1] == "N" and dataList[2] == "F":
            tts_typoEffect("Well it seem from the data we collected , you need some quite time")
            tts_typoEffect(
                "So please watch this video to help you overcome your  dating  problem ")  # need to plan the speech!
            guru_kate_point_b_female()
    elif dataList[0]>18<25  and dataList[1] == "N" and dataList[2] == "M":
            tts_typoEffect("Well it seem from the data we collected , you need some quite time")
            tts_typoEffect(
                "So please watch this video to help you overcome your  dating  problem ")  # need to plan the speech!
            guru_kate_point_b_male()
    elif dataList[0]>18<25 and dataList[1] == "Y" and dataList[2] == "M":
        tts_typoEffect("Well it seem from the data we collected , you need some quite time")
        tts_typoEffect(
            "So please watch this video to help you overcome your  dating  problem ")  # need to plan the speech!
        guru_kate_point_b_female()


#userDOB_input=input("Date of Brith: ") for the zodic signs later one will work on this




def get_user_data():
    '''This is the functions  take UserDetails'''




def GuruKatePointA():
    '''This is the function for Guru kate Responds'''
    tts_typoEffect("Here you go , now remember that dating is all about guts!")
    webbrowser.open('https://www.youtube.com/watch?v=3kj1_QkwHuM&pbjreload=10', new=2)
    tts_typoEffect("Guru Kate Service charge of £6.99")

    # type in  youtube teenager dating advice :0

def guru_kate_point_b_male():
    '''This is the function for Guru kate Responds'''
    tts_typoEffect("Remain clam...")
    webbrowser.open('https://www.youtube.com/watch?v=zVwuV3qd114&pbjreload=10', new=2)
    tts_typoEffect("Guru Kate Service charge of £6.99")

    # type in  Male advice 18
def guru_kate_point_b_female():
    '''This is the function for Guru kate Responds'''
    tts_typoEffect("Remain clam...")
    webbrowser.open('https://www.youtube.com/watch?v=xhuj0ZOvKLI&pbjreload=10', new=2)
    tts_typoEffect("Guru Kate Service charge of £6.99")

    # type in  female advice
    #PS what am i doing with my life
# Note python main is below unlike C#
def main():
    '''The main fuction which the starting point will beginning'''
    x=("*"*50,"Welcome to Guru Kate Version Command Line Interface","*"*50)
    y=("*"*50,"Some time in the future I'll be on tinder, discord or kik","*"*50)
    tts_typoEffect(x)
    # the reason why i had to create the x y variable is that the tts_typoEffect can work as i does not act like the print fuction
    tts_typoEffect("Type 1 to chat with me(Chatterbot API SOON!)") # maybe uses list or chatterbot api to make it have some form of convo ....
    tts_typoEffect("Type 2 to take some dating advice from me") # Question and answer style chatbot.....
    tts_typoEffect("And finally Type 3 to leave")
    tts_typoEffect(y)
    user_input=input("Your Choice: ")

    if user_input == "1": #some function in progress
       ChatWithGuruServices.chatWithGuru()
    elif user_input == "2":
        user_details()
    elif user_input == "3":
            quit()  # maybe sys.exit



main()






