#""'Here we import all the necessary API's '""

import random
import discord
import wikipedia
from discord.ext.commands import Bot
from weather import Weather, Unit

#""'We declare ? and ! into BOT_PREFIX tuple!! '""
BOT_PREFIX = ('?','!')

#""'Here we set ? and ! as special symbols to call the Bot!! '""

client = Bot(command_prefix = BOT_PREFIX)


#""'Bot command that takes two arguments that they will be used to search informations through wikipedia,
#using bot supported languages!! '""

@client.command(brief = "[wikipedia search][language]",)
async def wiki(context, setLanguage,):
        supportedLanguages = ['en','fr','de','es','it']
        if setLanguage in supportedLanguages:
            wikipedia.set_lang(setLanguage)
            definition = wikipedia.summary(context, sentences=2, chars=100,
                                   auto_suggest=True, redirect=True)
            await client.say(context + ' summary: '+definition)
        elif setLanguage not in supportedLanguages:
            await client.say("Error i don't support this language or you typed a non-existing language!!")
        return

#""'Bot command which when you run it will respond you with all the current Olympic Sports, You can use it
#to have some ideas for summary[Ideas for WIKI command!!]  '""

@client.command()
async def echoolympicsports():
    olympicSports = ['Gymnastics',
                     'Triathlon',
                     'Tennis',
                     'Basketball',
                     'Golf',
                     'Cycling',
                     'Boxing',
                     'Swimming',
                     'Equestrian',
                     'Hockey',
                     'Football',
                     'Rowing',
                     'Curling',
                     'Badminton',
                     'Baseball',
                     'Bobsleigh',
                     'Ice hockey',
                     'Modern pentathlon',
                     'Cricket',
                     'Taekwondo',
                     'Fencing',
                     'Table Tennis',
                     'Volleyball',
                     'Archery',
                     'Softball',
                     'Olympic weightlifting',
                     'Rugby union',
                     'Diving',
                     'Artistic swimming',
                     'Skeleton',
                     'Speed skating',
                     'Snowboarding',
                     'Biathlon',
                     'Judo',
                     'Team Handball',
                     'Cross-country skiing',
                     'Luge',
                     'Surfing',
                     'Figure skating',
                     'Freestyle skiing',
                     'Karate',
                     'Polo',
                     'Wrestling',
                     'Alpine skiing',
                     'Track and field athletics',
                     'Ski jumping',
                     'Short track speed skating',
                     'Canoeing',
                     'Water polo',
                     'BMX']

    echoSports = ' '.join(olympicSports)
    await client.say(echoSports)

#""'Bot command which gets a City of the world as an argument[It will return as the current date
#with the current weather condition of the City that we chose!!] '""

@client.command(brief = "[Input a City]")
async def weathercondition(userLocation):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(userLocation)
    condition = location.condition
    await client.say(condition.date+'- the weather in '+userLocation+' is '+ condition.text)

#""'Bot command which gets a City of the world as an argument again[This time it will return as
#the forecast of the weather for the next nine days(weather temperature for each day as an extra)]   '""

@client.command(brief="[Input a City]")
async def forecast(userCity):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(userCity)
    forecasts = location.forecast
    for forecast in forecasts:
        await client.say('Location: ' + userCity.upper())
        await client.say('Date: '+forecast.date)
        await client.say('Condition: ' + forecast.text)
        await client.say('Temperature: High[ ' + forecast.high + '°C ] - Low[ ' + forecast.low + '°C ]')
        await client.say('------------NEXT-------------')

#""'Bot command which takes a user as an argument and welcomes you into the server channel!!'""

@client.event
async def new_user_join(user):
    client = discord.Client()
    server = user.server
    botEcho = 'Oh..Welcome {0.mention} to {1.name}!!'
    await client.send_message(server,botEcho.format(user,server))


#""'Checks if the bot is ready for use and if it's logged in'""
@client.event
async def on_ready():
    typesOfHello = ['Hello', 'Hey', 'Hi']
    print(random.choice(typesOfHello) + ', ' + 'you are ' + 'Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



#""'Here you have to add your Bots token to make your Bot go online!!'""

client.run("Discord Bot TOKEN HERE!!!!")
