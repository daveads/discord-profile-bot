from discord.ext import commands
import discord
from discord import app_commands 

from view.modal.announce_modal import Announce
class announce(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="announce", description="feature announcement")
    async def announce(self, interaction: discord.Interaction):
        
        if interaction.user.id == 840152379122384896:
            
            modal = Announce()
            await interaction.response.send_modal(modal)
                  
        else:
            await interaction.response.send_message("Only @daveads#6337 can use this commands")
            



async def setup(bot):
    await bot.add_cog(announce(bot))