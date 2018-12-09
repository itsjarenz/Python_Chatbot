# Work with Python 3.6
import discord
from discord.ext.commands import  Bot
from discord.ext import  commands
import asyncio
import time


TOKEN = 'NTA0MjMyODA0MTIxNDQ0MzUz.DrCvOw.RdCjINgTTRVorFxF_AMHFdRj9_4'

client = discord.Client()
client = commands.Bot (command_prefix ="!")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.upper().startswith('!hi'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s>  Ummmm watch some youtube videos!" % userID)
        if message.content.upper().startswith("!Give me an youtube video on "):
            await client.send_message(message.channel, "<@%s> https://www.youtube.com/watch?v=l7ZlSHGFfdc&pbjreload=10  Please enjoy !" % userID)
    if message.content.startswith('!Chatbot'):
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>  Guru Kate Discord Version" % userID)
    if message.content.startswith('!BoxingList'):
            userID = message.author.id
            await client.send_message(message.channel,WikiLinksBoxer()  % userID)





client.run(TOKEN)