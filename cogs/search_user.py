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

        try:
            convert_id = int(first_value)
        
            user = await self.bot.fetch_user(convert_id)

            if user_in_db.get_user(user.id):
                user_d = user_in_db.get_user(interaction.user.id)
                user_data ={}
          
                for i in range(len(self.dic_key)):
                    user_data[self.dic_key[i]] = user_d[i]

                #await interaction.response.send_message(f'your data {user_data}, {interaction.user.mention} {first_value}' , ephemeral=False)


                # Emded

                embed=discord.Embed(title=f"PROFILE `{user_data['username']}` ", color=discord.Color.blue())
                embed.set_thumbnail(url=user.avatar)
                embed.add_field(name="NAME ", value=f"{user_data['name']}", inline=True)
                embed.add_field(name="LOCATION", value=f"{user_data['location']}", inline=True)
                embed.add_field(name="LOOKING FOR", value=f"{user_data['looking_for']}", inline=True)
                embed.add_field(name="HOBBIES", value=f"{user_data['hobbies']}",inline=True)
                embed.add_field(name="BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
                embed.set_footer(icon_url=user.avatar)

                await interaction.response.send_message(embed=embed)


            else: 
                await interaction.response.send_message("user doesn't have a profile yet")


        except:
            await interaction.response.send_message("That's not a user id")

async def setup(bot):
    await bot.add_cog(search(bot))