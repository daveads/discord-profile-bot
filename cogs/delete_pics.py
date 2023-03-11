import os
from discord.ext import commands
import discord
import asyncio
from discord import app_commands

from model import user_profile_image_query

from core import embed
from model import queries

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()
image_query = user_profile_image_query.Imageque()


class Delete_pics(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    
    @app_commands.command(name="deletep", description="Delete profile pictures")
    async def delete_pics(self, interaction: discord.Interaction):
        """ /deletep"""

        user = await self.bot.fetch_user(interaction.user.id)

        #user images 
        images_data = image_query.get_user_images(user.id)
        user_images = [img[0] for img in images_data]
        dir = "UserImages"

        if user_in_db.get_user(interaction.user.id):
            
            if user_images:

                for image in user_images:
                    os.remove(os.path.join(dir, image))
            
                image_query.delete_all_images(user_id=user.id)

                await interaction.response.send_message("Pictures Deleted", ephemeral=True)


            else:
                await interaction.response.send_message("YOU HAVE NO IMAGES TO DELETE", ephemeral=True)
        
        else:
            await interaction.response.send_message("YOU DONT HAVE A PROFILE YET", ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response() 

async def setup(bot):
    await bot.add_cog(Delete_pics(bot))
