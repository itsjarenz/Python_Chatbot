from requests import get, ConnectionError #internet imports
"""Code to check the conection to a specific website, got it on stacks overflow"""
def check_internet(url, timeout):
    try:
      get("https://"+url, timeout=timeout)
      return True
    except ConnectionError:
      print("You don't have internet connection")
      return False
