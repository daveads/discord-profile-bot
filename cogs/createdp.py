from discord.ext import commands
import discord
from discord import app_commands 
from model import queries

user_in_db = queries.PROFILEque()

class users(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
 

   
    @app_commands.command(name="profiles", description="Total number of profile created")
    async def profile(self, interaction: discord.Interaction):
        
        count = user_in_db.total_created_profile()

        count_data = ()

        for i in count:
            count_data = i

        counter = count_data[len(count_data)-11]


        embed=discord.Embed(title="Total Number of Created Profile", description=f" `Profile Count` : {counter} Users", color=0xFF5733)
        
        await interaction.response.send_message(embed=embed)
        



async def setup(bot):
    await bot.add_cog(users(bot))