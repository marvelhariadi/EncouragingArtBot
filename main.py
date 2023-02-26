import discord
from discord.ext import commands
import os
from dotenv import load_dotenv  #needed for os to work. note: doesn't work for replit ver. as replit won't allow me to create .env file
import requests
import json
import random
from activewebserver import keep_alive
import giphy_client

# load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

artEncouragements = [
  "Your style is very beautiful", "I see you've improved!",
  "Your art always brings me joy", "I like your art style",
  "Your art is so cool!!!"
]

cheerUppers = [
  "Hey!! Your art is freakin GORGEOUS and so are you",
  "Believe in yourself or I will make you xoxo",  #threatening love
  "But the world would be so boring without your art!",
  "You should know everyone looks at your art with stars in their eyes!",
  "You deserve to love yourself the way I love you",
]

negSelfTalk = [
  "ugly", "bad", "I don't like my art style", "I dont like my art style",
  "horrendous", "hate", "mistake"
]


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
  author = message.author.name
  msg = message.content
  ctx = await bot.get_context(message)

 #guard
  if message.author == bot.user:  #if the author of the message comes from the bit
    return  #do nothing

  #say hi
  if ('hi' in msg.lower() or "hello" in msg.lower()) and 'art bot' in msg.lower():
    await message.channel.send(
      f'Hello, {author}! You certainly look friend-shaped today')

  #say encouraging words for artists
  if 'art bot' in msg.lower() and 'be nice' in msg.lower():
    await message.channel.send(random.choice(artEncouragements))
    
  #combat negative self talk
  if any(word in msg for word in negSelfTalk):
    await message.channel.send(random.choice(cheerUppers))

  #vent function
  if 'art bot' in msg.lower() and 'vent' in msg.lower():
    await message.channel.purge(limit=1)  #immediately deletes that function
    await message.channel.send(
      f"thank you for sharing your hard feelings with me, {author}. Nobody will ever see that ever again. I am proud of you for making it this far <3"
    )
    
  #bob ross gif function
  if 'art bot' in msg.lower() and 'bob ross' in msg.lower():
    await bobRossGif(ctx)

  if ("sad".lower() in msg):
    await message.channel.send(
      "I'm sorry you've been down. Perhaps papa Ross's wisdoms shall bring you peace"
    )
    await bobRossGif(ctx)

#helper function:
async def bobRossGif(ctx):
  api_key = os.getenv("API_KEY")
  api_instance = giphy_client.DefaultApi()
  api_response = api_instance.gifs_search_get(api_key, "bob+ross+quote", limit=5, rating='g')
  lst = list(api_response.data)
  giffingtons = random.choice(lst)
  await ctx.channel.send(giffingtons.embed_url)


keep_alive()
bot.run(os.getenv("TOKEN"))  #this line is different on github. des oke. replit doesn't like os
