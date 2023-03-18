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


class Display(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    
    @app_commands.command(name="display", description="Display user profile pictures")
    async def display_pics(self, interaction: discord.Interaction, user_p : discord.Member):
        """ /display"""

        user = await self.bot.fetch_user(interaction.user.id)

        #user images 
        images_data = image_query.get_user_images(user_p.id)
        user_images = [img[0] for img in images_data]
        dir = "UserImages/"

        if user_in_db.get_user(user.id):
            if user_in_db.get_user(user_p.id):

                from core.random_image import randomise_image                
                if user_images:
                    
                    user_pic = randomise_image(user_images)

                    file = discord.File(f"{dir}{user_pic}")
                    embed = discord.Embed(title=f"{user_p.name} profile picture", description=f'{user_p}', color=0x00ff00)
                    embed.set_image(url=f"attachment://{user_pic}")

                    await interaction.response.send_message(file=file, embed=embed)


                else:
                    await interaction.response.send_message("YOU HAVE NO Profile IMAGE", ephemeral=True)
        
            else:
                await interaction.response.send_message(f"{user_p.name} Doesn't Have a profile", ephemeral=True)

        else:
            await interaction.response.send_message("YOU Need To Have a Profile to be able to Use this", ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response() 

async def setup(bot):
    await bot.add_cog(Display(bot))

# any(val in a for val in (d,b,c))