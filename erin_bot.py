from dotenv import load_dotenv
load_dotenv()

import os
import urllib.request
import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'The bot has logged in as {bot.user} and is ready to serve requests of its human overlords.')

bot.run(os.getenv('BOT_TOKEN'))
