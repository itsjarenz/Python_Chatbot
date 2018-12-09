# get ufc related information # far better than using wikipedia for information , as i can force direct user
# https://pypi.org/project/pyufc/ the docs for the libraries
from pyufc import Fighter , PyUFCError # this is the module i download , make grab UFC data easy
from fancy_tools_effects import tts_Effect


def ufcSearch(data):
    '''This function allows the bot to use the API to get uFC fighter data'''
    try:
        get_ufc_data=Fighter()# this is the class module provide by the API
        get_ufc_data.get_fighter(data)
        name = get_ufc_data.name
        ufc_record= get_ufc_data.record
        ufc_summary = get_ufc_data.summary#the name of fighter
        x=("{} {} {}".format(name,ufc_record,ufc_summary))
        return  x
    except PyUFCError: # call forth this error if the fighter is not found
        print("The UFC fighter is not found")

