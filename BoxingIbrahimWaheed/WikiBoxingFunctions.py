import webbrowser
# this will allow me open websites! #https://docs.python.org/3/library/webbrowser.html
from time import sleep
# will make the search longer , as it is a spider
import wikipedia#https://wikipedia.readthedocs.io/en/latest/code.html
from fancy_tools_effects import tts_typoEffect
from APIForWebiste import getUrl # the function that i created with the help of realpython.com
from bs4 import BeautifulSoup  # for me to extract infromation from the HTML via tags
# I created this module , to make my files easy to read
# Plus i doesnt make sense to have boxing related functions on the fancy_tools file


def WikiMoreInfoBoxer(text):
    '''This function will grab the subheadings '''
    try:
        #Really nice function i created ! :)
        boxer=wikipedia.page(text)
        boxerInfo=wikipedia.summary(text,end="/n")
        tts_typoEffect(boxer.title)
        tts_typoEffect(boxerInfo)
    except wikipedia.DisambiguationError:
        tts_typoEffect("Type again")



def WikiLinksBoxer():
    '''Grabs the entire boxers names on the list of male boxers! too many!'''
    boxers_male_names = wikipedia.page("List_of_male_boxers")
    tts_typoEffect(boxers_male_names.title)
    boxers = [boxers_male_names.links]
    # Use a search array loop grab data and then allow search ! :)
    # for now just print vertical!
    for boxer in boxers:
        tts_typoEffect("\n".join(boxer))


def WikiLinksFeMaleBoxer():
    '''Grabs the entire boxers names on the list of male boxers! too many!'''
    boxers_male_names = wikipedia.page("List_of_female_boxers")
    tts_typoEffect(boxers_male_names.title)
    boxers = [boxers_male_names.links]
    # Use a search array loop grab data and then allow search ! :)
    # for now just print vertical!
    for boxer in boxers:
        tts_typoEffect("\n".join(boxer))

# create a more robust data for the chatbot to use
 # allows us to extract DOM nodes
# bascially it is a interface ,  it allows us to manipulate html/xml data
#for me this is really interesting , as it reminds me of Javascript


#
#my function to grab data from the html page via enter the boxer id


'''def BoxRec(id):
    grab the id and search for boxer
    #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    #https://docs.python.org/3/library/functions.html#enumerate

    getRawHTML = getUrl('http://boxrec.com/en/boxer/{}.html'.format(id))
    html=BeautifulSoup(getRawHTML,'html.parser')
    for i,tbody in enumerate(html.select('tbody')): # will get career table and then go thorught them via the parent/child DOM
        print(tbody.text)

        # the top grabs the career of the boxer , and he fight with he opponent'''
# Need to fix the above

def GiveWebsiteBoxing(f,l):
    first = str(f)
    last = str(l)
    sleep(2)
    SearchBoxRec=('http://boxrec.com/en/search?Lvo%5Bfirst_name%5D={}&Lvo%5Blast_name%5D={}&Lvo%5Brole%5D=boxer&Lvo%5Bstatus%5D=&pf_go=&Lvo%5BorderBy%5D=&Lvo%5BorderDir%5D='.format(first,last))
    webbrowser.open(SearchBoxRec,new=2)
