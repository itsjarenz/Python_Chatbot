import webbrowser # this will allow me open websites! #https://docs.python.org/2/library/webbrowser.html
from time import sleep
# make the quickfix for the bot to slow down...should do it in fancy tool module
import random # allows the bot too random choose the list of sentences!
from fancy_tools_effects import tts_typoEffect , bg_tts # import the fuction text to speech
import ChatbotGuruKate as GuruKateServices
#Note the chatbot is rule base , if questions are anwsered incorrently then system will prompt you to repeat process!
#did not want to do a rule base i've struggle with the tensorflow AI bot ( see tensorflow AI failed)

greetings = ['hello', 'hi', 'hey!','hey']
conversations= ['how are you?', 'how are you doing?']
date_coversations=["i need some dating advice"]
date_replies=["you can use my dating services , just type 2 !"]
replies = ["i'm okay just need some variables","i'm a CHATBOT what do you expect ! , I dont have feelings","Ummm , Well I'm fine , just that my Creator has'nt made me clever"]

def chatWithGuru():
        tts_typoEffect("Hi guys , come at chat with me...improve your social skills.......")
        user_type = input("****:  ").lower()#input of user lower.() allows typo error!
        while True:
                if user_type in greetings:
                        guru_kate_choice = random.choice(greetings)
                        tts_typoEffect(guru_kate_choice)
                        user_type = input("****:  ").lower()
                elif user_type in conversations:
                        guru_kate_choice = random.choice(replies)
                        tts_typoEffect(guru_kate_choice) # random ! choice from guru kate.....
                elif user_type in date_coversations:
                        guru_kate_choice=random.choice(date_replies)
                        tts_typoEffect(guru_kate_choice)
                        user_type = input("****:  ").lower()
                        if user_type=="2":
                                GuruKateServices.main()
                else:
                        tts_typoEffect("I am not that clever , so please talk more formally ")
                return False

chatWithGuru()