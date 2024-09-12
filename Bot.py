
#imports
import os
import discord
import json
import requests
from urllib import parse
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()



#get the different API tokens for both discord and chatgpt
DIS_TOKEN = os.getenv('DISCORD_TOKEN')
HS_SECRET = os.getenv('HEARTHSTONE_SECRET')
HS_ID = os.getenv("HEARTHSTONE_ID")


#generate access token for blizzard api
data = { 'grant_type': 'client_credentials' }
response = requests.post('https://oauth.battle.net/token', data=data, auth=(HS_ID, HS_SECRET))
list_response = response.text.split('"')[1::2]
hs_access_token = list_response[1]



bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command(name='hs')
async def hearthstone(msg, search_input= "boulderfist ogre"):
    parse.quote(search_input)
    try:
        #performs a search for the card in question, defaults to boulderfist ogre if no input is given
        url = 'https://us.api.blizzard.com/hearthstone/cards?locale=en_US&access_token={access_token}&textFilter={text}'.format(access_token = hs_access_token, text = search_input)
        response = requests.get(url)
        response_data = response.json()

        image = json.dumps(response_data['cards'][0]["image"])
        image = image[1:-1]
        await msg.send(image)
    except:
        output = "Sorry sir, I could not find that card."
        await msg.send(output)


bot.run(DIS_TOKEN)