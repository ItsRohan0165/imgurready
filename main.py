import discord #the discord.py library
from discord import utils, Client
import asyncio #required to run async methods
import random #rng
import configparser #pulls credentials from auth.ini
import youtube_dl #music
import images #image module
import os

client=discord.Client()
audioQueue = []

players = {}


@client.event #startup
async def on_ready():
    print('Bot running')
    



@client.event #commands
async def on_message(message):
#chat log
    if message:
        print(message.channel.name + ': ' + message.author.name + ': ' + message.content)

#help command
    if message.content.lower().startswith('--help'):
        helpCommand = ('**__Commands__**\n\n'
                       '__Image(Imgur) commands__:\n'
                       '!top  --> Shows the top viewed image on the imgur frontpage\n'
                       '!img [tag]  --> Shows a random image with that tag\n\n'
                       '__Music commands__\n!play [yt link]  --> Bot joins the voice channel and plays a song\n'
                       '!add [yt link]  --> Queues a song\n'
                       '!skip  --> Skips to the next song in the queue\n'
                       '!pause  --> Pauses the current song\n'
                       '!resume  --> Continues the current song\n'
                       '!quit  --> Removes the bot from the voice channel')
        channel = message.channel
        await  channel.send(helpCommand)

# ----------------------- IMAGE COMMANDS ------------------------------
#Shows the top viewed image on the imgur frontpage
    elif message.content.lower().startswith('/top'):
        await  channel.send('Right now the most viewed image on the imgur frontpage is: ' + images.topCommand().link)

#Shows a random image with the tag you mentioned
    elif message.content.lower().startswith('/img'):
        tag = message.content[5:]
        result = images.imgCommand(tag)
        if not result:
            await channel.send('No images found for that tag :frowning:')
        else:
            await channel.send(result.link)

#---------------------------------- MUSIC COMMANDS ---------------------------------


#Shows the queue
    elif message.content.lower().startswith('--queue')
        await  channel.send(audioQueue)


client.run(os.getenv('TOKEN'))
