# user join date
import asyncio
from email import message
from typing import Optional
from discord.ext import commands
import discord
from discord import app_commands 
from model import queries
from core.profile_data import profile_embed

user_in_db = queries.PROFILEque()

class joined(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # /slash command


    def cooldown_for_everyone_but_me(interaction: discord.Interaction) -> Optional[app_commands.Cooldown]:
        if interaction.user.id == 840152379122384896:
            return None
        
        return app_commands.Cooldown(1, 259200) #3 days 

    """
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
    """
        

   
    @app_commands.command(name="join", description="joined date ")
    async def join(self, interaction: discord.Interaction, member: Optional[discord.Member] = None):

        """Says when a member joined."""
        member = member or interaction.user

        await interaction.response.send_message(f'`{member}` joined **{interaction.guild.name.upper()}** On {discord.utils.format_dt(member.joined_at)}', ephemeral=True)



async def setup(bot):
    await bot.add_cog(joined(bot))