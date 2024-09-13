
# imports
import os
import discord
import json
import requests
from urllib import parse
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()



# Get the different API tokens for dicord and hearthstone
DIS_TOKEN = os.getenv('DISCORD_TOKEN')
HS_SECRET = os.getenv('HEARTHSTONE_SECRET')
HS_ID = os.getenv("HEARTHSTONE_ID")


# Generate access token for blizzard api
data = { 'grant_type': 'client_credentials' }
response = requests.post('https://oauth.battle.net/token', data=data, auth=(HS_ID, HS_SECRET))
list_response = response.text.split('"')[1::2]
hs_access_token = list_response[1]



bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# Card search for Hearthstone
@bot.command(name='hs', help = "Returns a Hearthstone card when given a card name.")
async def hearthstone(msg, *, args):
    search_input = args
    parse.quote(search_input)
    try:
        # performs a search for the card in question, defaults to boulderfist ogre if no input is given
        url = 'https://us.api.blizzard.com/hearthstone/cards?locale=en_US&access_token={access_token}&textFilter={text}'.format(access_token = hs_access_token, text = search_input)
        response = requests.get(url)
        response_data = response.json()

        # pull image data for first result from search
        image = json.dumps(response_data['cards'][0]["image"])
        image = image[1:-1]
        await msg.send(image)
    except:
        output = "Sorry sir, I could not find that card."
        await msg.send(output)

@bot.command(name='bg', help = "Returns a Battlegrounds card when given a card name.")
async def hearthstone(msg, *, args):
    search_input = args
    parse.quote(search_input)
    try:
        # performs a search for the card in question, defaults to boulderfist ogre if no input is given
        url = 'https://us.api.blizzard.com/hearthstone/cards?locale=en_US&access_token={access_token}&gameMode=battlegrounds&textFilter={text}'.format(access_token = hs_access_token, text = search_input)
        response = requests.get(url)
        response_data = response.json()

        # pull image data for first result from search
        image = json.dumps(response_data['cards'][0]["image"])
        
        image = image[1:-1]
        await msg.send(image)
    except:
        output = "Sorry sir, I could not find that card."
        await msg.send(output)

@bot.command(name='mtg', help = "Returns a Magic card when given a card name.")
async def Magic(msg, *, args):
    try:
        search_input = args
        parse.quote(search_input)
        url = "https://api.scryfall.com/cards/search?q={search_query}".format(search_query = search_input)
        response = requests.get(url)
        response_data = response.json()

        image = json.dumps(response_data['data'][0]['image_uris']['png'])

        image = image[1:-1]
        await msg.send(image)
    except:
        output = "Sorry sir, I could not find that card."
        await msg.send(output)

bot.run(DIS_TOKEN)