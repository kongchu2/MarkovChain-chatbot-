import discord

import os
import time
from dotenv import load_dotenv
from botengine import make_reply

load_dotenv()
TOKEN = os.getenv('TOKEN')
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print(f'Bot is ready and logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user.mentioned_in(message):
        await message.channel.send(f'{make_reply(message.content)}')

client.run(TOKEN)
