from discord.ext import commands
import discord
import asyncio
from discord import app_commands 
from model import queries


user_in_db = queries.PROFILEque()

class search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.dic_key = ['id','username','username_id','name','location','looking_for','hobbies','biography','premium_day','profile_date']
    pass
    # /slash command

    @app_commands.describe(first_value='Input user id',)
    @app_commands.command(name="find", description="search for a user profile")
    async def find(self, interaction: discord.Interaction, first_value : str):
        """ /find """

        #print(first_value)
        guild = self.bot.get_guild(interaction.guild.id)

        #print(guild)
        user = discord.utils.get(guild.members, name="daveads", discriminator="6337")
        #daveads#6337

        
        #if user:
        print(user)

        if user_in_db.get_user(840152379122384896):
            
            user_d = user_in_db.get_user(interaction.user.id)
            user_data ={}
          
            for i in range(len(self.dic_key)):
                user_data[self.dic_key[i]] = user_d[i]

            await interaction.response.send_message(f'your data {user_data}, {interaction.user.mention} {first_value}' , ephemeral=False)
            #await interaction.response.send_message(first_value)

        else: 
            await interaction.response.send_message("user doesn't have a profile yet")

async def setup(bot):
    await bot.add_cog(search(bot))