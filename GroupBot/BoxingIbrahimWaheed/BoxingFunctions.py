import webbrowser
# this will allow me open websites! #https://docs.python.org/3/library/webbrowser.html
from time import sleep
# import sleep will be used in the BoxRec Function which is a web spider-
# ( some website will block IPs address if they deem the user to be a bot)
import wikipedia#https://wikipedia.readthedocs.io/en/latest/code.html
from fancy_tools_effects import tts_Effect # from the module i created
from BoxingIbrahimWaheed.APIForWebiste import getUrl # the function that i created with the help of realpython.com
from bs4 import BeautifulSoup  # for me to extract information from the HTML via tags
# I created this module , to make my files easy to read
# Plus it does not make sense to have boxing related functions on the fancy_tools file , as the team would not need them


def WikiMoreInfoBoxer(text):
    '''This function will grab the subheadings '''
    try:
        #Really nice function i created ! :)
        boxer=wikipedia.page(text)
        boxerInfo=wikipedia.summary(text,sentences=4)
        print(boxer.title)
        print(boxerInfo)
        tts_Effect("Do you want me to speak the above information")
        userInput=input("Type yes or no")
        if userInput.lower =="yes":
            print(boxerInfo)

    except wikipedia.DisambiguationError: #if the name does not exst in wikiepedia then give message
        return "try Again"


def WikiLinksBoxer():
    '''Grabs the entire boxers names on the list of male boxers! too many!'''
    boxers_male_names = wikipedia.page("List_of_male_boxers")
    tts_Effect(boxers_male_names.title)
    boxers = [boxers_male_names.links]
    # Use a search array loop grab data and then allow search ! :)
    # for now just print vertical!
    for boxer in boxers:
        print("\n".join(boxer))



def WikiLinksFeMaleBoxer():
    '''Grabs the entire boxers names on the list of male boxers! too many!'''
    boxers_male_names = wikipedia.page("List_of_female_boxers")
    tts_Effect(boxers_male_names.title)
    boxers = [boxers_male_names.links]
    # Use a search array loop grab data and then allow search ! :)
    # for now just print vertical!
    for boxer in boxers:
        tts_Effect("\n".join(boxer))

# create a more robust data for the chatbot to use
 # allows us to extract DOM nodes
# bascially it is a interface ,  it allows us to manipulate html/xml data
#for me this is really interesting , as it reminds me of Javascript


#
#my function to grab data from the html page via enter the boxer id



def BoxRec(id):
    ''' This function will allow me to get the id of the boxer and get his fighting record from the website BoxRec'''
    #grab the id and search for boxer
    #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    #https://docs.python.org/3/library/functions.html#enumerate


    getRawHTML = getUrl('http://boxrec.com/en/boxer/{}.html'.format(id))
    html=BeautifulSoup(getRawHTML,'html.parser')
    #https://docs.python.org/3/library/functions.html#enumerate
    for i,tbody in enumerate(html.select('tbody')): # will get career table and then go thorught them via the parent/child DOM
        sleep(3) # dont want to get ip blocked :)
        print(tbody.text)

        # the top grabs the career of the boxer , and he fight with he opponent'''
# The only problem the above function has is that ID are numerical , thus the problem is how does the user know the ID of-
# the boxer.So i might not used this... It works.



def GiveWebsiteBoxing(f,l):
    ''' Will open a website with the data provided.'''
    # the params f and l are convert to str
    first = str(f)
    last = str(l)
    # using sleep , as the IP address will act normal and not like some bot
    sleep(2)
    # the SearchBoxRec variable has the website like and formant so that the f , l will be place in the {} placeholders
    SearchBoxRec=('http://boxrec.com/en/search?Lvo%5Bfirst_name%5D={}&Lvo%5Blast_name%5D={}&Lvo%5Brole%5D=boxer&Lvo%5Bstatus%5D=&pf_go=&Lvo%5BorderBy%5D=&Lvo%5BorderDir%5D='.format(first,last))
    #using the in-bulit module webbrowser , it will open the website with the default brwoser the users has installed.
    webbrowser.open(SearchBoxRec,new=2)
