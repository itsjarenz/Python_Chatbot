import requests
from bs4 import BeautifulSoup
pro14URL = requests.get("https://en.wikipedia.org/wiki/Pro14").text

soup =