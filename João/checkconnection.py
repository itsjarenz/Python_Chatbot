import socket
"""https://stackoverflow.com/questions/20913411/test-if-an-internet-connection-is-present-in-python"""
def check_connection(website): #should be a string (ex."www.google.com")
    port = 80
    try:
        socket.create_connection((website, port))
        return True
    except OSError:
        print("You can't connect to that website")
    return False