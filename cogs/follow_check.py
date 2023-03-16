from typing import Optional
from discord.ext import commands
import discord
from discord import app_commands 
from model import queries
from model import follower_following_query

user_in_db = queries.PROFILEque()
ffq = follower_following_query.Following_follower()

class FollowCheck(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="check_follower", description="check if a user is following you")
    async def checkFollower(self, interaction: discord.Interaction, user : discord.Member ):
        """ /check_follower """

        try:
            
            if user_in_db.get_user(interaction.user.id):

                following_check = ffq.user_ff_bool(interaction.user.id, user.id)
                
                if following_check:
                    await interaction.response.send_message(f"{user.name} is following you")

                else: 
                    await interaction.response.send_message(f"{user.name} isn't following you")


            else: 
                await interaction.response.send_message("user doesn't have a profile yet")


        except:
            await interaction.response.send_message("That's not a user id")


    @checkFollower.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)




async def setup(bot):
    await bot.add_cog(FollowCheck(bot))