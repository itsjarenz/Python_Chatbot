from kivy.app import  App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
# The above is the Kivy framework , it allows me to create GUI in python.
#What makes kivy really powerful is that it sperates the logic(python) and the presentation(kv language)
# into separate components

import webbrowser
import fancy_tools_effects as fancy
from time import sleep

# All of the top imports are the Kivy GUI framework
#https://kivy.org/doc/ for help on the methods and classes



# i know that global is bad , but it had to be done

#Window.size = (width, height)



class TextDesign(BoxLayout): # Class inhertinace , the TestDesign used the boxlayout(from Kivy)
    sendText = ObjectProperty(None)
    sendBoxerText = ObjectProperty(None)
    seeText = ObjectProperty(None)
    def intro(self):
        self.seeText.text = """
        Type Play radio to listen to radio
        Type Wow to open a browser
        Type @{Boxer Name} 
        
        """


        fancy. bg_tts("Testing the text to speech api")


    def sendData(self): # acts like a main......
        userinput = self.sendBoxerText.text

        if userinput.lower() == "hi":
            self.intro()
        if userinput[0] in "@":
            fancy.WikiSearch(userinput.lstrip("@"))
            self.boxing()
        if userinput == "play radio" or userinput ==  "listen radio" :
            fancy.PlaySportRadio("None") # The Else make this text play the player
        if userinput == "stop radio":
            fancy.PlaySportRadio("stop")
        if userinput == "wow":
            webbrowser.open("http://radiowav.live/", new=2)





            print("test is working")
    def boxing(self):
        self.seeText.text = "Boxing Area"
        f = open("hold.txt" , "r")
        data=f.read()
        self.seeText.text = data
        f.close()

    # display text to label



class TextPageApp(App):
    pass


if __name__ == '__main__':
    TextPageApp().run()



# i read two books for me to understand how kivy framework works
#   Dusty., P., 2014. Creating Apps In Kivy. O'reilly Media.
#  Vaslikov, M., 2015. Kivy Blueprints. 1st ed. Packt Publishing Ltd.

# The above books really help me understand the difference between the logic side and presentation.