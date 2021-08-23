import discord

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content('$hello'):
        await message.channel.send('Hello!')

client.run('ODc4NjcwNTczNzEzMTI1NDM3.YSEjvQ.As8J_HTLPSPyzYreEhRIo7ax5xM')
