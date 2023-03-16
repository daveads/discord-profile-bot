from typing import Optional
from discord.ext import commands
import discord
from discord import app_commands 
from model import queries
from model import follower_following_query

user_in_db = queries.PROFILEque()
ffq = follower_following_query.Following_follower()

class Command_debug_test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="command_test", description="@daveads")
    async def command_test(self, interaction: discord.Interaction):
        """ /command_test """

        if interaction.user.id == 840152379122384896:

            try:
                #FOLLOWERS
                #print(ffq.total_following_count(interaction.user.id)) ***
                print("total followers", ffq.total_followers_count(interaction.user.id))
                cc = ffq.followers_list(interaction.user.id)
                follower = [row[2] for row in cc]
                
                print(follower)
                print('')

                # Following
                dd = ffq.following_list(interaction.user.id)
                following = [row[2] for row in dd]
                print("following", following)


                await interaction.response.send_message(f"Test***")

            except:
                await interaction.response.send_message("unknown error db or logic related")

        else:
            await interaction.response.send_message("This is meant for the Creator only")

    @command_test.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)




async def setup(bot):
    await bot.add_cog(Command_debug_test(bot))