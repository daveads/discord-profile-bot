from typing import Optional
from discord.ext import commands
import discord
from discord import app_commands 
from model import queries
from model import follower_following_query

user_in_db = queries.PROFILEque()
ffq = follower_following_query.Following_follower()

class FollowersList(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="followers", description="See a User Followers or Yours")
    async def followers_list(self, interaction: discord.Interaction, member: Optional[discord.Member] = None):
        """ /followers """

        # If no member is explicitly provided then we use the command user here
        member = member or interaction.user
        
        try:

            if user_in_db.get_user(member.id):

                followers = ffq.followers_list(member.id)

                if followers:
                    # embeds
                    embed = discord.Embed(title="Profile details", description=f"Followers", color=0x808080)

                    for id in followers:
                        embed.add_field(name="*", value=f"<@{id}>", inline=True)

                    embed.set_footer(
                        text=f"{member.name} Followers",
                        icon_url=member.guild.icon.url,
                    )

                    await interaction.response.send_message(embed=embed, ephemeral=True)

                else:
                    embed = discord.Embed(title="Profile details", description=f"0 Followers", color=0x808080)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    
            else: 
                await interaction.response.send_message("user doesn't have a profile", ephemeral=True)


        except:
            await interaction.response.send_message("That's not a user id", ephemeral=True)


    @followers_list.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)




async def setup(bot):
    await bot.add_cog(FollowersList(bot))