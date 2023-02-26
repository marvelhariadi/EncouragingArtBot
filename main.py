import discord
import os
from dotenv import load_dotenv #needed for os to work. note: doesn't work for replit ver. as replit won't allow me to create .env file
import requests
import json
import random
from activewebserver import keep_alive
import giphy_client


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

@client.event #log-in conformation
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event #all bot outputs
async def on_message(message):
    author = message.author.name
    msg = message.content

    #guard
    if message.author == client.user: #if the author of the message comes from the bit
        return #do nothing

    #say hi
    if msg.lower().startswith('hi art bot'): #test
        await message.channel.send(f'Hello, {author}! You certainly look friend-shaped today')

    #give encouragement
    if any(word in msg for word in negSelfTalk):
        await message.channel.send(random.choice(cheerUppers))

    #vent function
    if msg.lower().startswith('art bot, I need to vent') | msg.lower().startswith('art bot I need to vent'):
        vent(author)

    #bob ross gif function
    if msg.lower().startswith('Bob Ross me'):
        bobRossGif()

    if any(word in msg == "sad"):
        await message.channel.send("I'm sorry you've been down. Perhaps Papa Ross's wisdoms shall bring you peace")
        bobRossGif()


#abstracted functions
@client.event
async def vent(author):
    await message.delete() #immediately deletes that function
    await message.channel.send(f"thank you for sharing your hard feelings with me, {author}. I am proud of you <3")

@client.event
async def bobRossGif():
    api_key = os.getenv('API_KEY') #replit issue
    api_instance = giphy_client.DefaultApi()
    api_response = api_instance.gifs_search_get(api_key, "bob+ross+quote", limit=5, rating='g')

keep_alive()
client.run(os.getenv('TOKEN')) #replit issue
 
#bot features i want:
#add a compliment
#say an art compliment
#bonus: add a bob-ross gif. good trial for spn bot