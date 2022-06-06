import discord
import os
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
    logger.log(logging.INFO, 'We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(('Hello', 'hello', 'hi', 'Hi')):
        await message.channel.send('Hello!')
    if 'Pickle' in message.content or 'pickle' in message.content:
        await message.channel.send(':cucumber:')

client.run(os.environ.get('DISCORD_TOKEN'))
