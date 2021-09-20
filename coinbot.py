import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

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

client.run(token)
