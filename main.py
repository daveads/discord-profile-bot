import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
from model import profile

# intializing database
profile.main()

load_dotenv()
token = os.getenv('TOKEN')

"""
intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True
"""

from core.bot  import ProfileBot
#from src.core.config_parser import BotConfigs

load_dotenv()
bot = ProfileBot()
#bot_configs = BotConfigs()

async def load():
    for f in os.listdir("./cogs"):
        if f.endswith(".py"):
            await bot.load_extension(f'cogs.{f[:-3]}')


bot.remove_command('help')  
async def main():
    await load()
    await bot.start(token)

asyncio.run(main())