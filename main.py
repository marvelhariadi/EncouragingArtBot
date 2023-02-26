import discord
import os
from dotenv import load_dotenv #needed for os to work
import requests
import json
import random
from activewebserver import keep_alive

load_dotenv() 
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

artEncouragements = [
    "Your style is very beautiful",
    "i see you've improved",
    "Your art always brings me joy",
    "I like your art style"
]

cheerUppers = [
    "Hey!! Your art is freakin GORGEOUS and so are you",
    "Believe in yourself or I will make you x", #threatening love
    "The world would be so boring without your art",
    "You should know everyone looks at your art with stars in their eyes",
    f"Stop manifesting negativity in your life. You deserve to love yourself (and your art) the way I love you",
]

negSelfTalk = [
    "ugly",
    "bad",
    "I don't like my art style",
    "I dont like my art style",
    "horrendous",
    "hate",
    "mistake"
]

@client.event #when message is recieved
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event #when bot makes message 
async def on_message(message):
    author = message.author.name

    #guard
    if message.author == client.user: #if the author of the message comes from the bit
        return #do nothing

    #say hi
    if message.content.lower().startswith('hi art bot'): #test
        await message.channel.send(f'Hello, {author}! You certainly look friend-shaped today')

    #give encouragement
    if any(word in msg for word in negSelfTalk):
        await message.channel.send(random.choice(cheerUppers))

    #vent function
    if message.content.lower().startswith('venting: '):
         await message.delete() #immediately deletes that function
         await message.channel.send(f"thank you for sharing your hard feelings with me, {author}. I am proud of you <3")

keep_alive()
client.run(os.getenv('TOKEN')) #different on replit
 
#bot features i want:
#add a compliment
#say an art compliment
#bonus: add a bob-ross gif. good trial for spn bot