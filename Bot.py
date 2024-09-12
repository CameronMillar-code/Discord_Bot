
#imports
import os
import discord
from openai import OpenAI
import tiktoken
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

#get the different API tokens for both discord and chatgpt
DIS_TOKEN = os.getenv('DISCORD_TOKEN')
AI_TOKEN = os.getenv('OPENAI_TOKEN')



bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command(name='henlo')
async def henlo(msg, number):
    response = "hello you STINKY "+number
    await msg.send(response)
    
bot.run(DIS_TOKEN)