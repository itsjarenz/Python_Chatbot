from requests import get # this will download the website for us
from requests.exceptions import RequestException # this will allow us to create a message if the website is not download
# http://docs.python-requests.org/en/master/

from contextlib import closing  #


# all the above will be used to extract data from  boxrec.com
# The reason why i had to create this long winded is that there are no boxing apis ( like the pyufc)
# Plus wikipedia cause all sort of problem * like no speific tailoerd data
# for the individual boxer ( records , belts , and different boxing assoication)
#https://realpython.com/python-web-scraping-practical-introduction/
# Above website help me a ton , on how to read html data and get it working on python

#http://boxrec.com/en/boxer/447121

def getUrl(url):
    '''This function get the html website'''
#All i know that the getURL function allows me to grab a website (XML,HTML) , if
#the website is not XML,HTML then the error will show...

    try:
        with closing(get(url,stream=True)) as resp:
            if getResponse(resp):
                return resp.content
            else:
                return none
            # all of the above code is not mines !
            # it from https://realpython.com/python-web-scraping-practical-introduction/
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def getResponse(resp):
    '''This function get reponsed if the websiet is HTML , if not the nothing is return'''
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None

            and content_type.find('html') > -1)
def log_error(e):
    """
   hold the errors of the getURl exception
    """
    print(e)
    #






