import discord
import os
from dotenv import load_dotenv
import requests

load_dotenv()

client = discord.Client()
api_url = 'http://api.coinlayer.com/api/live'
api_key = os.getenv('COINLAYER_KEY')
token = os.getenv('BOT_TOKEN')

def get_crypto_price(symbol):
    url = f'{api_url}&symbols={symbol}?access_key={api_key}'
    raw = requests.get(url).json()
    response = []
    response.append(raw['rates'])
    prices = response[0][f'{symbol}']

    return prices

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        await message.channel.send('this bot is working!')

    if message.content.startswith('$ADA'):
        price = get_crypto_price('ADA')
        await message.channel.send(f'{price}')

    if message.content.startswith('$BTC'):
        price = get_crypto_price('BTC')
        await message.channel.send(f'{price}')
    
    if message.content.startswith('$ETH'):
        price = get_crypto_price('ETH')
        await message.channel.send(f'{price}')

    if message.content.startswith('$DOGE'):
        price = get_crypto_price('DOGE')
        await message.channel.send(f'{price}')

client.run(token)
