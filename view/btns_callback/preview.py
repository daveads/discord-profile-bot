import asyncio
import discord
from core import embed
from model import queries

from core.profile_data import profile_embed

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()

async def preview(bot, interaction, button):
    
    user = await bot.fetch_user(interaction.user.id)

    if user_in_db.get_user(interaction.user.id):

        profile_embed_data = await profile_embed(user, interaction)

        embed, file = profile_embed_data

        try:

            if file:
                await user.send(file=file, embed=embed)
                await interaction.response.defer()

            else:
                await user.send(embed=embed)
                await interaction.response.defer()
            
        except:

            if file:
                await interaction.response.send_message(file=file, embed=embed, ephemeral=True)
            
            else:
                await interaction.response.send_message(embed=embed, ephemeral=True)


    else:

        try:
            await user_embed.user_reply(user,"YOU DONT HAVE A PROFILE YET")
            await interaction.response.defer()
                

        except:
            await interaction.response.send_message("YOU DONT HAVE A PROFILE YET", ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response()