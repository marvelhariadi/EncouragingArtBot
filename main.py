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
  "Your style is very beautiful", "i see you've improved",
  "Your art always brings me joy", "I like your art style"
]

cheerUppers = [
  "Hey!! Your art is freakin GORGEOUS and so are you",
  "Believe in yourself or I will make you x",  #threatening love
  "The world would be so boring without your art",
  "You should know everyone looks at your art with stars in their eyes",
  f"Stop manifesting negativity in your life. You deserve to love yourself (and your art) the way I love you",
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
  if msg.lower().startswith('hi art bot'):  #test
    await message.channel.send(
      f'Hello, {author}! You certainly look friend-shaped today')

  #give encouragement
  if any(word in msg for word in negSelfTalk):
    await message.channel.send(random.choice(cheerUppers))

  #vent function
  if msg.lower().startswith('vent time:'):
    await message.channel.purge(1)  #immediately deletes that function
    await message.channel.send(
      f"thank you for sharing your hard feelings with me, {author}. I am proud of you <3"
    )

  #bob ross gif function
  if msg.lower().startswith('bob ross me'):
    await bobRossGif(ctx)

  if ("sad".lower() in msg):
    await message.channel.send(
      "I'm sorry you've been down. Perhaps Papa Ross's wisdoms shall bring you peace"
    )
    await bobRossGif(ctx)


async def bobRossGif(ctx):
  api_key = os.getenv("API_KEY")
  api_instance = giphy_client.DefaultApi()
  api_response = api_instance.gifs_search_get(api_key, "bob+ross+quote", limit=5, rating='g')
  lst = list(api_response.data)
  giffingtons = random.choice(lst)
  await ctx.channel.send(giffingtons.embed_url)


keep_alive()
bot.run(os.getenv("TOKEN"))  #this line is different on github. des oke. replit doesn't like os
