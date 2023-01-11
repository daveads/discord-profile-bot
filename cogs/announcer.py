from discord.ext import commands
import discord
import asyncio

class announce(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    pass
    # /slash command



async def setup(bot):
    await bot.add_cog(announce(bot))