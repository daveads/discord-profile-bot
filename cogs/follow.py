from typing import Optional
from discord.ext import commands
import discord
from discord import app_commands 
from model import queries
from model import follower_following_query

user_in_db = queries.PROFILEque()
ffq = follower_following_query.Following_follower()

class Follow(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="follow", description="follower a user")
    async def followu(self, interaction: discord.Interaction, user : discord.Member ):
        """ /follow """
        
        user_check = ffq.user_ff_bool(user.id, interaction.user.id)

        try:
            
            if user_check:

                await interaction.response.send_message("You are alreadying following this user")
            

            else:

                await ffq.follow_user(user.id, interaction.user.id)
                    
                print("total following", ffq.total_following_count(interaction.user.id))
                print("total followers", ffq.total_followers_count(interaction.user.id))

                await interaction.response.send_message("User followed")


                #else: 
                #    await interaction.response.send_message("user doesn't have a profile yet")

            
        except:
            await interaction.response.send_message("That's not a user id")


    @followu.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)




async def setup(bot):
    await bot.add_cog(Follow(bot))