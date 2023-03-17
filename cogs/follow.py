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

        
        m_user = user_in_db.get_user(interaction.user.id)
        user_id = user_in_db.get_user(user.id)
        

        if interaction.user.id == user.id :
            
            await interaction.response.send_message("You are Not allowed to Follow Yourself dummy")

        else:

            if m_user:

                if user_id:

                    try:
                        if user_check:
                            await interaction.response.send_message("You already follow this user")
                        

                        else:
                            await ffq.follow_user(user.id, interaction.user.id)
                            await interaction.response.send_message("User followed")

                        
                    except:
                        await interaction.response.send_message("That's not a user id")

                else:
                    await interaction.response.send_message(f"`{user.display_name.capitalize()}` doesn't have a profile \nYou Can only Follow a User who has a Profile")
                    
            else:
                await interaction.response.send_message("You don't have a profile yet")


        

    @followu.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)




async def setup(bot):
    await bot.add_cog(Follow(bot))