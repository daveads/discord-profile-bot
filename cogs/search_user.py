from discord.ext import commands
import discord
import asyncio
from discord import app_commands 

class search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    pass
    # /slash command

    @app_commands.command(name="find", description="search for a user profile")
    async def find(self, interaction: discord.Interaction):
        """ /find """
        await interaction.response.send_message(f'Hi, {interaction.user.mention}' , ephemeral=True)



async def setup(bot):
    await bot.add_cog(search(bot))