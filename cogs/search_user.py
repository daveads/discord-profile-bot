from typing import Optional
from discord.ext import commands
import discord
from discord import app_commands 
from model import queries
from core.profile_data import profile_embed

user_in_db = queries.PROFILEque()

class search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # /slash command


    def cooldown_for_everyone_but_me(interaction: discord.Interaction) -> Optional[app_commands.Cooldown]:
        if interaction.user.id == 840152379122384896:
            return None
        
        return app_commands.Cooldown(1, 3600) #1 hour 


    @app_commands.checks.dynamic_cooldown(cooldown_for_everyone_but_me)
    @app_commands.command(name="search", description="search for a user profile")
    async def find(self, interaction: discord.Interaction, user : discord.Member ):
        """ /search """

        try:
        
            if user_in_db.get_user(user.id):
              
                profile_embed_data = await profile_embed(user, interaction)
                await interaction.response.send_message(embed=profile_embed_data)


            else: 
                await interaction.response.send_message("user doesn't have a profile yet")


        except:
            await interaction.response.send_message("That's not a user id", ephemeral=True)


    @find.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)




async def setup(bot):
    await bot.add_cog(search(bot))