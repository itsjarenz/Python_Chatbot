import Jarence as basketBall
import Ibrahim as CombatSport
import shueb as Cricket
import gwyn as Rugby
#import joao as Football
#import OlympicSports_Joseph as Olympic
from  fancy_tools_effects import bg_tts , tts_Effect







def SportTalk():
    print("=============SportTalkBot=================")
    tts_Effect('''
    Which sports do you want to talk about
                    1)BasketBall
                    2)CombatSports
                    3)Cricket
                    4)Football
                    5)OlympicSports
                    6)Rugby''')
    bg_tts("Enter The Sport Topic You want to go to")
    userInput=input(str("Enter The Sport Topic You want to go to: "))

    if userInput in "1":
        basketBall.BasketBall()
    elif userInput in "2":
        CombatSport.main()
    elif userInput in "3":
        Cricket.CricketMain()
    elif userInput in "4":
       pass
    elif userInput in "5":
        pass
    elif  userInput in "6":
        Rugby.gwynMain()


if __name__ == '__main__':
    SportTalk()
    from Rugby.Functions import *


    





