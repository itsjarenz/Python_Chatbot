import kivy
kivy.require('1.9.0')
from kivy.app import  App
from kivy.uix.button import Label

class ChatbotApp(App):
    def build(self):
        return Label()
OpenChat = ChatbotApp()
OpenChat.run()


#WEEK 3 SHOULD BE COMPLETED