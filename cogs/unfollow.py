from typing import Optional
from discord.ext import commands
import discord
from discord import app_commands 
from model import queries
from model import follower_following_query

user_in_db = queries.PROFILEque()
ffq = follower_following_query.Following_follower()

class Unfollow(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="unfollow", description="unfollower a user")
    async def unfollow(self, interaction: discord.Interaction, user : discord.Member ):
        """ /unfollow """

        try:
        
            if user_in_db.get_user(interaction.user.id):
                
                if user.id == 840152379122384896:

                    await interaction.response.send_message("Once You Follow the Creator you are not allowed to Unfollow Him, You are bound forever")


                else:

                    user_check = ffq.user_ff_bool(user.id, interaction.user.id)
                    
                    if user_check:
                        ffq.unfollower_user(user.id, interaction.user.id)
                        
                        await interaction.response.send_message("User unfollowed")

                    else: 
                        await interaction.response.send_message("You aren't following this user")


            else: 
                await interaction.response.send_message("You Don't have a profile yet")


        except:
            await interaction.response.send_message("That's not a user id")


    @unfollow.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)




async def setup(bot):
    await bot.add_cog(Unfollow(bot))