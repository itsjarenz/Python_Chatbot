from Rugby.Functions import *

def gwynMain():
    rugby()
    while True:
        text = str(uinput())
        if text == "help":
            help()
        elif text == "leagues" or text == "league":
            league()
        elif text == "teams":
            teams()
        elif text == "players":
            player()
        elif text == "fixtures":
            fixtures()
        elif text == "tables":
            tables()
        elif text == "results":
            results()
        elif text == "anything":
            anySummary()
        elif text == "exit":
            break
        else:
            print("Unknown command!")

        print("""
        Ask me about something!""")




