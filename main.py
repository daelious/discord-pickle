import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(('Hello', 'hello', 'hi', 'Hi')):
        await message.channel.send('Hello!')
    if 'Pickle' in message.content or 'pickle' in message.content:
        await message.channel.send(':cucumber:')

client.run(os.environ.get('DISCORD_TOKEN'))
