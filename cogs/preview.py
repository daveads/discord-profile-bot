from discord.ext import commands
import discord
import asyncio
from discord import app_commands


from core import embed
from model import queries

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()


class Preview(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    

    
    @app_commands.command(name="preview", description="check your profile update")
    async def cooldwn(self, interaction: discord.Interaction):
        """ /preview"""

        dic_key = ['id','username','username_id','name','location','looking_for','hobbies','biography','premium_day','profile_date']

        user = await self.bot.fetch_user(interaction.user.id)

        if user_in_db.get_user(interaction.user.id):
            
            user_d = user_in_db.get_user(interaction.user.id)
            user_data ={}
            for i in range(len(dic_key)):
                user_data[dic_key[i]] = user_d[i]


            embed=discord.Embed(title=f"PROFILE `{user_data['username']}` ", description="Your current profile details", color=discord.Color.blue())
            embed.set_thumbnail(url=user.avatar)
            embed.add_field(name="NAME ", value=f"{user_data['name']}", inline=True)
            embed.add_field(name="LOCATION", value=f"{user_data['location']}", inline=True)
            embed.add_field(name="LOOKING FOR", value=f"{user_data['looking_for']}", inline=True)
            embed.add_field(name="HOBBIES", value=f"{user_data['hobbies']}",inline=True)
            embed.add_field(name="BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
            embed.set_footer(text="profile can only be edited once a week",icon_url=user.avatar)

           
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response()


        else:
            await interaction.response.send_message("YOU DONT HAVE A PROFILE YET", ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response() 

async def setup(bot):
    await bot.add_cog(Preview(bot))
