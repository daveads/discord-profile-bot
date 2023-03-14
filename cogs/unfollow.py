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
              
                #profile_embed_data = await profile_embed(user, interaction)
                ffq.unfollower_user(user.id, interaction.user.id)
                     
                await interaction.response.send_message("User unfollowed")


            else: 
                await interaction.response.send_message("user doesn't have a profile yet")


        except:
            await interaction.response.send_message("That's not a user id")


    @unfollow.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)




async def setup(bot):
    await bot.add_cog(Unfollow(bot))