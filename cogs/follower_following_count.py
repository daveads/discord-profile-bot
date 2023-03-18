from discord.ext import commands
import discord
from discord import app_commands 
from model import queries
from model import follower_following_query

user_in_db = queries.PROFILEque()
ffq = follower_following_query.Following_follower()

class ffCount(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="follower_following_count", description="followers and following details")
    async def follower_following_count(self, interaction: discord.Interaction):
        """ /follower_following_count """

        try:

            if user_in_db.get_user(interaction.user.id):

                followings = ffq.total_following_count(interaction.user.id)
                followers = ffq.total_followers_count(interaction.user.id)

                embed = discord.Embed(title="Profile details", description=f"{interaction.user.name} follower following details", color=0x808080)
                embed.add_field(name="Followers", value=str(followers), inline=True)
                embed.add_field(name="Following", value=str(followings), inline=True)

                await interaction.response.send_message(embed=embed, ephemeral=True)

            else: 
                await interaction.response.send_message("user doesn't have a profile yet", ephemeral=True)


        except:
            await interaction.response.send_message("That's not a user id", ephemeral=True)


    @follower_following_count.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)




async def setup(bot):
    await bot.add_cog(ffCount(bot))