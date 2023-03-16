from discord.ext import commands
import discord
import asyncio
from discord import app_commands

from core.profile_data import profile_embed

from core import embed
from model import queries

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()


class Preview(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    

    
    @app_commands.command(name="preview", description="Preview your current profile!")
    async def cooldwn(self, interaction: discord.Interaction):
        """ /preview"""

        user = await self.bot.fetch_user(interaction.user.id)

        if user_in_db.get_user(interaction.user.id):
            
        
            profile_embed_data = await profile_embed(user, interaction)

            embed, file = profile_embed_data


            if file:
                await interaction.response.send_message(file=file, embed=embed, ephemeral=True)
                await asyncio.sleep(60)
                await interaction.delete_original_response()

            else:
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await asyncio.sleep(60)
                await interaction.delete_original_response()


        else:
            await interaction.response.send_message("YOU DONT HAVE A PROFILE YET", ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response() 

async def setup(bot):
    await bot.add_cog(Preview(bot))
