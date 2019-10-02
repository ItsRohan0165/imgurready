import discord #the discord.py library
import asyncio #required to run async methods
import random #rng
import configparser #pulls credentials from auth.ini
import youtube_dl #music
import images #image module
import os


client = commands.Bot()

audioQueue = []

players = {}


@bot.event #startup
async def on_ready():
    print('Bot running')
    



@bot.event #commands
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
        await ctx.send(message.channel, helpCommand)

# ----------------------- IMAGE COMMANDS ------------------------------
#Shows the top viewed image on the imgur frontpage
    elif message.content.lower().startswith('/top'):
        await ctx.send(message.channel, 'Right now the most viewed image on the imgur frontpage is: ' + images.topCommand().link)

#Shows a random image with the tag you mentioned
    elif message.content.lower().startswith('/img'):
        tag = message.content[5:]
        result = images.imgCommand(tag)
        if not result:
            await ctx.send(message.channel, 'No images found for that tag :frowning:')
        else:
            await ctx.send(message.channel, result.link)

#---------------------------------- MUSIC COMMANDS ---------------------------------
#Lets the bot leave voice
    elif message.content.lower().startswith('--quit'):
        voice_client = bot.voice_client_in(message.server)
        if not voice_client:
            await ctx.send(message.channel, 'I\'m not in a voice channel right now')
        else:
            await voice_client.disconnect()

#Lets the bot join your voice channel and plays a song
    elif message.content.lower().startswith('--play'):
        yt_url = message.content[6:]
        channel = message.author.voice.voice_channel
        if not channel:
            await ctx.send(message.channel, 'You have to be in a voice channel')
        else:
            voice_client = bot.voice_client_in(message.server)
            if not voice_client:
                voice = await bot.join_voice_channel(channel)
                if not yt_url:
                    await ctx.send(message.channel, 'You have to provide a link to a youtube video')
                else:
                    player = await voice.create_ytdl_player(yt_url)
                    players[message.server.id] = player
                    player.start()
            else:
                await ctx.send(message.channel, 'Please use !add [Youtube link] to add songs to the queue')

#Pauses the song
    elif message.content.lower().startswith('--pause'):
        players[message.server.id].pause()

#Continues the song
    elif message.content.lower().startswith('--resume'):
        players[message.server.id].resume()

#Adds a song to the queue
    elif message.content.lower().startswith('!add'):
        yt_url = message.content[5:]
        audioQueue.append(yt_url)
       

#Shows the queue
    elif message.content.lower().startswith('--queue'):
        await ctx.send(message.channel, audioQueue)


bot.run(os.getenv('TOKEN'))
