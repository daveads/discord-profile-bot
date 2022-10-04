import discord
import os
import json
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
import time

load_dotenv()
token = os.getenv('TOKEN')
#f = open('./config.json')
#data = json.load(f)




intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True


description = '''Testing stuffs'''
owners = [840152379122384896]
bot = commands.Bot(command_prefix='!', intents=intents, description=description)

async def load():
    for f in os.listdir("./cogs"):
        if f.endswith(".py"):
            await bot.load_extension(f'cogs.{f[:-3]}')

@bot.command()
async def shutdown(ctx):
    await ctx.send("shutdown completed")

@bot.command()
async def emb(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    await ctx.send(embed=embed)

    
async def main():
    await load()
    await bot.start(token)

asyncio.run(main())