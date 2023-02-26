import discord
import os
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event #when message is recieved
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event #when bot makes message
async def on_message():
    if message.author == client.user: #if the author of the message comes from the bit
        return #do nothing

    if message.content.startswith('$hello'): #test
        await message.channel.send('Hello!')

TOKEN = 
print(len(TOKEN))

client.run(os.getenv('TOKEN'))  #change this later. env is not working rn for some reason