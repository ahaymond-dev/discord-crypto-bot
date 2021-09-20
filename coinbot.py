import discord
import os
from dotenv import load_dotenv
import requests

load_dotenv()

client = discord.Client()
api_url = 'http://api.coinlayer.com/api/live'
api_key = os.getenv('COINLAYER_KEY')
token = os.getenv('BOT_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        await message.channel.send('this bot is working!')

    if message.content.startswith('$ada'):
        url = f'{api_url}&symbols=ADA?access_key={api_key}'
        raw = requests.get(url).json()
        response = []
        response.append(raw['rates'])
        price = response[0]
        await message.channel.send(f'{price}')

client.run(token)
